import sys
from datetime import datetime
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl, QObject, pyqtSlot
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel
from khayyam import JalaliDatetime


class Bridge(QObject):
    @pyqtSlot(float, float)
    def printCoordinates(self, lat, lng):
        ui.textEdit.setText(str(lat))
        ui.textEdit_2.setText(str(lng))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 844)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 680, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: green;")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 740, 161, 51))
        self.pushButton_2.setStyleSheet('background-color: red;')
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 131, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet('background-color: white;')

        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 130, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet('background-color: white;')

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 229, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(70, 390, 441, 271))
        self.listView.setStyleSheet('background-color: white;')
        self.listView.setObjectName("listView")

        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setStyleSheet('background-color: white;')
        self.listView_2.setGeometry(QtCore.QRect(560, 390, 441, 271))
        self.listView_2.setObjectName("listView_2")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 70, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        font = QtGui.QFont()
        font.setPointSize(11)
        self.web_view = QWebEngineView(self.centralwidget)
        self.web_view.setGeometry(QtCore.QRect(600, 110, 400, 250))
        self.bridge = Bridge()
        self.channel = QWebChannel()
        self.channel.registerObject("bridge", self.bridge)
        self.web_view.page().setWebChannel(self.channel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 26))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet('background-color: white;')
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the button click to the slot
        self.pushButton.clicked.connect(self.add_to_list_view)
        self.pushButton_2.clicked.connect(QtWidgets.QApplication.instance().quit)

        self.load_map()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.pushButton_2.setText(_translate("MainWindow", "exit"))
        self.label.setText(_translate("MainWindow", "latitude :"))
        self.label_2.setText(_translate("MainWindow", "longitude :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1 day"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3 days"))
        self.comboBox.setItemText(2, _translate("MainWindow", "7 days"))
        self.comboBox.setItemText(3, _translate("MainWindow", "14 days"))
        self.comboBox.setItemText(4, _translate("MainWindow", "16 days"))
        self.label_3.setText(_translate("MainWindow", "number of days :"))
        self.label_4.setText(_translate("MainWindow", "map for coordinates :"))

    def load_map(self):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
            <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
            <style>
                #map {
                    height: 100vh;
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <div id="map"></div>
            <script>
                var map = L.map('map').setView([35.6895, 51.3896], 16);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 10, // Set the maximum zoom level
                }).addTo(map);

                L.control.scale().addTo(map);

                var marker;

                new QWebChannel(qt.webChannelTransport, function(channel) {
                    window.bridge = channel.objects.bridge;
                });

                map.on('click', function (e) {
                    if (marker) {
                        map.removeLayer(marker);
                    }
                    var clickedLat = e.latlng.lat;
                    var clickedLng = e.latlng.lng;
                    marker = L.marker([clickedLat, clickedLng]).addTo(map);
                    window.bridge.printCoordinates(clickedLat, clickedLng);
                });
            </script>
        </body>
        </html>
        """
        self.web_view.setHtml(html_content, QUrl('about:blank'))

    def add_to_list_view(self):
        # Get the text from the inputs
        latitude = self.textEdit.toPlainText()
        longitude = self.textEdit_2.toPlainText()
        num_days = self.comboBox.currentText()
        day = int(num_days[0])

        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&forecast_days={day}'
        response = requests.get(url)
        data = response.json()

        model = QtGui.QStandardItemModel()
        model2 = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        self.listView_2.setModel(model2)

        for i in range(len(data['hourly']['time'])):
            date = datetime.strptime(data['hourly']['time'][i], "%Y-%m-%dT%H:%M")
            latitude_item = QtGui.QStandardItem(
                f'{str(JalaliDatetime(datetime(date.year, date.month, date.day, date.hour, date.minute)))} = temp:{data["hourly"]["temperature_2m"][i]}, wind speed:{data["hourly"]["wind_speed_10m"][i]}\n')
            model.appendRow(latitude_item)
        sunrise = data["daily"]["sunrise"][0].split("T")
        sunset = data["daily"]["sunset"][0].split("T")
        longitude_item = QtGui.QStandardItem(
            f'maximum temp: {data["daily"]["temperature_2m_max"][0]}\nminimum temp: {data["daily"]["temperature_2m_min"][0]}\nsunrise: {sunrise[0]} , {sunrise[1]}\nsunset: {sunset[0]} , {sunset[1]}\ncurrent temperature: {data["current"]["temperature_2m"]}\ncurrent wind speed: {data["current"]["wind_speed_10m"]}')
        model2.appendRow(longitude_item)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet('background-color: skyBlue;')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
