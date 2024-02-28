"""

!!! APLICAÇÃO EM DESENVOLVIMENTO !!!

Autor: Wendell Resende dos Santos
Data de Criação: Em desenvolvimento

Descrição:
Esta aplicação é extremamente exponenciável, e no memomento o intuito principal
é integração de serviços de geoprocessamento da empresa Arquea Engenharia e Geotecnologia, com Python

Uso:
Uso exclusivo da equipe Arquea, porém no futuro se expanda

"""


import sys
import io
from typing import cast
import threading
import time
import datetime

from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve, QObject, Signal, QThread, Qt, QDate
from PySide6.QtGui import QKeyEvent, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog)
from PySide6.QtWebEngineWidgets import QWebEngineView
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, GeometryCollection
from shapely.wkt import loads
import shapely
from codsup import codigo_supressao
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from mainwindow import Ui_MainWindow

class ShapefileLoader(QObject):
    progress_updated = Signal(int)
    shapefile_loaded = Signal(gpd.GeoDataFrame)

    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def load_shapefile(self, sicar_path, column_names):
        try:
            # Lendo o arquivo Shapefile como GeoDataFrame
            sicarmt = gpd.read_file(sicar_path)
            
            # Definindo os nomes das colunas
            sicarmt.columns = column_names

            # Verificar os nomes das colunas antes e depois da atribuição
            print("Nomes das colunas antes da atribuição:", sicarmt.columns)
            
            self.shapefile_loaded.emit(sicarmt)

            # Verificar algumas informações sobre o GeoDataFrame após a atribuição
            print("Informações sobre o GeoDataFrame após a atribuição:")
            print(sicarmt.head())
            print(sicarmt.info())

            # Definindo o valor máximo da barra de progresso como o número total de registros no GeoDataFrame
            total_records = len(sicarmt)
            self.progress_updated.emit(total_records)

            # Atualizando a barra de progresso conforme os registros são processados
            for i in range(total_records):
                # Simulando o processamento de cada registro (você pode substituir isso pelo processamento real)
                time.sleep(0.01)
                self.progress_updated.emit(i + 1)

                # Verificando se a thread deve ser encerrada
                if self._stop_event.is_set():
                    break

                # Processa os eventos do aplicativo regularmente para garantir que a interface do usuário não congele
                QCoreApplication.processEvents()

            return sicarmt

        except Exception as e:
            print(f"Erro ao carregar o Shapefile: {e}")

    def stop_loading(self):
        # Define o evento de parada para interromper o processamento
        self._stop_event.set()

