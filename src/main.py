import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import QQmlApplicationEngine

import views

from models.scheme import Scheme
from converter import convert

if __name__ == "__main__":

    convert("data/2024-bis-dez-25.CSV", "data/import-24.csv")
    sys.exit()

    scheme = Scheme()
    scheme.importCSV("data/data.csv")

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('src/style/Main.qml')

    # app = QGuiApplication()
    # view = QQuickView()
    # view.engine().addImportPath(sys.path[0])
    
    # view.loadFromModule("style", "Main")
    # view.show()
    # ex = app.exec()

    # del view
    sys.exit(app.exec())