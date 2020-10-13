import time
from PIL import ImageTk, Image
import tkinter as tk


class ScreenFrame(tk.Frame):
    def __init__(self, master, win_info):
        tk.Frame.__init__(self, master, width=3*win_info.win_width/4, height=win_info.win_height, bg="gray78")
        self.width = 3*win_info.win_width/4
        self.height = win_info.win_height
        self.win_info = win_info
        self.canv = None

    def screen_update(self):
        if self.win_info.file is None:
            self.pack(side='left', expand=False, fill=tk.Y, padx=2, pady=2)
        else:
            img = ImageTk.PhotoImage(Image.open(self.win_info.file))
            self.canv = tk.Canvas()
            self.canv.create_image((150, 150), image=img)
            self.canv.pack()

    def get_image_info(self, data):
        self.win_info.file = data
        print(data)
        self.screen_update()




