import os
import tkinter as tk
from tkinter import filedialog


class ToolsFrame(tk.Frame):
    def __init__(self, master, coordinator, win_info):
        self.master = master
        self.coordinator = coordinator
        self.win_info = win_info
        self.width = None
        self.height = None

    def tool_setting(self):
        uni_fg = "mint cream"
        uni_bg = "gray22"

        tk.Frame.__init__(self, self.master, width=self.win_info.win_width, height=self.win_info.win_height, bg=uni_bg)
        self.width = 3*self.win_info.win_width/4
        self.height = self.win_info.win_height
        signature1 = tk.Label(self, text="created by Gabliw", bg=uni_bg, fg=uni_fg)
        signature2 = tk.Label(self, text="hchan11@naver.com", bg=uni_bg, fg=uni_fg)

        signature1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        signature2.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        page_descript = tk.Label(self, text="page :", bg=uni_bg, fg=uni_fg)
        page_entry = tk.Entry(self, width=5, bg=uni_bg, fg=uni_fg, bd=3, insertbackground=uni_fg,
                              highlightbackground=uni_fg, justify="right")

        page_descript.grid(row=2, column=0, padx=10, pady=10)
        page_entry.grid(row=2, column=1, pady=10)

        open_btn = tk.Button(self, text="OPEN", fg=uni_bg, highlightbackground=uni_fg,
                             command= self.open_callback)
        open_btn.grid(row=3, column=0, pady=10)

    def open_callback(self):
        self.win_info.file = filedialog.askopenfilename(initialdir=os.getcwd(), title="open file",
                                                        filetypes=[("image files", ['.jpg', '.jpeg', '.png'])])
        return self.export_data()

    def export_data(self):
        return self.coordinator.get_image_info(self.win_info.file)
