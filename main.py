import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from plugin_loader import load_plugins
from pipeline import Pipeline
from simulator import SensorSimulator

from ui.control_panel import ControlPanel
from ui.plot_widget import PlotWidget


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.sim=SensorSimulator()

        filters=load_plugins()

        self.pipeline=Pipeline(filters)

        layout=QHBoxLayout()

        self.plot=PlotWidget()
        self.panel=ControlPanel(filters,self.sim)

        layout.addWidget(self.plot,3)
        layout.addWidget(self.panel,1)

        self.setLayout(layout)

        self.timer=QTimer()
        self.timer.timeout.connect(self.update_loop)
        self.timer.start(50)

    def update_loop(self):

        true_val,measurement=self.sim.update()

        filtered=self.pipeline.process(measurement)

        self.plot.update_plot(measurement,filtered)


app=QApplication(sys.argv)

w=MainWindow()
w.resize(1000,600)
w.show()

sys.exit(app.exec())
