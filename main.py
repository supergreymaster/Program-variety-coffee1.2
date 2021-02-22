import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QWidget


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle('Window2')
        self.Button.clicked.connect(self.work)
        # print(self.name, self.roasting, self.grains, self.taste, self.price, self.v, )

    def work(self):
        self.name = self.lineEdit_name.text()
        self.roasting = self.lineEdit_roasting.text()
        self.grains = self.lineEdit_grains.text()
        self.taste = self.lineEdit_taste.text()
        self.price = self.lineEdit_price.text()
        self.v = self.lineEdit_v.text()
        self.row = self.lineEdit_4.text()
        if self.row:
            try:
                a = int(self.row)
                if a <= 0:
                    self.add()
                else:
                    self.change()
            except ValueError:
                self.add()
        else:
            self.add()

    def add(self):
        con = sqlite3.connect("coffee.db")
        # name,roasting,grains,taste,price,v
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Сoffee(name,roasting,grains,taste,price,v)
                        VALUES('{self.name}', '{self.roasting}', '{self.grains}',
                        '{self.taste}', '{self.price}', '{self.v}')""")
        con.commit()
        print("Добавление произошло успешно")

    def change(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        res = cur.execute(f"SELECT id FROM Сoffee").fetchall()
        a = max([int(i[0]) for i in res])
        if a < int(self.row) and int(self.row) > 0:
            self.add()
            return
        if self.name:
            cur.execute(f"""UPDATE Сoffee SET name = '{self.name}' 
                            WHERE id == '{self.row}'""")
            con.commit()
        if self.roasting:
            cur.execute(f"""UPDATE Сoffee SET roasting = '{self.roasting}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.grains:
            cur.execute(f"""UPDATE Сoffee SET grains = '{self.grains}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.taste:
            cur.execute(f"""UPDATE Сoffee SET taste = '{self.taste}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.price:
            cur.execute(f"""UPDATE Сoffee SET price = '{self.price}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.v:
            cur.execute(f"""UPDATE Сoffee SET v = '{self.v}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        print("Изменение прошло успешно")



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.work)
        self.pushButton_2.clicked.connect(self.loc)

    def work(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        req = cur.execute("SELECT * FROM Сoffee").fetchall()
        print(req)
        self.tableWidget.setRowCount(len(req))
        for i in range(len(req)):
            for j in range(len(req[i])):
                item = QTableWidgetItem()
                item.setText(str(req[i][j]))
                self.tableWidget.setItem(i, j, item)

    def loc(self):
        self.w2 = Window2()
        self.w2.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())



