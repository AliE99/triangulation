from tkinter import *


class Graphic:

    def draw(self, diameter, name):
        canvas_width = 1280
        canvas_height = 760
        python_green = "#476042"

        master = Tk()

        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        w.pack()
        points = []
        w.create_text(canvas_width / 2,
                      20,
                      text=name, fill="#476042")

        for i in range(0, len(self)):
            points.append(self[i].x * 15)
            points.append(self[i].y * 15)

        w.create_polygon(points, outline=python_green,
                         fill='#30e3ca', width=5)

        for j in range(0, len(diameter) - 1, 2):
            w.create_line(points[2 * diameter[j]], points[2 * diameter[j] + 1], points[2 * diameter[j + 1]],
                          points[2 * diameter[j + 1] + 1], fill="#40514e",width=2)

        mainloop()
