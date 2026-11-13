# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk
# Requires tkinterdnd2:  pip install tkinterdnd2
from tkinterdnd2 import DND_FILES, TkinterDnD


class DndWindow(ctk.CTk, TkinterDnD.DnDWrapper):
    """CustomTkinter window with tkinterdnd2 drop support mixed in."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loads the tkdnd Tcl package into this interpreter.
        self.TkdndVersion = TkinterDnD._require(self)


THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#4a9eff"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT_FAMILY = "Segoe UI"
THEME_FONT_SIZE = 10


def apply_theme(root):
    """Apply the project theme to a window. CustomTkinter styles per widget,
    so the widgets themselves carry the rest of the colours."""
    root.configure(fg_color=THEME_BG)


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("520x380")
        apply_theme(root)

        self.label1 = ctk.CTkLabel(root, text="DM-Decoder_V.1", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=130, height=30)
        self.label1.grid(row=0, column=0, columnspan=2, sticky="w", padx=4, pady=4)

        self.Capture = ctk.CTkButton(root, text="Capture", command=self.on_Capture, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=96, height=32)
        self.Capture.grid(row=2, column=1, columnspan=2, sticky="w", padx=4, pady=4)

        self.Export = ctk.CTkButton(root, text="Export as CSV", command=self.on_Export, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=96, height=32)
        self.Export.grid(row=6, column=1, columnspan=2, sticky="w", padx=4, pady=4)

        self.Photo = ctk.CTkFrame(root, border_width=2, fg_color=THEME_BG, width=200, height=140)
        self.Photo_caption = ctk.CTkLabel(self.Photo, text="photo", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE))
        self.Photo_caption.place(x=10, y=4)
        self.Photo.grid(row=1, column=4, rowspan=3, sticky="nsew", padx=4, pady=4)
        self.Photo.drop_target_register(DND_FILES)
        self.Photo.dnd_bind("<<Drop>>", self.on_Photo_drop)

        self.CSV_preview = ctk.CTkFrame(root, border_width=2, fg_color=THEME_BG, width=200, height=140)
        self.CSV_preview_caption = ctk.CTkLabel(self.CSV_preview, text="CSV preview", text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE))
        self.CSV_preview_caption.place(x=10, y=4)
        self.CSV_preview.grid(row=5, column=4, rowspan=3, sticky="nsew", padx=4, pady=4)
        self.CSV_preview.drop_target_register(DND_FILES)
        self.CSV_preview.dnd_bind("<<Drop>>", self.on_CSV_preview_drop)

        self.separator1 = ctk.CTkFrame(root, corner_radius=0, fg_color="gray70", width=520, height=2)
        self.separator1.grid(row=4, column=0, columnspan=6, sticky="ew", padx=4, pady=4)

        root.columnconfigure(0, minsize=90, weight=1)
        root.columnconfigure(1, minsize=56, weight=1)
        root.columnconfigure(2, minsize=56, weight=1)
        root.columnconfigure(3, minsize=120, weight=1)
        root.columnconfigure(4, minsize=208, weight=1)
        root.columnconfigure(5, minsize=38, weight=1)
        root.rowconfigure(0, minsize=38)
        root.rowconfigure(1, minsize=68, weight=1)
        root.rowconfigure(2, minsize=40, weight=1)
        root.rowconfigure(3, minsize=60, weight=1)
        root.rowconfigure(4, minsize=34)
        root.rowconfigure(5, minsize=68, weight=1)
        root.rowconfigure(6, minsize=40, weight=1)
        root.rowconfigure(7, minsize=62, weight=1)

    def on_Capture(self):
        pass

    def on_Export(self):
        pass

    def on_Photo_drop(self, event):
        """Files dropped on Photo."""
        paths = self.root.tk.splitlist(event.data)
        # TODO: do something with paths

    def on_CSV_preview_drop(self, event):
        """Files dropped on CSV_preview."""
        paths = self.root.tk.splitlist(event.data)
        # TODO: do something with paths


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = DndWindow()
    app = Application(root)
    root.mainloop()
