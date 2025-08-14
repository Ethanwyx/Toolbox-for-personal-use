# subtitle_module.py

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import re
import os
from tkinter import filedialog, messagebox

class SubtitleToTextModule:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        tk.Label(self.frame, text="字幕文件转纯文字", font=("Arial", 14)).pack(pady=10)

        self.entry_files = tk.Entry(self.frame, width=60)
        self.entry_files.pack(pady=5)

        btn_select = tk.Button(self.frame, text="选择 srt 文件(可多选)", command=self.select_files)
        btn_select.pack(pady=5)

        btn_convert = tk.Button(self.frame, text="开始转换", command=self.convert)
        btn_convert.pack(pady=10)

    def subtitle_to_text(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        text_lines = []
        for line in lines:
            if re.match(r'^\d+$', line.strip()):
                continue
            if re.match(r'^\d{2}:\d{2}:\d{2}[,\.]\d{3}\s-->\s\d{2}:\d{2}:\d{2}[,\.]\d{3}$', line.strip()):
                continue
            if line.strip().upper() == 'WEBVTT':
                continue
            if not line.strip():
                continue
            text_lines.append(line.strip())

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_lines))

    def select_files(self):
        file_paths = filedialog.askopenfilenames(
            title="选择字幕文件",
            filetypes=(("字幕文件", "*.srt *.vtt"), ("所有文件", "*.*"))
        )
        if file_paths:
            self.entry_files.delete(0, tk.END)
            self.entry_files.insert(0, ";".join(file_paths))

    def convert(self):
        input_files = self.entry_files.get().strip()
        if not input_files:
            messagebox.showwarning("提示", "请先选择至少一个字幕文件！")
            return

        file_list = input_files.split(";")
        success_count = 0
        fail_count = 0
        fail_files = []

        for input_file in file_list:
            input_file = input_file.strip()
            if not os.path.isfile(input_file):
                fail_count += 1
                fail_files.append(input_file)
                continue

            output_file = os.path.splitext(input_file)[0] + ".txt"
            try:
                self.subtitle_to_text(input_file, output_file)
                success_count += 1
            except Exception as e:
                fail_count += 1
                fail_files.append(f"{input_file} ({e})")

        msg = f"转换完成！\n成功：{success_count} 个\n失败：{fail_count} 个"
        if fail_count > 0:
            msg += "\n失败文件：\n" + "\n".join(fail_files)

        messagebox.showinfo("结果", msg)

    def get_frame(self):
        return self.frame
