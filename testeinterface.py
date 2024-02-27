import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QWidget
import geopandas as gpd
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar e Salvar Shapefile")

        # Botão para selecionar o arquivo shapefile
        self.select_button = QPushButton("Selecionar Shapefile")
        self.select_button.clicked.connect(self.select_shapefile)

        # Tabela para exibir os dados
        self.table_widget = QTableWidget()

        # Botão para salvar as modificações
        self.save_button = QPushButton("Salvar Modificações")
        self.save_button.clicked.connect(self.save_modifications)
        self.save_button.setEnabled(False)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.select_button)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.save_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Variáveis para armazenar os dados do shapefile
        self.gdf = None
        self.gdf_atributos = None

    def select_shapefile(self):
        shp_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Shapefile", "", "Arquivos Shapefile (*.shp)")

        # Extrair apenas as colunas de atributos (excluindo a coluna de geometrias)
        gdf_atributos = gdf.drop(columns='geometry')

        # Inicializar um novo workbook do Excel
        wb = Workbook()
        ws = wb.active

        # Adicionar os dados do GeoDataFrame para o Excel
        for row in dataframe_to_rows(gdf_atributos, index=False, header=True):
            ws.append(row)


        if shp_path:
            self.gdf = gpd.read_file(shp_path)
            self.gdf_atributos = self.gdf.drop(columns='geometry')

            # Preencher a table widget com os dados
            self.fill_table_widget()

            # Habilitar o botão de salvar
            self.save_button.setEnabled(True)

    def fill_table_widget(self):
        if self.gdf_atributos is not None:
            self.table_widget.setColumnCount(len(self.gdf_atributos.columns))
            self.table_widget.setRowCount(len(self.gdf_atributos))
            self.table_widget.setHorizontalHeaderLabels(self.gdf_atributos.columns)

            for i, row in enumerate(self.gdf_atributos.values):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table_widget.setItem(i, j, item)

    def save_modifications(self):
        if self.gdf is not None:
            # Atualizar os dados modificados na table widget
            dados_modificados = []
            for i in range(self.table_widget.rowCount()):
                linha_modificada = []
                for j in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(i, j)
                    if item is not None:
                        linha_modificada.append(item.text())
                    else:
                        linha_modificada.append(None)
                dados_modificados.append(linha_modificada)

            # Criar um DataFrame pandas com os dados modificados
            df_modificado = pd.DataFrame(dados_modificados, columns=self.gdf_atributos.columns)

            # Criar um novo GeoDataFrame combinando os dados modificados com as geometrias originais
            gdf_modificado = self.gdf.copy()
            gdf_modificado[self.gdf_atributos.columns] = df_modificado

            # Salvar o GeoDataFrame modificado de volta para um shapefile
            shp_modificado_path, _ = QFileDialog.getSaveFileName(self, "Salvar Shapefile Modificado", "", "Arquivos Shapefile (*.shp)")
            if shp_modificado_path:
                gdf_modificado.to_file(shp_modificado_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
