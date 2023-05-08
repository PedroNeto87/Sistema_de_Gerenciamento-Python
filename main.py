from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from database import DataBase
from xml_files import Read_xml
import sys


class login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_user.text(), self.txt_password.text())

        if autenticado == 'administrador' or autenticado == 'user':
            self.w = MainWindow(autenticado)
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Erro ao acessar')
                msg.setText(f'Login ou senha incorretos \n\nTentativa {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                self.users.close_connection()
                sys.exit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Gerenciamento')

        if user == 'user':
            self.btn_pg_cadastro.setVisible(False)

        #*******************************PAGINAS DO SISTEMA*****************************************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_pg_importar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        #ARQUIVO XML
        self.btn_open_2.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas divergentes')
            msg.setText('As senhas devem ser iguais!')
            msg.exec_()
            return None
        
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Cadastro de Usuário')
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec_()

        self.txt_nome.setText('')
        self.txt_usuario.setText('')
        self.txt_senha.setText('')
        self.txt_senha_2.setText('')

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str("Open Directory"),
                                                                "/home",
                                                                QFileDialog.ShowDirsOnly

                                                                |QFileDialog.DontResolveSymlinks)
        self.txt_file.setText(self.path)

    def import_xml_files(self):
        xml = Read_xml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()

        cont = 1
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1
        
        #ATUALIZAR A TABELA
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("Importação concluída")
        msg.exec_()
        self.progressBar.setValue(0)

        db.close_connection()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()
