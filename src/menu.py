# menu.py
import sys
from PySide6 import QtWidgets
from subtitle_module import SubtitleToTextModule
from mp4_to_mp3_module import MP4ToMP3Module
from danmu_module import DanmuExtractModule
from ui_toolbox import Ui_MainWindow


class ToolboxApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 把 UI 加载到 QMainWindow
        self.subtitle_file = None
        self.mp4_files = []  # 支持多文件

        # 模块实例化为主窗口属性，防止线程被回收
        self.mp4_module = MP4ToMP3Module(self)
        self.danmu_module = DanmuExtractModule(self)  # ✅ 提前初始化，避免 AttributeError

        self.bind_events()

    # ---------------- 绑定按钮事件 ----------------
    def bind_events(self):
        # 左侧菜单切换
        self.ui.menuList.currentRowChanged.connect(self.ui.stackedWidget.setCurrentIndex)

        # 字幕模块
        self.ui.btn_select_subtitle.clicked.connect(self.select_subtitle_file)
        self.ui.btn_convert_subtitle.clicked.connect(self.convert_subtitle)

        # MP4模块
        self.ui.btn_select_mp4.clicked.connect(self.select_mp4_files)
        self.ui.btn_convert_mp4.clicked.connect(self.convert_mp4)

        # 弹幕模块
        self.ui.btn_select_danmu.clicked.connect(self.select_danmu_file)
        self.ui.btn_select_output_danmu.clicked.connect(self.select_output_path)
        self.ui.btn_convert_danmu.clicked.connect(self.convert_danmu)

    # ---------------- 字幕模块 ----------------
    def select_subtitle_file(self):
        module = SubtitleToTextModule(self)
        files = module.select_files()
        if files:
            self.subtitle_file = files[0]
            self.ui.txt_output_subtitle.clear()
            self.ui.txt_output_subtitle.append(f"选中的字幕文件: {self.subtitle_file}")

    def convert_subtitle(self):
        if not self.subtitle_file:
            self.ui.txt_output_subtitle.append("请先选择字幕文件 ⚠️")
            return

        module = SubtitleToTextModule(self)
        success_files, fail_files = module.convert_files([self.subtitle_file])

        self.ui.txt_output_subtitle.clear()

        if success_files:
            for f in success_files:
                self.ui.txt_output_subtitle.append(f"生成文件: {f}")
            self.ui.txt_output_subtitle.append("字幕转文本完成 ✅")

        if fail_files:
            for f in fail_files:
                self.ui.txt_output_subtitle.append(f"失败文件: {f}")
            self.ui.txt_output_subtitle.append("字幕转文本失败 ❌\n当前仅支持UTF-8编码！")

    # ---------------- MP4模块 ----------------
    def select_mp4_files(self):
        files = self.mp4_module.select_files()
        if files:
            self.mp4_files = files
            self.ui.txt_output_mp4.clear()
            self.ui.txt_output_mp4.append("选中的 MP4 文件:")
            for f in files:
                self.ui.txt_output_mp4.append(f)
            self.ui.progress_mp4.setValue(0)

    def convert_mp4(self):
        if not self.mp4_files:
            self.ui.txt_output_mp4.append("请先选择 MP4 文件 ⚠️")
            return

        self.ui.progress_mp4.setValue(0)

        def update_progress(percent):
            self.ui.progress_mp4.setValue(percent)

        def on_finished(success_files, fail_files):
            self.ui.txt_output_mp4.clear()
            for f in success_files:
                self.ui.txt_output_mp4.append(f"生成文件: {f}")
            for f in fail_files:
                self.ui.txt_output_mp4.append(f"失败文件: {f}")
            self.ui.progress_mp4.setValue(100)

        self.mp4_module.convert_files(
            self.mp4_files,
            progress_callback=update_progress,
            finished_callback=on_finished
        )

    # ---------------- 弹幕模块 ----------------
    def select_danmu_file(self):
        self.danmu_module = DanmuExtractModule(self)
        file_path = self.danmu_module.select_file()
        if file_path:
            self.ui.txt_output_danmu.setText(f"已选择文件: {file_path}")

    def select_output_path(self):
        file_path = self.danmu_module.select_output_path()
        if file_path:
            self.ui.txt_output_danmu.append(f"输出路径: {file_path}")

    def convert_danmu(self):
        text = self.danmu_module.extract_danmu()
        if text:
            self.ui.txt_output_danmu.setText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ToolboxApp()
    window.show()
    sys.exit(app.exec())
