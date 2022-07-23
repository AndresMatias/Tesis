import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation,QRect,QSize,QSequentialAnimationGroup


class PropertyAnimation(QPropertyAnimation):
    def __init__(self, target, property):
        super(PropertyAnimation, self).__init__(target, property.encode())
        self._func = None

    def setUpdateFunc(self, func):
        # Establecer la función que se ejecutará cuando se active la animación
        self._func = func

    def updateCurrentValue(self, value):
        if self._func is None:
            super(PropertyAnimation, self).updateCurrentValue(value)
        else:
            self._func(self.targetObject(), value)


class Example(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        button = QPushButton('Haz clic en mí, haz clic en mí')
        button.setFixedSize(QSize(100, 100))
        button.setStyleSheet('QWidget{background-color: red;}')
        layout.addWidget(button)


        self.animation_group = QSequentialAnimationGroup()

        def update(target, value):
            # Función de actualización, configure el tamaño del botón en esta función
            target.setFixedSize(value)

        # Componentes y propiedades de unión
        # Adelante
        animation = PropertyAnimation(button, 'size')
        animation.setUpdateFunc(update)
        animation.setDuration(1000)
        animation.setStartValue(QSize(50, 50))
        animation.setEndValue(QSize(150, 150))
        # La animación que se agregará a la secuencia de animación no puede llamar a setLoopCount y comenzar por separado
        # animation.setLoopCount(-1)
        # animation.start()
        self.animation_group.addAnimation(animation)

        # Contrarrestar
        animation = PropertyAnimation(button, 'size')
        animation.setUpdateFunc(update)
        animation.setDuration(1000)
        animation.setStartValue(QSize(150, 150))
        animation.setEndValue(QSize(50, 50))
        self.animation_group.addAnimation(animation)

        self.animation_group.setLoopCount(-1)
        self.animation_group.start()

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()