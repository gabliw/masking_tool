"""
Contributed by Gabliw (hchan11@naver.com)
"""
from workspace import ScreenFrame
from tools import ToolsFrame
import tkinter as tk


WIDTH_REDUCE = 200
HEIGHT_REDUCE = 200


class Reactor:
    def __init__(self):
        self.win_width = None
        self.win_height = None
        self.file = None

    def window_setting(self, width, height):
        self.win_width = width
        self.win_height = height

    def window_size(self):
        return self.win_width, self.win_height


class Application(tk.Frame):
    def __init__(self, window, win_info):
        tk.Frame.__init__(self, window)
        self.win_info = win_info
        self.master.title("Grid Manager")

        self.screens = ScreenFrame(window, self.win_info)
        self.tools = ToolsFrame(window, self.screens, self.win_info)

    def screen_update(self):
        self.tools.tool_setting()
        self.screens.screen_update()
        self.tools.pack(side='left', expand=True, fill=tk.BOTH, padx=2, pady=2)


if __name__ == "__main__":
    infoster = Reactor()
    main_structure = tk.Tk()
    main_structure.title("Masking Mk.2")
    infoster.window_setting(main_structure.winfo_screenwidth()-WIDTH_REDUCE,
                            main_structure.winfo_screenheight()-HEIGHT_REDUCE)

    main_structure.geometry(f"{infoster.win_width}x{infoster.win_height}")
    main_structure.resizable(False, False)
    application = Application(main_structure, infoster)

    application.screen_update()
    main_structure.mainloop()

