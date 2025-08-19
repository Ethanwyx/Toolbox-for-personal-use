
# mp4_to_mp3_module.py

import os
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QFileDialog, QMessageBox
from moviepy.video.io.VideoFileClip import VideoFileClip

class MP4ToMP3Worker(QThread):
    progress_signal = Signal(int)           # 总进度 0~100
    finished_signal = Signal(list, list)   # 成功文件列表, 失败文件列表

    def __init__(self, file_list):
        super().__init__()
        self.file_list = file_list

    def run(self):
        success_files = []
        fail_files = []

        total_files = len(self.file_list)
        for idx, input_file in enumerate(self.file_list, 1):
            input_file = input_file.strip()
            if not os.path.isfile(input_file):
                fail_files.append(f"{input_file} (文件不存在)")
                self.progress_signal.emit(int(idx / total_files * 100))
                continue

            try:
                video = VideoFileClip(input_file)
                mp3_path = os.path.splitext(input_file)[0] + ".mp3"
                video.audio.write_audiofile(mp3_path)  # 只保留输出路径
                video.close()
                success_files.append(mp3_path)
            except Exception as e:
                fail_files.append(f"{input_file} ({e})")

            self.progress_signal.emit(int(idx / total_files * 100))

        self.finished_signal.emit(success_files, fail_files)

class MP4ToMP3Module:
    def __init__(self, parent_widget):
        self.parent = parent_widget
        self.worker = None

    def select_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self.parent,
            "选择 MP4 文件",
            "",
            "MP4 文件 (*.mp4);;所有文件 (*.*)"
        )
        return file_paths

    def convert_files(self, file_list, progress_callback=None, finished_callback=None):
        self.worker = MP4ToMP3Worker(file_list)
        if progress_callback:
            self.worker.progress_signal.connect(progress_callback)
        if finished_callback:
            self.worker.finished_signal.connect(finished_callback)
        self.worker.start()
