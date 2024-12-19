from PySide6.QtCore import QObject, Property, Signal, Slot, QUrl
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "MyApp"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class CounterHandler(QObject):
    # Signal to notify QML when the count changes
    countChanged = Signal()

    def __init__(self):
        super().__init__()
        self._count = 0

    # Getter method for the count property
    def get_count(self):
        return self._count

    # Setter method for the count property
    def set_count(self, value):
        if self._count != value:
            self._count = value
            self.countChanged.emit()  # Notify QML that the count has changed

    # Property definition
    count = Property(int, get_count, set_count, notify=countChanged)

    # Slot to increment the count
    @Slot()
    def increment(self):
        self.set_count(self._count + 1)

    # Slot to reset the count
    @Slot()
    def reset(self):
        self.set_count(0)