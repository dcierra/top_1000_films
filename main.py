import sys
from films import *
import pandas as pd


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #подключение дата фрейма и установка столбцов и строк
        self.data = pd.read_csv('films_r.csv')
        self.ui.tableWidget.setColumnCount(len(self.data.columns))
        self.ui.tableWidget.setRowCount(10)

        #Перемешивание дата фрейма
        self.data = self.data.sample(frac=1)

        #Заполнение таблицы из дата фрейма
        for i in range(1000):
            for j in range(6):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.data.iat[i, j])))

        self.ui.tableWidget.resizeColumnsToContents()

        #Убираем рамки
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        #Обработчики кнопок
        self.ui.tBtn_closeWindow.clicked.connect(self.closeWindow)
        self.ui.tBtn_minimaze.clicked.connect(self.minimazeWindow)
        self.ui.btn_enter.clicked.connect(self.update)

    def update(self):
        self.data = self.data.sample(frac=1)
        for i in range(1000):
            for j in range(6):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.data.iat[i, j])))

    def closeWindow(self):
        if QtWidgets.QMessageBox.warning(self, 'Выход', 'Вы действительно хотите выйти?',
                                         QtWidgets.QMessageBox.Yes,
                                         QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            raise SystemExit
        else:
            return

    def minimazeWindow(self):
        self.showNormal()
        self.showMinimized()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    hz = GUI()
    hz.show()
    sys.exit(app.exec_())