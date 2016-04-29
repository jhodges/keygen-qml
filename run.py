import sys

from PyQt5.QtCore import QDateTime, QObject, QUrl, pyqtSignal, pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent , qmlRegisterType
from KeyGenerator import KeyGenerator

app = QApplication(sys.argv)

qmlRegisterType(KeyGenerator,'com.ics.demo',1,0,'KeyGenerator')

engine = QQmlApplicationEngine(app)

engine.load(QUrl("keygen.qml"))

app.exec_()
