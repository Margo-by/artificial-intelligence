from tkinter import Tk
from gui import App

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()