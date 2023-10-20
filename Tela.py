from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from ModuloCadastrar import reserva
from ModuloConverterData import converterData

class TelaPrincipal(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()

    def componentes(self):
        self.CbOrig = self.tela.findChild(QtWidgets.QComboBox,"CbOrig")
        self.CbDest = self.tela.findChild(QtWidgets.QComboBox,"CbDest")
        self.caixaData = self.tela.findChild(QtWidgets.QDateEdit,"caixaData")
        self.caixaNome = self.tela.findChild(QtWidgets.QLineEdit,"caixaNome")
        self.CaixaCPF = self.tela.findChild(QtWidgets.QLineEdit,"CaixaCPF")
        self.CbPag = self.tela.findChild(QtWidgets.QComboBox,"CbPag")
        self.BtnCadastrar = self.tela.findChild(QtWidgets.QPushButton,"pushBtnReserva")
        self.BtnCadastrar.clicked.connect(self.reservarViagem)


    def reservarViagem(self):
        nome = self.caixaNome.text()
        cpf = self.CaixaCPF.text()
        local_orig = self.CbOrig.currentText()
        local_dest = self.CbDest.currentText()
        pagamento = self.CbPag.currentText()
        data = self.caixaData.text()
        reserva (nome, cpf, local_orig, local_dest, pagamento, converterData(data))
        

if __name__== "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.show()
    app.exec()
