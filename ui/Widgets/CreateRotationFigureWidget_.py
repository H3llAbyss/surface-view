# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateRotationFigureWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(215, 354)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.create_line_layout = QtWidgets.QHBoxLayout()
        self.create_line_layout.setObjectName("create_line_layout")
        self.verticalLayout_point1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_point1.setObjectName("verticalLayout_point1")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_x_1 = QtWidgets.QLineEdit(Form)
        self.input_x_1.setObjectName("input_x_1")
        self.horizontalLayout.addWidget(self.input_x_1)
        self.verticalLayout_point1.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.input_y_1 = QtWidgets.QLineEdit(Form)
        self.input_y_1.setObjectName("input_y_1")
        self.horizontalLayout_2.addWidget(self.input_y_1)
        self.verticalLayout_point1.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.input_z_1 = QtWidgets.QLineEdit(Form)
        self.input_z_1.setObjectName("input_z_1")
        self.horizontalLayout_3.addWidget(self.input_z_1)
        self.verticalLayout_point1.addLayout(self.horizontalLayout_3)
        self.create_line_layout.addLayout(self.verticalLayout_point1)
        self.verticalLayout_point2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_point2.setObjectName("verticalLayout_point2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.input_x_2 = QtWidgets.QLineEdit(Form)
        self.input_x_2.setObjectName("input_x_2")
        self.horizontalLayout_5.addWidget(self.input_x_2)
        self.verticalLayout_point2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.input_y_2 = QtWidgets.QLineEdit(Form)
        self.input_y_2.setObjectName("input_y_2")
        self.horizontalLayout_6.addWidget(self.input_y_2)
        self.verticalLayout_point2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.input_z_2 = QtWidgets.QLineEdit(Form)
        self.input_z_2.setObjectName("input_z_2")
        self.horizontalLayout_7.addWidget(self.input_z_2)
        self.verticalLayout_point2.addLayout(self.horizontalLayout_7)
        self.create_line_layout.addLayout(self.verticalLayout_point2)
        self.verticalLayout.addLayout(self.create_line_layout)
        self.selectLineBox = QtWidgets.QComboBox(Form)
        self.selectLineBox.setObjectName("selectLineBox")
        self.selectLineBox.addItem("")
        self.verticalLayout.addWidget(self.selectLineBox)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.create_curve_layout = QtWidgets.QHBoxLayout()
        self.create_curve_layout.setObjectName("create_curve_layout")
        self.verticalLayout_point1_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_point1_2.setObjectName("verticalLayout_point1_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.curve_input_x = QtWidgets.QLineEdit(Form)
        self.curve_input_x.setObjectName("curve_input_x")
        self.horizontalLayout_4.addWidget(self.curve_input_x)
        self.verticalLayout_point1_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.curve_input_y = QtWidgets.QLineEdit(Form)
        self.curve_input_y.setObjectName("curve_input_y")
        self.horizontalLayout_8.addWidget(self.curve_input_y)
        self.verticalLayout_point1_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.curve_input_z = QtWidgets.QLineEdit(Form)
        self.curve_input_z.setObjectName("curve_input_z")
        self.horizontalLayout_9.addWidget(self.curve_input_z)
        self.verticalLayout_point1_2.addLayout(self.horizontalLayout_9)
        self.create_curve_layout.addLayout(self.verticalLayout_point1_2)
        self.verticalLayout.addLayout(self.create_curve_layout)
        self.selectCurveBox = QtWidgets.QComboBox(Form)
        self.selectCurveBox.setObjectName("selectCurveBox")
        self.selectCurveBox.addItem("")
        self.verticalLayout.addWidget(self.selectCurveBox)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.applyButton = QtWidgets.QPushButton(Form)
        self.applyButton.setObjectName("applyButton")
        self.verticalLayout.addWidget(self.applyButton)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_10.setText(_translate("Form", "Line:"))
        self.label.setText(_translate("Form", "x:"))
        self.label_2.setText(_translate("Form", "y:"))
        self.label_3.setText(_translate("Form", "z:"))
        self.label_4.setText(_translate("Form", "x:"))
        self.label_5.setText(_translate("Form", "y:"))
        self.label_6.setText(_translate("Form", "z:"))
        self.selectLineBox.setItemText(0, _translate("Form", "No existing lines found"))
        self.label_11.setText(_translate("Form", "Curve:"))
        self.label_7.setText(_translate("Form", "x(t) ="))
        self.label_8.setText(_translate("Form", "y(t) ="))
        self.label_9.setText(_translate("Form", "z(t) ="))
        self.selectCurveBox.setItemText(0, _translate("Form", "No existing curves found"))
        self.applyButton.setText(_translate("Form", "Apply"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
