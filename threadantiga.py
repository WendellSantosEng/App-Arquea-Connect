import threading
import time
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog
from geopandas import gpd
from mainwindow import Ui_MainWindow

class ShapefileLoader(QObject):
    progress_updated = Signal(int)
    shapefile_loaded = Signal(gpd.GeoDataFrame)

    def load_shapefile(self, sicar_path):
        try:
            # Lendo o arquivo Shapefile como GeoDataFrame
            sicarmt = gpd.read_file(sicar_path)
            self.shapefile_loaded.emit(sicarmt)

            # Definindo o valor máximo da barra de progresso como o número total de registros no GeoDataFrame
            total_records = len(sicarmt)
            self.progress_updated.emit(total_records)

            # Atualizando a barra de progresso conforme os registros são processados
            for i in range(total_records):
                # Simulando o processamento de cada registro (você pode substituir isso pelo processamento real)
                time.sleep(0.01)
                self.progress_updated.emit(i + 1)

            return sicarmt

        except Exception as e:
            print(f"Erro ao carregar o Shapefile: {e}")

class ClassShape(QObject):

    def __init__(self, ui_main_window):
        super().__init__()
        self.ui_main_window = ui_main_window
        self.loader = ShapefileLoader()
        self.loader.shapefile_loaded.connect(self.handle_shapefile_loaded)

    def abrir_sicarmt(self):
        sicar_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Shapefile", "", "Arquivos Shapefile (*.shp)")

        if sicar_path:
            self.ui_main_window.progressBar_sicar.setValue(0)
            self.ui_main_window.label_aguarde.show()
            self.ui_main_window.progressBar_sicar.show()

            self.loader.progress_updated.connect(self.update_progress)
            threading.Thread(target=self.loader.load_shapefile, args=(sicar_path,)).start()

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
