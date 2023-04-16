import pyvista as pv
from pyvistaqt import QtInteractor
from PyQt5.QtWidgets import QVBoxLayout, QWidget

class PyvistaPyQtWidget(QWidget):
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


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyvista as pv

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the PyvistaPyQtWidget
        self.pyvista_widget = PyvistaPyQtWidget(self)
        self.setCentralWidget(self.pyvista_widget)

        # Add example mesh
        sphere = pv.Sphere()
        self.pyvista_widget.add_mesh(sphere, opacity = 0.50 ,color="red")

        self.pyvista_widget.add_mesh(pv.Sphere(0.5, (1,1,1)), opacity=0.5, color="green")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())