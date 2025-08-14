import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

class MP4ToMP3Module:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        tk.Label(self.frame, text="MP4 转 MP3", font=("Arial", 14)).pack(pady=10)

        btn_select = tk.Button(self.frame, text="选择 MP4 文件(可多选)", command=self.select_files)
        btn_select.pack(pady=5)

        self.entry_files = tk.Entry(self.frame, width=60)
        self.entry_files.pack(pady=5)

        btn_convert = tk.Button(self.frame, text="开始转换", command=self.convert)
        btn_convert.pack(pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="选择 MP4 文件",
            filetypes=[("MP4 文件", "*.mp4"), ("所有文件", "*.*")]
        )
        if files:
            self.entry_files.delete(0, tk.END)
            self.entry_files.insert(0, ";".join(files))

    def convert(self):
        input_files = self.entry_files.get().strip()
        if not input_files:
            messagebox.showwarning("提示", "请先选择至少一个 MP4 文件！")
            return

        file_list = input_files.split(";")
        success = 0
        failed = []

        for f in file_list:
            f = f.strip()
            if not os.path.isfile(f):
                failed.append(f"{f} (文件不存在)")
                continue
            try:
                video = VideoFileClip(f)
                mp3_path = os.path.splitext(f)[0] + ".mp3"
                video.audio.write_audiofile(mp3_path)
                video.close()
                success += 1
            except Exception as e:
                failed.append(f"{f} ({e})")

        msg = f"转换完成！成功：{success} 个\n失败：{len(failed)} 个"
        if failed:
            msg += "\n失败文件：\n" + "\n".join(failed)
        messagebox.showinfo("结果", msg)

    def get_frame(self):
        return self.frame
