import pyvista as pv
from pyvistaqt import QtInteractor
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QApplication, QMainWindow, QPushButton
import PyQt5

from CustomWidgets.CustomWidgets import *
import sys


class PyvistaPyQtWidget(QWidget): # TODO: customize this function
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the QtInteractor object
        self.interactor = QtInteractor(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.interactor)
        self.setLayout(self.layout)

        # Initialize the Pyvista plotter
        self.plotter = self.interactor

        self.plotter.enable_depth_peeling(10)



    def add_mesh(self, mesh, **kwargs):
        self.plotter.add_mesh(mesh, **kwargs)
        self.plotter.reset_camera()
        self.plotter.update()




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()

        vert_layout = QVBoxLayout()

        self.pyvista_widget = PyvistaPyQtWidget(self)

        vert_layout.addWidget(self.pyvista_widget, 1)

        self.createPointButton = QPushButton("Create Point")
        self.createPointButton.clicked.connect(self.openCreatePointWidget)

        self.dickButton = QPushButton("Create Dick")
        self.dickButton.clicked.connect(self.openCreateDick)

        vert_layout.addWidget(self.createPointButton)
        vert_layout.addWidget(self.dickButton)
        vert_layout.addWidget(QPushButton("Create Ass"))





        # Set up the PyvistaPyQtWidget
        # self.pyvista_widget = PyvistaPyQtWidget(self)

        #self.setCentralWidget(self.pyvista_widget)

        # Add example mesh
        sphere = pv.Sphere()
        self.pyvista_widget.add_mesh(sphere, opacity = 0.50 ,color="red")
        self.pyvista_widget.add_mesh(pv.Sphere(2, (1,1,1)), opacity=0.5, color="red")

        self.pyvista_widget.add_mesh(pv.Sphere(2, (3, 1, 1)), opacity=0.50, color="red")
        self.pyvista_widget.add_mesh(pv.Sphere(0.5, (3, -0.7, 1)), opacity=0.5, color="red")

        main_layout.addLayout(vert_layout, 2)

        self.currentEditWidget = QWidget()

        self.newlayout = QVBoxLayout()

        self.inside = PyQt5.QtWidgets.QLabel("Hello")

        self.newlayout.addWidget(self.inside)


        self.currentEditWidget.setLayout(self.newlayout)

        main_layout.addWidget(self.currentEditWidget)

        central_widget.setLayout(main_layout)

    def openCreatePointWidget(self):
        self.createPointWidget = CreatePointWidget()

        self.newlayout.removeWidget(self.inside)
        self.inside.deleteLater()

        self.inside = self.createPointWidget
        self.newlayout.addWidget(self.inside)
        self.newlayout.update()

        self.applyButton = self.findChild(QPushButton, "applyButton")




    def openCreateDick(self):
        self.dick = PyQt5.QtWidgets.QLabel("Dick")

        self.newlayout.removeWidget(self.inside)
        self.inside.deleteLater()

        self.inside = self.dick
        self.newlayout.addWidget(self.inside)
        self.newlayout.update()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())