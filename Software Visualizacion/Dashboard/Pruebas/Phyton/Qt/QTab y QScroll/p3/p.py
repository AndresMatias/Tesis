from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
import sys

class MainWindow(QMainWindow):
  def __init__(self,parent=None,*args,**kwargs):
    QMainWindow.__init__(self,parent,*args,**kwargs)

    self.tabs = QTabWidget(self)
    self.tabs.setTabBar(TabBar(self.tabs))
    self.tabs.setMovable(True)

    for color in ["red","orange","yellow","lime","green","cyan","blue","purple","violet","magenta"]:
      title = color
      widget = QWidget(styleSheet="background-color:%s" % color)

      pixmap = QPixmap(8,8)
      pixmap.fill(QColor(color))
      icon = QIcon(pixmap)

      self.tabs.addTab(widget,icon,title)

    self.setCentralWidget(self.tabs)
    self.showMaximized()

class TabBar(QTabBar):
    class MovingTab(QWidget):
        '''
        A private QWidget that paints the current moving tab
        '''
        def setPixmap(self, pixmap):
            self.pixmap = pixmap
            self.update()

        def paintEvent(self, event):
            qp = QPainter(self)
            qp.drawPixmap(0, 0, self.pixmap)

    def __init__(self,parent, *args, **kwargs):
        QTabBar.__init__(self,parent, *args, **kwargs)
        self.movingTab = None
        self.isMoving = False
        self.animations = {}
        self.pressedIndex = -1

    def isVertical(self):
        return self.shape() in (
            self.RoundedWest, 
            self.RoundedEast, 
            self.TriangularWest, 
            self.TriangularEast)

    def createAnimation(self, start, stop):
        animation = QVariantAnimation()
        animation.setStartValue(start)
        animation.setEndValue(stop)
        animation.setEasingCurve(QEasingCurve.InOutQuad)            
        def removeAni():
            for k, v in self.animations.items():
                if v == animation:
                    self.animations.pop(k)
                    animation.deleteLater()
                    break
        animation.finished.connect(removeAni)
        animation.valueChanged.connect(self.update)
        animation.start()
        return animation

    def layoutTab(self, overIndex):
        oldIndex = self.pressedIndex
        self.pressedIndex = overIndex
        if overIndex in self.animations:
            # if the animation exists, move its key to the swapped index value
            self.animations[oldIndex] = self.animations.pop(overIndex)
        else:
            start = self.tabRect(overIndex).topLeft()
            stop = self.tabRect(oldIndex).topLeft()
            self.animations[oldIndex] = self.createAnimation(start, stop)
        self.moveTab(oldIndex, overIndex)

    def finishedMovingTab(self):
        self.movingTab.deleteLater()
        self.movingTab = None
        self.pressedIndex = -1
        self.update()

    # reimplemented functions

    def tabSizeHint(self, i):
        return QSize(112, 48)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.pressedIndex = self.tabAt(event.pos())
            if self.pressedIndex < 0:
                return
            self.startPos = event.pos()

    def mouseMoveEvent(self,event):
        if not event.buttons() & Qt.LeftButton or self.pressedIndex < 0:
            super().mouseMoveEvent(event)
        else:
            delta = event.pos() - self.startPos
            if not self.isMoving and delta.manhattanLength() < QApplication.startDragDistance():
                # ignore the movement as it's too small to be considered a drag
                return

            if not self.movingTab:
                # create a private widget that appears as the current (moving) tab
                tabRect = self.tabRect(self.pressedIndex)
                overlap = self.style().pixelMetric(
                    QStyle.PM_TabBarTabOverlap, None, self)
                tabRect.adjust(-overlap, 0, overlap, 0)
                pm = QPixmap(tabRect.size())
                pm.fill(Qt.transparent)
                qp = QStylePainter(pm, self)
                opt = QStyleOptionTab()
                self.initStyleOption(opt, self.pressedIndex)
                if self.isVertical():
                    opt.rect.moveTopLeft(QPoint(0, overlap))
                else:
                    opt.rect.moveTopLeft(QPoint(overlap, 0))
                opt.position = opt.OnlyOneTab
                qp.drawControl(QStyle.CE_TabBarTab, opt)
                qp.end()
                self.movingTab = self.MovingTab(self)
                self.movingTab.setPixmap(pm)
                self.movingTab.setGeometry(tabRect)
                self.movingTab.show()

            self.isMoving = True
            self.startPos = event.pos()
            isVertical = self.isVertical()
            startRect = self.tabRect(self.pressedIndex)
            if isVertical:
                delta = delta.y()
                translate = QPoint(0, delta)
                startRect.moveTop(startRect.y() + delta)
            else:
                delta = delta.x()
                translate = QPoint(delta, 0)
                startRect.moveLeft(startRect.x() + delta)

            movingRect = self.movingTab.geometry()
            movingRect.translate(translate)
            self.movingTab.setGeometry(movingRect)

            if delta < 0:
                overIndex = self.tabAt(startRect.topLeft())
            else:
                if isVertical:
                    overIndex = self.tabAt(startRect.bottomLeft())
                else:
                    overIndex = self.tabAt(startRect.topRight())
            if overIndex < 0:
                return

            # if the target tab is valid, move the current whenever its position 
            # is over the half of its size
            overRect = self.tabRect(overIndex)
            if isVertical:
                if ((overIndex < self.pressedIndex and movingRect.top() < overRect.center().y()) or
                    (overIndex > self.pressedIndex and movingRect.bottom() > overRect.center().y())):
                        self.layoutTab(overIndex)
            elif ((overIndex < self.pressedIndex and movingRect.left() < overRect.center().x()) or
                (overIndex > self.pressedIndex and movingRect.right() > overRect.center().x())):
                    self.layoutTab(overIndex)

    def mouseReleaseEvent(self,event):
        super().mouseReleaseEvent(event)
        if self.movingTab:
            if self.pressedIndex > 0:
                animation = self.createAnimation(
                    self.movingTab.geometry().topLeft(), 
                    self.tabRect(self.pressedIndex).topLeft()
                )
                # restore the position faster than the default 250ms
                animation.setDuration(80)
                animation.finished.connect(self.finishedMovingTab)
                animation.valueChanged.connect(self.movingTab.move)
            else:
                self.finishedMovingTab()
        else:
            self.pressedIndex = -1
        self.isMoving = False
        self.update()

    def paintEvent(self, event):
        if self.pressedIndex < 0:
            super().paintEvent(event)
            return
        painter = QStylePainter(self)
        tabOption = QStyleOptionTab()
        for i in range(self.count()):
            if i == self.pressedIndex and self.isMoving:
                continue
            self.initStyleOption(tabOption, i)
            if i in self.animations:
                tabOption.rect.moveTopLeft(self.animations[i].currentValue())
            painter.drawControl(QStyle.CE_TabBarTab, tabOption)

if __name__ == "__main__":
  application = QApplication(sys.argv)
  mainwindow = MainWindow()
  application.exec_()      