class ClassShape(QObject):

    def __init__(self, ui_main_window):
        super().__init__()
        self.ui_main_window = ui_main_window

    def start_load_shapefile(self, loader, sicar_path, column_names):
        loader.load_shapefile(sicar_path, column_names)

    def update_progress(self, value):
        self.ui_main_window.progressBar_sicar.setValue(value)
        if value == self.ui_main_window.progressBar_sicar.maximum():
            self.ui_main_window.label_aguarde.hide()

    def handle_shapefile_loaded(self, sicarmt):
        print("carregou")
        # Verificando se o GeoDataFrame foi carregado corretamente
        if not sicarmt.empty:
            print("O GeoDataFrame não está vazio.")
        else:
            print("O GeoDataFrame está vazio.")

        # Exibindo algumas informações sobre o GeoDataFrame
        print("Informações sobre o GeoDataFrame:")
        print(sicarmt.head())
        print(sicarmt.info())

        # Este método é chamado quando o shapefile foi carregado
        # Você pode fazer qualquer coisa que precise com o sicarmt aqui
        # Por exemplo, você pode atribuí-lo a uma variável de instância para acessá-lo posteriormente
        self.ui_main_window.sicarmt = sicarmt
        print("ta carregado")
        self.ui_main_window.btn_selectCAR.setEnabled(True)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ArqueaConnect")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        # Criar um novo ShapefileLoader
        self.loader = ShapefileLoader()
        self.loader.progress_updated.connect(self.update_progress)
        self.loader.shapefile_loaded.connect(self.handle_shapefile_loaded)

        # Botao do menu lateral
        self.pushButton.clicked.connect(self.leftMenu)

        # Paginas do sistema
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_codsup))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_shape))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_sobre))

        # Variáveis para armazenar os dados do shapefile
        self.gdf = None
        self.gdf_atributos = None
        # self.sicarmt = None

        # Botao para abrir arquivos Excel
        self.btn_import.clicked.connect(lambda: self.abrir_arquivos("", self.tableWidget))

        # Botao para abrir arquivos Shapefile
        self.btn_importshp.clicked.connect(self.abrir_shp)

        # Botão para fazer modificações
        self.btn_gerar.clicked.connect(self.gerar_codigo_sup)

        # Botão para salvar modificações
        self.btn_saved.clicked.connect(self.salvar_modificacoes)

        # Botão para salvar Shapefile
        self.btn_savedshp.clicked.connect(lambda: self.exportar_shp_da_tabela(self.tableWidget, "SUP"))

        # Botao para abrir Planilha de Dados        
        self.btn_planilha_dados.clicked.connect(lambda: self.abrir_arquivos("DATA", self.tableWidget_2))

        # Botão para entrar no filtro
        self.btn_filtrar.clicked.connect(self.show_filter_menu)
        self.frame_filter.hide()
        self.filtered_rows = []

        # Botão pra aparecer a tabela de acordo com o filtro
        self.column_index = -1
        self.select_column.currentIndexChanged.connect(self.column_selected)

        # Conecte a função intermediária ao sinal clicked do botão
        self.btn_okfilter.clicked.connect(self.filtred)

        # Importando SICAR-MT
        self.btn_sicar.clicked.connect(self.abrir_sicarmt)

        # Desabilitar o botão btn_selectCAR inicialmente
        self.btn_selectCAR.setEnabled(False)

        # Selecionando as linhas de dentro do SicarMT de acordo com o que é visivel na tabela de Dados principal
        self.btn_selectCAR.clicked.connect(self.seletionCARs)
        self.label_aguarde.hide()
        self.progressBar_sicar.hide()
        self.progressBar_sicar.setRange(0, 100)
        self.column_names = []

        # Exportando como Shp a tabela do SicarMT
        self.gdfSICAR = None
        self.gdf_atributosSICAR = None
        self.btn_exportCAR.clicked.connect(lambda: self.exportar_shp_da_tabela(self.tableWidget_3, "CAR"))

        # Importando dados da tabela filtrada para o shape safra
        self.importDataSafra.clicked.connect(self.transfer_data_for_safra)
        self.exportSHPSafra.clicked.connect(lambda: self.exportar_shp_da_tabela(self.tableWidget_4, "SAFRA"))

        # Informações da usina
        self.usina_info.hide()
        self.usina_name.hide()

    def gerar_codigo_sup(self):
        # Obter os dados da tabela widget
        dados = []
        cabecalhos = []

        for column in range(self.tableWidget.columnCount()):
            cabecalhos.append(self.tableWidget.horizontalHeaderItem(column).text())

        for row in range(self.tableWidget.rowCount()):  # Começar da primeira linha
            linha = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    linha.append(item.text())
                else:
                    linha.append("")
            dados.append(linha)

        # Criar um DataFrame do pandas com os dados da tabela e os cabeçalhos
        df = pd.DataFrame(dados, columns=cabecalhos)

        list_geometry = df['geometry'].tolist()

        df.drop(columns=['geometry'], inplace=True)

        # Chamar a função para modificar os dados
        workbook_modificado = codigo_supressao(df)
        ws = workbook_modificado.active

        # Verificar se a coluna 'geometry' já existe
        if 'geometry' not in df.columns:
            last_column_index = len(df.columns) + 1
            ws.insert_cols(idx=last_column_index)

            # Adicionar os dados da lista à coluna "geometry"
            for idx, item in enumerate(list_geometry, start=2):
                ws.cell(row=idx, column=last_column_index, value=item)

            # Renomear a coluna para 'geometry'
            ws.cell(row=1, column=last_column_index, value='geometry')
        else:
            print("A coluna 'geometry' já existe.")

        # Atualizar a QTableWidget com os dados do workbook
        self.mostrar_dados(workbook_modificado, self.tableWidget)

    # Menu da esquerda
    def leftMenu(self):
        width = self.left_container.width()
        print(width)

        if width == 9:
            newWidth = 150
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
    def abrir_arquivos(self, value, tablewidget):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Arquivos Excel (*.xlsx *.xls)", options=options)
        if fileName:
            workbook = load_workbook(fileName)
            # Renomear a aba para "Codigos Car" se ela existir
            if "Codigos Car" in workbook.sheetnames:
                worksheet = workbook["Codigos Car"]
                worksheet.title = "Codigos Car"  # Renomear a aba
            else:
                # Se a aba não existir, você pode criar uma nova aba com esse nome ou tratar de outra maneira
                pass
        if value == "DATA":
            # Transformar a coluna "DATA" em uma string com dia;mes;ano
            self.transformar_coluna_data_str(workbook)

        # Mostrar dados na tabela
        self.mostrar_dados(workbook, tablewidget)

    def parse_coordinates(self, coord_str):
        coords = []
        # Dividir a string em substrings individuais com base na vírgula
        for coord_pair in coord_str.split(','):
            # Verificar se a substring não contém a palavra 'POLYGON'
            if 'POLYGON' not in coord_pair:
                # Remover os parênteses extras e converter a substring em um par de coordenadas
                coord_pair = coord_pair.strip().strip(')').strip('(')
                coords.append(tuple(map(float, coord_pair.split())))
        return coords
    
    def transformar_coluna_data_str(self, workbook):
        worksheet = workbook.active
        data_column_index = None
        for col_idx, col in enumerate(worksheet.iter_cols(values_only=True)):
            if col[0] == "DATA":
                data_column_index = col_idx
                break
        if data_column_index is not None:
            for i, cell in enumerate(worksheet.iter_rows(values_only=True, min_row=2)):
                if isinstance(cell[data_column_index], datetime.datetime):
                    # Converte a data para o formato desejado dia;mes;ano
                    data_str = cell[data_column_index].strftime("%d/%m/%Y")
                    # Atualiza o valor na célula
                    worksheet.cell(row=i + 2, column=data_column_index + 1, value=data_str)
        else:
            print("A coluna 'DATA' não foi encontrada.")

    def abrir_shp(self):
        shp_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Shapefile", "", "Arquivos Shapefile (*.shp)")

        if shp_path:
            # Lendo o arquivo Shapefile como GeoDataFrame
            gdf = gpd.read_file(shp_path)

            # Convertendo as geometrias para strings
            gdf['geometry'] = gdf['geometry'].apply(lambda geom: str(geom))

            # Inicializar um novo workbook do Excel
            wb = Workbook()
            ws = wb.active

            # Adicionar os dados do GeoDataFrame ao workbook do Excel
            for row in dataframe_to_rows(gdf, index=False, header=True):
                ws.append(row)

            # Exibir os dados na tabelaWidget
            self.mostrar_dados(wb, self.tableWidget)

    # Método para mostrar dados na tabela widget e atualizar a planilha
    def mostrar_dados(self, workbook, tablewidget):
        # Atualizar a QTableWidget com os dados do workbook
        worksheet = workbook.active
        dados = []
        for linha in worksheet.iter_rows(values_only=True, min_row=2):
            if not all(cell is None for cell in linha):
                dados.append(linha)

        df = pd.DataFrame(dados, columns=[coluna[0].value for coluna in worksheet.iter_cols()])
        
        tablewidget.setRowCount(df.shape[0])
        tablewidget.setColumnCount(df.shape[1])
        tablewidget.setHorizontalHeaderLabels(df.columns)
        
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                if df.columns[j] == "DATA":  # Verifica se a coluna é "DATA"
                    # Se for, converte o valor para string
                    tablewidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
                else:
                    # Caso contrário, insere o valor normalmente
                    tablewidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    # Método para salvar as modificações na planilha original
    def salvar_modificacoes(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar Tabela como Excel", "", "Arquivo Excel (*.xlsx)")

        if fileName:
            # Criar um DataFrame a partir dos dados da tableWidget
            dados = []
            cabecalhos = []
            for column in range(self.tableWidget.columnCount()):
                cabecalhos.append(self.tableWidget.horizontalHeaderItem(column).text())

            for row in range(self.tableWidget.rowCount()):
                linha = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:
                        linha.append(item.text())
                    else:
                        linha.append("")
                dados.append(linha)

            df = pd.DataFrame(dados, columns=cabecalhos)

            # Salvar o DataFrame como um arquivo Excel
            df.to_excel(fileName, index=False)

    def show_filter_menu(self):
        # Verifica se há uma tabela no tableWidget_2
        if self.tableWidget_2.rowCount() > 0 and self.tableWidget_2.columnCount() > 0:
            # Limpa as opções anteriores do combobox
            self.select_column.clear()
            # Preenche as opções do combobox com os nomes das colunas da tabela
            for col in range(self.tableWidget_2.columnCount()):
                column_name = self.tableWidget_2.horizontalHeaderItem(col).text()
                if column_name == "Qual o código de identificação do Grupo?":
                    column_name = "ID"
                self.select_column.addItem(column_name)
            # Exibe o frame do filtro
            self.frame_filter.show()
        else:
            # Se não houver tabela, oculta o frame do filtro
            self.frame_filter.hide()

    def column_selected(self):
        # Atualiza column_index quando uma coluna é selecionada no combobox
        self.column_index = self.select_column.currentIndex()

    def filtred(self):
        self.filtered_rows.clear()
        # Limpa o filtro anterior antes de aplicar o novo filtro
        self.clear_filter()

        # Obtém o texto de filtro do lineedit
        filter_text = self.search_filter.text().lower()
        print(filter_text, " em ", self.column_index)
        
        # Lista para armazenar as linhas filtradas
        filtered = []

        # Verifica se um índice de coluna válido foi selecionado
        if self.column_index >= 0:
            # Itera sobre as linhas da tabela
            for row in range(self.tableWidget_2.rowCount()):
                # Obtém o item da célula na coluna selecionada e linha atual
                item = self.tableWidget_2.item(row, self.column_index)
                if item:
                    # Verifica se o texto de filtro está presente no texto do item (ignorando maiúsculas/minúsculas)
                    if filter_text in item.text().lower():
                        # Adiciona o número da linha à lista de linhas filtradas
                        filtered.append(row)
                        # Exibe a linha se o texto de filtro estiver presente
                        self.tableWidget_2.setRowHidden(row, False)
                    else:
                        # Oculta a linha se o texto de filtro não estiver presente
                        self.tableWidget_2.setRowHidden(row, True)
            for item in filtered:
                self.filtered_rows.append(item)

            else:
                # Se não houver linhas filtradas, oculta o label
                self.usina_name.hide()

        else:
            # Se nenhum índice de coluna válido foi selecionado, exibe todas as linhas da tabela
            for row in range(self.tableWidget_2.rowCount()):
                # Adiciona o número da linha à lista de linhas filtradas
                filtered.append(row)
                self.tableWidget_2.setRowHidden(row, False)

    def clear_filter(self):
        # Exibe todas as linhas da tabela antes de aplicar um novo filtro
        for row in range(self.tableWidget_2.rowCount()):
            self.tableWidget_2.setRowHidden(row, False)

    def abrir_sicarmt(self):
        sicar_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Shapefile", "", "Arquivos Shapefile (*.shp)")

        if sicar_path:
            print("CARREGOU")
            self.progressBar_sicar.setValue(0)
            self.label_aguarde.show()
            self.progressBar_sicar.show()

            # Obter os nomes das colunas da tabela
            self.column_names = [self.tableWidget_3.horizontalHeaderItem(column).text() for column in range(self.tableWidget_3.columnCount())]

            # Conectar os sinais e slots do loader
            self.loader.progress_updated.connect(self.update_progress)
            self.loader.shapefile_loaded.connect(self.handle_shapefile_loaded)

            # Iniciar a carga do shapefile na thread
            self.loader.load_shapefile(sicar_path, self.column_names)
        
    def update_progress(self, value):
        self.progressBar_sicar.setValue(value)
        if value == self.progressBar_sicar.maximum():
            self.label_aguarde.hide()

    def handle_shapefile_loaded(self, sicarmt):
        # Verificando se o GeoDataFrame foi carregado corretamente
        if not sicarmt.empty:
            print("O GeoDataFrame não está vazio.")
        else:
            print("O GeoDataFrame está vazio.")

        # Exibindo algumas informações sobre o GeoDataFrame
        print("Informações sobre o GeoDataFrame:")
        print(sicarmt.head())
        print(sicarmt.info())
        
        # Este método é chamado quando o shapefile foi carregado
        # Você pode fazer qualquer coisa que precise com o sicarmt aqui
        # Por exemplo, você pode atribuí-lo a uma variável de instância para acessá-lo posteriormente
        self.sicarmt = sicarmt
        self.btn_selectCAR.setEnabled(True)

    def seletionCARs(self):
        CAR = "Informe os códigos de CARs do Grupo"
        # Verificar se self.sicarmt está definido antes de usá-lo
        if hasattr(self, 'sicarmt'):
            car_column_index = None
            for column in range(self.tableWidget_2.columnCount()):
                if self.tableWidget_2.horizontalHeaderItem(column).text() == CAR:
                    car_column_index = column
                    break

            if car_column_index is not None:
                car_values = []
                # Iterar apenas sobre as linhas filtradas
                for row in self.filtered_rows:
                    print(row)
                    item = self.tableWidget_2.item(row, car_column_index)
                    if item is not None:
                        car_values.append(item.text())

                # Verificar se car_values não está vazio
                if car_values:
                    # Selecionar as linhas correspondentes no DataFrame Geopandas 'sicarmt'
                    selected_rows = pd.DataFrame()
                    print("car_values:", car_values)

                    # Converter car_values para o mesmo tipo de dados da coluna 'CAR' em sicarmt
                    car_values_set = set(car_values)
                    car_values_filtered = [value for value in self.sicarmt['cod_imovel'].unique() if value in car_values_set]

                    for car_value in car_values_filtered:
                        selected_rows = pd.concat([selected_rows, self.sicarmt[self.sicarmt['cod_imovel'] == car_value]])

                    print("selected_rows:", selected_rows)

                    # Limpar e preencher a tableWidget_3 com os resultados
                    self.tableWidget_3.clear()
                    self.tableWidget_3.setRowCount(selected_rows.shape[0])
                    self.tableWidget_3.setColumnCount(selected_rows.shape[1])

                    # Atribuir os nomes de coluna originais após a seleção
                    self.tableWidget_3.setHorizontalHeaderLabels(self.column_names)

                    for i, row in enumerate(selected_rows.iterrows()):
                        for j, value in enumerate(row[1]):
                            item = QTableWidgetItem(str(value))
                            self.tableWidget_3.setItem(i, j, item)
                else:
                    print("Nenhum valor de CAR encontrado na tabela.")
            else:
                print("A coluna 'CAR' não foi encontrada na tabela.")
        else:
            print("O shapefile ainda não foi carregado completamente.")
    
    def extrair_dados_da_tabela(self, tablewidget):
        data = []
        header_items = [tablewidget.horizontalHeaderItem(column).text() for column in range(tablewidget.columnCount())]
        
        for row in range(tablewidget.rowCount()):
            row_data = []
            for column in range(tablewidget.columnCount()):
                cell_item = tablewidget.item(row, column)
                if cell_item is not None:
                    row_data.append(cell_item.text())
                else:
                    row_data.append("")  
            data.append(row_data)
            
        return data, header_items

    def exportar_shp_da_tabela(self, tablewidget, value):
        if value == "CAR":
            data, header_items = self.extrair_dados_da_tabela(tablewidget)
            shp_path, _ = QFileDialog.getSaveFileName(None, "Salvar Shapefile", "", "Arquivos Shapefile (*.shp)")
            if shp_path:
                df = pd.DataFrame(data, columns=header_items)

                if 'polygon' in df.columns:
                    print("TEM POLYGON")
                    try:
                        print("try entrou")
                        print(df)

                        df['geometry'] = df['polygon'].apply(lambda coords: shapely.geometry.Polygon(self.parse_coordinates(coords)) if isinstance(coords, str) else None)

                        # Remover linhas com geometria inválida
                        df = df.dropna(subset=['geometry'])

                        # Remover a coluna "polygon" agora que a coluna de geometria está presente
                        df.drop(columns=['polygon'], inplace=True)

                        # Criar um GeoDataFrame a partir do DataFrame 'df'
                        gdf = gpd.GeoDataFrame(df)
                    except NameError:
                        print("Erro ao criar geometria. Verifique se o pacote shapely está corretamente importado.")
                        return
                else:
                    return
                    
                gdf.to_file(shp_path, driver='ESRI Shapefile')
        elif value == "SAFRA":
            data, header_items = self.extrair_dados_da_tabela(tablewidget)
            data = [row for row in data if all(item is not None for item in row)]  # Remover linhas com células vazias
            shp_path, _ = QFileDialog.getSaveFileName(self, "Salvar Shapefile", "", "Arquivos Shapefile (*.shp)")
            if shp_path:
                df = pd.DataFrame(data, columns=header_items)
                df['geometry'] = None
                gdf = gpd.GeoDataFrame(df, geometry=[shapely.geometry.Polygon() for _ in range(len(df))])
                gdf.to_file(shp_path, driver='ESRI Shapefile')

        elif value == "SUP":
            data, header_items = self.extrair_dados_da_tabela(tablewidget)
            shp_path, _ = QFileDialog.getSaveFileName(None, "Salvar Shapefile", "", "Arquivos Shapefile (*.shp)")
            if shp_path:
                df = pd.DataFrame(data, columns=header_items)

                df.rename(columns={'geometry': 'polygon'}, inplace=True)

                if 'polygon' in df.columns:
                    print("TEM POLYGON")
                    try:
                        print("try entrou")
                        print(df)

                        df['geometry'] = df['polygon'].apply(lambda coords: shapely.geometry.Polygon(self.parse_coordinates(coords)) if isinstance(coords, str) else None)

                        # Remover linhas com geometria inválida
                        df = df.dropna(subset=['geometry'])

                        # Remover a coluna "polygon" agora que a coluna de geometria está presente
                        df.drop(columns=['polygon'], inplace=True)

                        # Criar um GeoDataFrame a partir do DataFrame 'df'
                        gdf = gpd.GeoDataFrame(df)
                    except NameError:
                        print("Erro ao criar geometria. Verifique se o pacote shapely está corretamente importado.")
                        return
                else:
                    return
                    
                gdf.to_file(shp_path, driver='ESRI Shapefile')

        else:
            print("Valor não reconhecido para exportação.")

    def transfer_data_for_safra(self):
        # Mapeando as colunas a serem copiadas de tableWidget_2 para tableWidget_4
        columns_mapping = {
            "O Grupo pertence a qual usina?": 1,
            "Qual o código de identificação do Grupo?": 0,
            "Qual o nome do Grupo a ser informado?": 2,
            "Qual o CPF/CNPJ do Grupo": 3,
            "Qual o ano da safra analisada?": 4,
            "Informe os códigos de CARs do Grupo": 6,
            "DATA": 9,
        }

        headers = []
        for i in range(self.tableWidget_4.columnCount()):
            header_item = self.tableWidget_4.horizontalHeaderItem(i)
            if header_item:
                headers.append(header_item.text())
            else:
                headers.append("")  # Adiciona uma string vazia se não houver um item de cabeçalho

        # Limpando tableWidget_4 antes de copiar
        self.tableWidget_4.clear()

        self.tableWidget_4.setColumnCount(len(headers))
        self.tableWidget_4.setHorizontalHeaderLabels(headers)

        # Transferir apenas os itens visíveis da tableWidget_2 para tableWidget_4
        row_position = 0  # Posição da linha na tableWidget_4
        for i in self.filtered_rows:
            for source_col_name, target_col_index in columns_mapping.items():
                try:
                    # Obter o índice da coluna em tableWidget_2
                    source_col_index = [self.tableWidget_2.horizontalHeaderItem(j).text() for j in range(self.tableWidget_2.columnCount())].index(source_col_name)
                    # Obter o item da célula em tableWidget_2
                    item = self.tableWidget_2.item(i, source_col_index)
                    if item:
                        # Se a linha correspondente não existir em tableWidget_4, crie-a
                        if row_position >= self.tableWidget_4.rowCount():
                            self.tableWidget_4.insertRow(row_position)
                        # Definir o item na célula correspondente em tableWidget_4
                        self.tableWidget_4.setItem(row_position, target_col_index, QTableWidgetItem(item.text()))

                         # Verificar se o nome da coluna é "DATA" e imprimir seu valor
                        if source_col_name == "DATA":
                            # Obter a data como uma string no formato "y/m/d"
                            data_y_m_d = datetime.datetime.strptime(item.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
                            # Substituir o valor original do item pela nova data formatada
                            self.tableWidget_4.setItem(row_position, target_col_index, QTableWidgetItem(data_y_m_d))
                        else:
                            # Manter o valor original do item para outras colunas
                            self.tableWidget_4.setItem(row_position, target_col_index, QTableWidgetItem(item.text()))
                    
                except ValueError as e:
                    print(f"Erro: {e}")
            row_position += 1  # Incrementar a posição da linha na tableWidget_4
        
        column_index = 1  # Índice da coluna de interesse
        if self.tableWidget_4.rowCount() > 0:
            name_usina = self.tableWidget_4.item(0, column_index).text()
            self.usina_name.setText(name_usina)

        self.usina_info.show()
        self.usina_name.show()

    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

