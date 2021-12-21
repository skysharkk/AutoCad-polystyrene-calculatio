from PyQt5 import QtCore, QtGui, QtWidgets, QtWinExtras
import os


os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"


class Ui_Form(object):
    def setupUi(self, Form):
        myappid = 'mycompany.myproduct.subproduct.version'
        QtWinExtras.QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        Form.setObjectName("Form")
        Form.resize(429, 777)
        Form.setMinimumSize(QtCore.QSize(429, 0))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 412, 822))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.init_data = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.init_data.setCheckable(False)
        self.init_data.setObjectName("init_data")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.init_data)
        self.verticalLayout_6.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.init_data)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.init_data_scale = QtWidgets.QLineEdit(self.init_data)
        self.init_data_scale.setObjectName("init_data_scale")
        self.verticalLayout_6.addWidget(self.init_data_scale)
        self.label = QtWidgets.QLabel(self.init_data)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.init_data_depth = QtWidgets.QLineEdit(self.init_data)
        self.init_data_depth.setObjectName("init_data_depth")
        self.verticalLayout_6.addWidget(self.init_data_depth)
        self.init_data_type = QtWidgets.QGroupBox(self.init_data)
        self.init_data_type.setObjectName("init_data_type")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.init_data_type)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.init_data_type_1 = QtWidgets.QRadioButton(self.init_data_type)
        self.init_data_type_1.setEnabled(True)
        self.init_data_type_1.setChecked(True)
        self.init_data_type_1.setObjectName("init_data_type_1")
        self.verticalLayout_2.addWidget(self.init_data_type_1)
        self.init_data_type_2 = QtWidgets.QRadioButton(self.init_data_type)
        self.init_data_type_2.setObjectName("init_data_type_2")
        self.verticalLayout_2.addWidget(self.init_data_type_2)
        self.verticalLayout_6.addWidget(self.init_data_type)
        self.init_data_table = QtWidgets.QTreeWidget(self.init_data)
        self.init_data_table.setMinimumSize(QtCore.QSize(192, 150))
        self.init_data_table.setObjectName("init_data_table")
        self.verticalLayout_6.addWidget(self.init_data_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.init_data_add = QtWidgets.QPushButton(self.init_data)
        self.init_data_add.setObjectName("init_data_add")
        self.horizontalLayout_2.addWidget(self.init_data_add)
        self.init_data_delete = QtWidgets.QPushButton(self.init_data)
        self.init_data_delete.setObjectName("init_data_delete")
        self.horizontalLayout_2.addWidget(self.init_data_delete)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.acad_select_positions = QtWidgets.QPushButton(self.init_data)
        self.acad_select_positions.setEnabled(True)
        self.acad_select_positions.setObjectName("acad_select_positions")
        self.verticalLayout_6.addWidget(self.acad_select_positions)
        self.gridLayout_2.addWidget(self.init_data, 0, 0, 1, 1)
        self.results = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.results.setObjectName("results")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.results)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.res_table = QtWidgets.QTableWidget(self.results)
        self.res_table.setMinimumSize(QtCore.QSize(0, 150))
        self.res_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.res_table.setObjectName("res_table")
        self.res_table.setColumnCount(8)
        self.res_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.res_table.setHorizontalHeaderItem(7, item)
        self.res_table.horizontalHeader().setMinimumSectionSize(50)
        self.res_table.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.res_table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.clear_all_data = QtWidgets.QPushButton(self.results)
        self.clear_all_data.setObjectName("clear_all_data")
        self.verticalLayout_4.addWidget(self.clear_all_data)
        self.res_delete_position = QtWidgets.QPushButton(self.results)
        self.res_delete_position.setObjectName("res_delete_position")
        self.gridLayout.addWidget(self.res_delete_position, 0, 0, 1, 1)
        self.res_export_table_to_acad = QtWidgets.QPushButton(self.results)
        self.res_export_table_to_acad.setObjectName("res_export_table_to_acad")
        self.gridLayout.addWidget(self.res_export_table_to_acad, 0, 1, 1, 1)
        self.res_draw_pos = QtWidgets.QPushButton(self.results)
        self.res_draw_pos.setObjectName("res_draw_pos")
        self.gridLayout.addWidget(self.res_draw_pos, 1, 1, 1, 1)
        self.res_export_table_to_excel = QtWidgets.QPushButton(self.results)
        self.res_export_table_to_excel.setObjectName(
            "res_export_table_to_excel")
        self.gridLayout.addWidget(self.res_export_table_to_excel, 1, 0, 1, 1)
        self.res_import_data_from_excel = QtWidgets.QPushButton(self.results)
        self.res_import_data_from_excel.setObjectName(
            "res_import_data_from_excel")
        self.gridLayout.addWidget(self.res_import_data_from_excel, 2, 1, 1, 1)
        self.res_excel_template = QtWidgets.QPushButton(self.results)
        self.res_excel_template.setObjectName("res_excel_template")
        self.gridLayout.addWidget(self.res_excel_template, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.results, 1, 0, 1, 1)
        self.waste = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.waste.setObjectName("waste")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.waste)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calc_waste = QtWidgets.QPushButton(self.waste)
        self.calc_waste.setObjectName("calc_waste")
        self.verticalLayout.addWidget(self.calc_waste)
        self.draw_bin = QtWidgets.QPushButton(self.waste)
        self.draw_bin.setObjectName("draw_bin")
        self.verticalLayout.addWidget(self.draw_bin)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout_2.addWidget(self.waste, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon("./assets/logo.png"))
        Form.setWindowTitle(_translate("Form", "Расскладка утеплителя"))
        self.init_data.setTitle(_translate("Form", "Исходные данные"))
        self.label_2.setText(_translate("Form", "Масштаб"))
        self.label.setText(_translate("Form", "Толщина ППТ"))
        self.init_data_type.setTitle(_translate("Form", "Тип"))
        self.init_data_type_1.setText(_translate("Form", "ППТ-15-А-Р"))
        self.init_data_type_2.setText(_translate(
            "Form", "Эффективный утеплитель λ ≤ 0,034 Вт/(м·°C)"))
        self.init_data_table.headerItem().setText(0, _translate("Form", "Толщина"))
        self.init_data_table.headerItem().setText(1, _translate("Form", "Тип"))
        self.init_data_add.setText(_translate("Form", "Добавить"))
        self.init_data_delete.setText(_translate("Form", "Удалить"))
        self.acad_select_positions.setText(
            _translate("Form", "Выбрать позиции ППТ"))
        self.results.setTitle(_translate("Form", "Результат"))
        item = self.res_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Поз."))
        item = self.res_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Обозначение"))
        item = self.res_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Длина, мм"))
        item = self.res_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Высота, мм"))
        item = self.res_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Ширина, мм"))
        item = self.res_table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Кол., шт."))
        item = self.res_table.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Объем, м3"))
        item = self.res_table.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Примечания"))
        self.clear_all_data.setText(_translate("Form", "Очистить данные"))
        self.res_delete_position.setText(_translate("Form", "Удалить позицию"))
        self.res_export_table_to_acad.setText(
            _translate("Form", "Экспорт таблицы в AutoCAD"))
        self.res_draw_pos.setText(_translate(
            "Form", "Отрисовать пакеты в AutoCAD"))
        self.res_export_table_to_excel.setText(
            _translate("Form", "Экспорт таблицы в Excel"))
        self.res_import_data_from_excel.setText(
            _translate("Form", "Импорт. таблицу из Excel"))
        self.res_excel_template.setText(
            _translate("Form", "Пример таблицы Excel"))
        self.waste.setTitle(_translate("Form", "Отходы"))
        self.calc_waste.setText(_translate(
            "Form", "Рассчитать и вывести на лист"))
        self.draw_bin.setText(_translate("Form", "Отрисовать раскрой"))
