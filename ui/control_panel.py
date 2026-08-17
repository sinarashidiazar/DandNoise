from PySide6.QtWidgets import *
from PySide6.QtCore import *

class ControlPanel(QWidget):

    params_changed = Signal()

    def __init__(self,filters,simulator):

        super().__init__()

        self.filters=filters
        self.sim=simulator

        layout=QVBoxLayout()

        layout.addWidget(QLabel("Filters"))

        for f in filters:

            cb=QCheckBox(f.name)
            cb.setChecked(True)

            cb.stateChanged.connect(lambda s,filt=f:self.toggle_filter(filt,s))

            layout.addWidget(cb)

        layout.addWidget(QLabel("Noise std"))

        self.noise=QDoubleSpinBox()
        self.noise.setRange(0,5)
        self.noise.setValue(self.sim.noise_std)

        self.noise.valueChanged.connect(self.update_noise)

        layout.addWidget(self.noise)

        layout.addWidget(QLabel("dt"))

        self.dt=QDoubleSpinBox()
        self.dt.setRange(0.01,1)
        self.dt.setValue(self.sim.dt)

        self.dt.valueChanged.connect(self.update_dt)

        layout.addWidget(self.dt)

        self.setLayout(layout)

    def toggle_filter(self,f,state):

        f.enabled=bool(state)

    def update_noise(self,val):

        self.sim.noise_std=val

    def update_dt(self,val):

        self.sim.dt=val
