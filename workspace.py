import tkinter as Tk


class ScreenFrame(Tk.Frame):
    def __init__(self, master, win_info):
        Tk.Frame.__init__(self, master, width=3*win_info.win_width/4, height=win_info.win_height, bg="gray78")
        self.width = 3*win_info.win_width/4
        self.height = win_info.win_height


