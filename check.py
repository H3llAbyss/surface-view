from PyQt5 import QtWidgets, uic
import pyvista as pv
from pyvistaqt import QtInteractor
from PyQt5.QtWidgets import *
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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("untitled.ui", self)
        plotter_widget = self.findChild(QWidget, "PlotterWidgetEmpty")
        self.pyvista_widget = PyvistaPyQtWidget(self)

        self.main_layout = self.findChild(QLayout)

        sphere = pv.Sphere()
        self.pyvista_widget.add_mesh(sphere, opacity=0.50, color="red")
        self.pyvista_widget.add_mesh(pv.Sphere(2, (1, 1, 1)), opacity=0.5, color="red")

        self.pyvista_widget.add_mesh(pv.Sphere(2, (3, 1, 1)), opacity=0.50, color="red")
        self.pyvista_widget.add_mesh(pv.Sphere(0.5, (3, -0.7, 1)), opacity=0.5, color="red")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())