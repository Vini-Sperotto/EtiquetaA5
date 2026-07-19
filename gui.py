import tkinter as tk
from tkinter import filedialog
from pdf_processor import process_pdf

import os
import platform
import subprocess

config = {"mode": "save"}


def open_file(path):
    """
    Abre um arquivo utilizando o programa padrão do sistema operacional.
    Compatível com Windows, macOS e Linux.
    """

    system = platform.system()

    if system == "Windows":
        os.startfile(path)

    elif system == "Darwin":
        subprocess.call(["open", path])

    else:
        subprocess.call(["xdg-open", path])


def select_file():

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    output = process_pdf(file_path, config["mode"])

    if config["mode"] in ("open", "hybrid"):
        open_file(output)


def set_mode(value):
    config["mode"] = value


def start_app():

    root = tk.Tk()

    root.title("Etiqueta para A5")
    root.geometry("260x180")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Etiqueta para A5",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    tk.Radiobutton(
        root,
        text="Só salvar",
        value="save",
        command=lambda: set_mode("save")
    ).pack(anchor="w")

    tk.Radiobutton(
        root,
        text="Salvar e abrir",
        value="open",
        command=lambda: set_mode("open")
    ).pack(anchor="w")

    tk.Radiobutton(
        root,
        text="Modo híbrido",
        value="hybrid",
        command=lambda: set_mode("hybrid")
    ).pack(anchor="w")

    tk.Button(
        root,
        text="Processar PDF",
        command=select_file
    ).pack(pady=15)

    root.mainloop()