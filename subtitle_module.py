
# subtitle_module.py

import os
import re
from PySide6.QtWidgets import QFileDialog, QMessageBox

class SubtitleToTextModule:
    def __init__(self, parent_widget):
        # parent_widget: QWidget，用于 QFileDialog、QMessageBox
        self.parent = parent_widget

    # 核心转换逻辑
    def subtitle_to_text(self, input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"{input_file} 不是 UTF-8 编码")

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

    # 选择文件
    def select_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self.parent,
            "选择字幕文件",
            "",
            "字幕文件 (*.srt *.vtt);;所有文件 (*.*)"
        )
        return file_paths

    # 转换文件列表
    def convert_files(self, file_list):
        success_files = []
        fail_files = []

        for input_file in file_list:
            input_file = input_file.strip()
            if not os.path.isfile(input_file):
                fail_files.append(f"{input_file} (文件不存在)")
                continue

            output_file = os.path.splitext(input_file)[0] + ".txt"
            try:
                self.subtitle_to_text(input_file, output_file)
                success_files.append(output_file)
            except Exception as e:
                fail_files.append(f"{input_file} ({e})")

        # 弹窗显示结果（可选）
        if self.parent:
            msg = ""
            if success_files:
                msg += f"成功转换：{len(success_files)} 个\n"
            if fail_files:
                msg += f"失败：{len(fail_files)} 个\n失败文件:\n" + "\n".join(fail_files)
            if msg:
                QMessageBox.information(self.parent, "转换结果", msg)

        return success_files, fail_files
