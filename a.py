# import pandas as pd
# import geopandas as gpd
# from PyQt5.QtWidgets import QTableWidgetItem

# # Supondo que 'sicar' é o seu GeoDataFrame e 'tableWidget_2' é a sua tabela onde os valores são selecionados
# # e 'tableWidget_3' é a tabela onde você deseja exibir as linhas selecionadas.

# # Encontre o índice da coluna "CAR"
# car_column_index = None
# for column in range(tableWidget_2.columnCount()):
#     if tableWidget_2.horizontalHeaderItem(column).text() == "CAR":
#         car_column_index = column
#         break

# # Verifique se a coluna foi encontrada
# if car_column_index is not None:
#     # Obter os valores da coluna "CAR" da tableWidget_2
#     car_values = []
#     for row in range(tableWidget_2.rowCount()):
#         item = tableWidget_2.item(row, car_column_index)
#         if item is not None:
#             car_values.append(item.text())

#     # Selecionar as linhas correspondentes no DataFrame Geopandas 'sicar'
#     selected_rows = pd.DataFrame()
#     for car_value in car_values:
#         selected_rows = pd.concat([selected_rows, sicar[sicar['CAR'] == car_value]])

#     # Limpar e preencher a tableWidget_3 com os resultados
#     tableWidget_3.clear()
#     tableWidget_3.setRowCount(selected_rows.shape[0])
#     tableWidget_3.setColumnCount(selected_rows.shape[1])

#     for i, row in enumerate(selected_rows.iterrows()):
#         for j, value in enumerate(row[1]):
#             item = QTableWidgetItem(str(value))
#             tableWidget_3.setItem(i, j, item)
# else:
#     print("A coluna 'CAR' não foi encontrada na tabela.")
