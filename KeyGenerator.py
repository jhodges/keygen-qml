import sys

from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl, pyqtSignal, QProcess, pyqtSlot
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

"""

bject to generate SSH key pairs by calling ssh-keygen.

class KeyGenerator : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString type READ type WRITE setType NOTIFY typeChanged)
    Q_PROPERTY(QStringList types READ types NOTIFY typesChanged)
    Q_PROPERTY(QString filename READ filename WRITE setFilename NOTIFY filenameChanged)
    Q_PROPERTY(QString passphrase READ filename WRITE setPassphrase NOTIFY passphraseChanged)

public:
    KeyGenerator();
    ~KeyGenerator();

    QString type();
    void setType(const QString &t);

    QStringList types();

    QString filename();
    void setFilename(const QString &f);

    QString passphrase();
    void setPassphrase(const QString &p);

public slots:
    void generateKey();

signals:
    void typeChanged();
    void typesChanged();
    void filenameChanged();
    void passphraseChanged();
    void keyGenerated(bool success);

private:
    QString _type;
    QString _filename;
    QString _passphrase;
    QStringList _types;
};
#endif

"""

class KeyGenerator(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._keytype = "rsa"
        self._filename = ''
        self._passphrase = ''
        self._keytypes = ["dsa", "ecdsa", "rsa", "rsa1"]

        ## SIGNALS
        """
            void typeChanged();
            void typesChanged();
            void filenameChanged();
            void passphraseChanged();
            void keyGenerated(bool success);
        """

    typeChanged = pyqtSignal()
    typesChanged = pyqtSignal()
    filenameChanged = pyqtSignal()
    passphraseChanged = pyqtSignal()
    keyGenerated = pyqtSignal(bool, arguments=['success'])

    # Define the getter of the '' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString',notify=typeChanged)
    def keytype(self):
        return self._keytype

    # Define the setter of the '' property.
    @keytype.setter
    def keytype(self, keytype):
        self._keytype = keytype
        self.typeChanged.emit()

    # Define the getter of the '' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString',notify=filenameChanged)
    def filename(self):
        return self._filename

    # Define the setter of the '' property.
    @filename.setter
    def filename(self, filename):
        self._filename = filename
        self.filenameChanged.emit()

    # Define the getter of the '' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString',notify=passphraseChanged)
    def passphrase(self):
        return self._passphrase

    # Define the setter of the '' property.
    @passphrase.setter
    def passphrase(self, passphrase):
        self._passphrase = passphrase
        self.passphraseChanged.emit()

    # Define the getter of the '' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QStringList',notify=typesChanged)
    def keytypes(self):
        return self._keytypes

    # Define the setter of the '' property.
    @keytypes.setter
    def keytypes(self, keytypes):
        self._keytypes = keytypes
        self.typesChanged.emit()

    @pyqtSlot()
    def generateKey(self):
        qp = QProcess()
        qp.start("ssh-keygen",["-t",self._keytype,"-N",self._passphrase,"-f",self._filename])
        qp.waitForFinished(3000)
        self.keyGenerated.emit((qp.exitCode() == 0))
