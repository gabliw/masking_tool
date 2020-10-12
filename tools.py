import tkinter as Tk


class ToolsFrame(Tk.Frame):
    def __init__(self, master, win_info):
        uni_fg = "mint cream"
        uni_bg = "gray22"
        Tk.Frame.__init__(self, master, width=win_info.win_width, height=win_info.win_height, bg=uni_bg)
        self.width = 3*win_info.win_width/4
        self.height = win_info.win_height

        signature1 = Tk.Label(self, text="created by Gabliw", bg=uni_bg, fg=uni_fg)
        signature2 = Tk.Label(self, text="hchan11@naver.com", bg=uni_bg, fg=uni_fg)

        signature1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        signature2.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        page_descipt = Tk.Label(self, text="page :", bg=uni_bg, fg=uni_fg)
        page_entry = Tk.Entry(self, width=5, bg=uni_bg, fg=uni_fg, bd=3, insertbackground=uni_fg,
                              highlightbackground="gray16", justify="right")

        page_descipt.grid(row=2, column=0, padx=10, pady=10)
        page_entry.grid(row=2, column=1, pady=10)

        load_btn = Tk.Button()

        Tk.Button()