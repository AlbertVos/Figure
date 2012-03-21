from Tkinter import *
import threading

class FigureThread(threading.Thread):
    def __init__(self, figure):
        threading.Thread.__init__(self)
        self.figure = figure
    def run(self):
        self.figure.mainloop()

class Figure(Tk):
    def __init__(self, width=600, height=600, title='Figure'):
        Tk.__init__(self)
        self.title(title)
        self.canvas = Canvas(self, width=width, height=height, bg="#fffff0")
        self.canvas.pack(side=TOP, padx=10, pady=10)

        self.nx = 10
        self.x0 = int(width / 10)
        self.dx = int(width - 2 * self.x0) / self.nx
        self.x1 = self.x0 + self.nx * self.dx

        self.ny = 10
        self.y0 = int(height / 10)
        self.dy = int(height - 2 * self.y0) / self.ny
        self.y1 = self.y0 + self.ny * self.dy

        for i in range(self.nx + 1):
            self.canvas.create_line([self.x0 + i * self.dx, self.y0
                , self.x0 + i * self.dx, self.y1], fill='#c0c0c0')
        for i in range(self.ny + 1):
            self.canvas.create_line([self.x0, self.y0 + i * self.dy
                , self.x1, self.y0 + i * self.dy], fill='#c0c0c0')
        t = FigureThread(self)
        #t.setDaemon(True)
        t.start()

    def plot(self, x, y, coords, color):
        xmin = coords[0]
        xmax = coords[1]
        ymin = coords[2]
        ymax = coords[3]
        for i in range(len(x)):
            px = float(x[i] - xmin) * float(self.x1 - self.x0) / float(xmax - xmin)
            px = int(px) + self.x0
            py = float(y[i] - ymin) * float(self.y1 - self.y0) / float(ymax - ymin)
            py =  self.y1 - int(py)
            self.canvas.create_oval([px - 2, py - 2, px + 2, py + 2]
                , outline=color, fill=color)


#f = Figure()
#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#coords = [0, 10, 0, 10]
#f.plot(x, y, 'red')

