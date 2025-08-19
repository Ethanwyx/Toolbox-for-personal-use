# danmu_module.py
import re
from PySide6.QtWidgets import QFileDialog


class DanmuExtractModule:
    def __init__(self, parent=None):
        self.parent = parent
        self.input_file = None   # 输入的XML弹幕文件
        self.output_file = None  # 输出的TXT文件

    def select_file(self):
        """选择XML弹幕文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            None, "选择弹幕XML文件", "", "XML Files (*.xml);;All Files (*)"
        )
        if file_path:
            self.input_file = file_path
        return self.input_file

    def select_output_path(self):
        """选择输出TXT路径"""
        file_path, _ = QFileDialog.getSaveFileName(
            None, "保存弹幕TXT文件", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            self.output_file = file_path
        return self.output_file

    def extract_danmu(self):
        """从XML中提取弹幕文本，并写入TXT"""
        if not self.input_file:
            return None

        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            return f"读取文件失败: {e}"

        # 提取 <d> 标签中的内容
        contents = re.findall(r"<d [^>]*>(.*?)</d>", text)

        # 如果用户指定了输出文件，则写入
        if self.output_file:
            try:
                with open(self.output_file, "w", encoding="utf-8") as f:
                    for c in contents:
                        f.write(c + "\n")
            except Exception as e:
                return f"写入文件失败: {e}"

        return "\n".join(contents)
