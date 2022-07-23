from tkinter import *
import tk_tools

root=Tk()
gauge = tk_tools.Gauge(root, max_value=100.0,
                       label='speed', unit='km/h')
gauge.grid()
gauge.set_value(10)
root.mainloop()
