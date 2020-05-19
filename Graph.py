from tkinter import*
class Bars:

    def __init__(self, canvas, data):
        self.canvas = canvas
        self.data = data
        self.canvas_dimensions = (self.canvas.winfo_reqheight(), self.canvas.winfo_reqwidth())


    def drawData(self, colors):
        self.canvas.delete("all")
        xWidth = self.canvas_dimensions[1] * 2 / (len(self.data) + 1)
        offcanvas, space = 20, 5
        normalizedData = [i / max(self.data) for i in self.data]
        for index, height in enumerate(normalizedData):
            xi = index * xWidth + offcanvas + space
            yi = self.canvas_dimensions[0] - (height * self.canvas_dimensions[0] / 1.10)
            xf = (index + 1) * xWidth + offcanvas
            yf = 425
            self.canvas.create_rectangle(xi, yi, xf, yf, fill=colors[index])
            self.canvas.create_text(xi,yi+2,anchor=SW,text=self.data[index],fill='white')
