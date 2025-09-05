from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar
from system_stats import SystemStats

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Dashboard")
        self.setGeometry(200, 200, 500, 400)

        self.cpu_label = QLabel(self)
        self.cpu_label.setGeometry(50, 30, 400, 25)

        self.cpu_bar = QProgressBar(self)
        self.cpu_bar.setGeometry(50, 60, 400, 25)
        self.cpu_bar.setAlignment(Qt.AlignCenter)

        self.ram_label = QLabel(self)
        self.ram_label.setGeometry(50, 100, 400, 25)

        self.disk_label = QLabel(self)
        self.disk_label.setGeometry(50, 140, 400, 25)

        self.network_label = QLabel(self)
        self.network_label.setGeometry(50, 180, 400, 25)

        self.volume_label = QLabel(self)
        self.volume_label.setGeometry(50, 220, 400, 25)

        self.battery_label = QLabel(self)
        self.battery_label.setGeometry(50, 260, 400, 25)

        self.india_time_label = QLabel(self)
        self.india_time_label.setGeometry(50, 300, 200, 25)

        self.london_time_label = QLabel(self)
        self.london_time_label.setGeometry(260, 300, 200, 25)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(2000)

        self.update_stats()

    def update_stats(self):
        cpu_percent = SystemStats.cpu_usage()
        self.cpu_label.setText(f"CPU Usage: {cpu_percent}%")
        self.cpu_bar.setValue(cpu_percent)

        used_gb, total_gb = SystemStats.ram_usage()
        self.ram_label.setText(f"RAM: {used_gb:.1f} GB / {total_gb:.1f} GB")

        used_disk, total_disk = SystemStats.disk_usage()
        self.disk_label.setText(f"Disk (C:): {used_disk:.1f} GB / {total_disk:.1f} GB")

        down, up = SystemStats.network_usage()
        self.network_label.setText(f"Network: ↓ {down:.2f} Mbps | ↑ {up:.2f} Mbps")

        self.volume_label.setText(f"Volume: {SystemStats.system_volume()}%")

        battery = SystemStats.battery_level()
        self.battery_label.setText(f"Battery: {battery}%")

        times = SystemStats.get_location_times()
        self.india_time_label.setText(f"India: {times.india_time} | {times.india_date}")
        self.london_time_label.setText(f"London: {times.london_time} | {times.london_date}")

if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec_()
