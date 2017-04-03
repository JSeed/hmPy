from PyQt5.QtWidgets import QMainWindow
from hmpy.gui.dashboard import ComponentDashboard
from hmpy.gui.menus.file import FileMenu
from hmpy.gui.menus.config import ConfigureMenu


class MainWindow(QMainWindow):
    """The main window for hmpy."""

    def __init__(self):
        """Initialize the MainWindow."""
        super().__init__()
        self.setCentralWidget(ComponentDashboard(self))
        self.setWindowTitle("hmPy")
        self.init_menu()
        self.showMaximized()

    def init_menu(self):
        """Initialize and populate the QMenuBar."""
        menu_bar = self.menuBar()
        menu_bar.addMenu(FileMenu(menu_bar))
        menu_bar.addMenu(ConfigureMenu(menu_bar))
