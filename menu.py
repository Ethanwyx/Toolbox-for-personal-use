# main_app.py
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from subtitle_module import SubtitleToTextModule
from mp4_to_mp3_module import MP4ToMP3Module

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自用工具箱")
        self.root.geometry("700x500")

        self.menu_frame = tk.Frame(root, width=150)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.content_frame = tk.Frame(root)
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 导入模块实例
        self.modules = {
            "字幕转纯文本": SubtitleToTextModule(self.content_frame),
            "MP4 转 MP3": MP4ToMP3Module(self.content_frame),
            # 此处可扩展其他模块
        }

        for i, name in enumerate(self.modules):
            btn = tk.Button(self.menu_frame, text=name, command=lambda n=name: self.show_module(n))
            btn.pack(fill=tk.X, pady=2, padx=5)

        self.current_module = None
        self.show_module("字幕转纯文本")
        self.show_module("MP4 转 MP3")

    def show_module(self, name):
        if self.current_module:
            self.current_module.get_frame().pack_forget()
        self.current_module = self.modules[name]
        self.current_module.get_frame().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
