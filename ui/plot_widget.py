import pyqtgraph as pg

class PlotWidget(pg.PlotWidget):

    def __init__(self):

        super().__init__()

        self.max_points = 500   # تعداد نقاط قابل نمایش

        self.raw_curve = self.plot(pen='r', name="raw")
        self.filtered_curve = self.plot(pen='g', name="filtered")

        self.raw_data = []
        self.filtered_data = []

    def update_plot(self, raw, filtered):

        self.raw_data.append(raw)
        self.filtered_data.append(filtered)

        # محدود کردن طول داده
        if len(self.raw_data) > self.max_points:
            self.raw_data = self.raw_data[-self.max_points:]

        if len(self.filtered_data) > self.max_points:
            self.filtered_data = self.filtered_data[-self.max_points:]

        self.raw_curve.setData(self.raw_data)
        self.filtered_curve.setData(self.filtered_data)
