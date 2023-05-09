from PySide2 import QtCore
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QTreeWidgetItem)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from database import DataBase
from xml_files import Read_xml
import sys
import sqlite3
import pandas as pd
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date


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
            self.w = MainWindow(self.txt_user.text(), autenticado)
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
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Gerenciamento')
        self.user = username

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

        #FILTRO
        self.txt_filtro.textChanged.connect(self.update_filter)

        #GERAR SAIDA E ESTORNO
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_estorno.clicked.connect(self.gerar_estorno)

        self.reset_tabel()

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

        self.reset_tabel()

        db.close_connection()

    def table_estoque(self):
        self.tw_estoque.setStyleSheet(u" QHeaderView{color:black}; color:#fff; font-size:15px;")
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #Faz o controle para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_estoque.setSortingEnabled(True)

        for i in range(1, 15):
            self.tw_estoque.resizeColumnToContents(i)

    def table_saida(self):
        self.tw_saida.setStyleSheet(u" QHeaderView{color:black}; color:#fff; font-size:15px;")
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT Nfe, serie, data_importacao, data_saida, usuario FROM Notas WHERE data_saida != ''", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #Faz o controle para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_saida.setSortingEnabled(True)

        for i in range(1, 15):
            self.tw_saida.resizeColumnToContents(i)

    def table_geral(self):
        self.tb_geral.setStyleSheet(u" QHeaderView{color:black}; color:#fff; font-size:15px;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()
    
    def reset_tabel(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    def update_filter(self, s):
        s = re.sub("[/W_]+", "", s)
        filter_str = 'Nfe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def gerar_saida(self):
        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))

        recurse(self.tw_estoque.invisibleRootItem())
        
        self.question('saida')

    def gerar_estorno(self):
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))
        
        recurse(self.tw_saida.invisibleRootItem())
        
        self.question('estorno')

    def question(self, table):
        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText('Deseja estornar as notas selecionadas?')
            msgBox.setInformativeText("As notas selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")
        else:
            msgBox.setText('Deseja gerar a saída das notas selecionadas?')
            msgBox.setInformativeText("As notas abaixo serão baixadas do estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")
        
        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_tabel()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_tabel()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()
