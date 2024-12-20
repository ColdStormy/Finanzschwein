import QtQuick 6.2
import QtQuick.Controls 6.2
import MyApp 1.0  // Import the module defined in Python

Rectangle {
    id: main
    width: 200
    height: 200
    color: "green"

    CounterHandler {
        id: counter
    }

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Count: " + counter.count
            font.pointSize: 24
        }

        Button {
            text: "Increment"
            onClicked: counter.increment()
        }

        Button {
            text: "Reset"
            onClicked: counter.reset()
        }
    }
}