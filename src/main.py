import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

import views

if __name__ == "__main__":
    app = QGuiApplication()
    view = QQuickView()
    view.engine().addImportPath(sys.path[0])
    
    view.loadFromModule("style", "Main")
    view.show()
    ex = app.exec()

    del view
    sys.exit(ex)