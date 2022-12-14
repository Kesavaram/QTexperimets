#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle('hello world application')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()