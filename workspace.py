from PIL import ImageTk, Image
import tkinter as tk


class ScreenFrame(tk.Frame):
    def __init__(self, master, win_info):
        tk.Frame.__init__(self, master, width=3*win_info.win_width/4, height=win_info.win_height, bg="gray78")
        self.width = 3*win_info.win_width/4
        self.height = win_info.win_height
        self.win_info = win_info

    def screen_update(self):
        img = ImageTk.PhotoImage(Image.open(self.win_info.file))
        panel = tk.Label(self, image=img)

        panel.pack(side='left', expand=False)

    def get_image_info(self, data):
        self.win_info.file = data
        print(data)
        self.screen_update()




