"""
Contributed by Gabliw (hchan11@naver.com)
"""
from workspace import ScreenFrame
from tools import ToolsFrame
import tkinter as Tk


WIDTH_REDUCE = 200
HEIGHT_REDUCE = 200


class Reactor:
    def __init__(self):
        self.win_width = None
        self.win_height = None

    def window_setting(self, width, height):
        self.win_width = width
        self.win_height = height

    def window_size(self):
        return self.win_width, self.win_height


class Application(Tk.Frame):
    def __init__(self, window, win_info):
        Tk.Frame.__init__(self, window)
        self.win_info = win_info
        self.master.title("Grid Manager")

        tools = ToolsFrame(window, self.win_info)
        screens = ScreenFrame(window, self.win_info)

        screens.pack(side='left', expand=False, fill=Tk.Y, padx=2, pady=2)
        tools.pack(side='left', expand=True, fill=Tk.BOTH, padx=2, pady=2)


if __name__ == "__main__":
    infoster = Reactor()
    main_structure = Tk.Tk()
    main_structure.title("Masking Mk.2")
    infoster.window_setting(main_structure.winfo_screenwidth()-WIDTH_REDUCE,
                            main_structure.winfo_screenheight()-HEIGHT_REDUCE)

    main_structure.geometry(f"{infoster.win_width}x{infoster.win_height}")
    main_structure.resizable(False, False)
    application = Application(main_structure, infoster)

    main_structure.mainloop()

