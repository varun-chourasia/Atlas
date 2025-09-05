import psutil
import datetime
import pytz
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import asyncio
from bleak import BleakScanner

class SystemStats:
    def ram_usage(self):
        memory = psutil.virtual_memory()
        used_gb = round(memory.used / (1024**3), 1)
        total_gb = round(memory.total / (1024**3), 1)
        return used_gb, total_gb

    def cpu_usage(self, interval=1):
        cpu_percent = psutil.cpu_percent(interval=interval)
        return cpu_percent

    def disk_usage(self, path="C:\\"):
        disk = psutil.disk_usage(path)
        used_gb = round(disk.used / (1024**3), 2)
        total_gb = round(disk.total / (1024**3), 2)
        return used_gb, total_gb

    def network_usage(self, interval=1):
        counters_start = psutil.net_io_counters()
        bytes_received_start = counters_start.bytes_recv
        bytes_sent_start = counters_start.bytes_sent

        time.sleep(interval)

        counters_end = psutil.net_io_counters()
        bytes_received_end = counters_end.bytes_recv
        bytes_sent_end = counters_end.bytes_sent

        download_speed_mbps = round(((bytes_received_end - bytes_received_start) / (1024 * 1024 * interval)) * 8, 2)
        upload_speed_mbps = round(((bytes_sent_end - bytes_sent_start) / (1024 * 1024 * interval)) * 8, 2)

        return download_speed_mbps, upload_speed_mbps

    def system_volume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = round(volume_interface.GetMasterVolumeLevelScalar() * 100)
        return current_volume

    def battery_level(self):
        battery = psutil.sensors_battery()
        return None if battery is None else battery.percent

    def date_time(self, timezone_name):
        timezone = pytz.timezone(timezone_name)
        current_time = datetime.datetime.now(timezone)
        date_str = current_time.strftime("%Y-%m-%d")
        time_str = current_time.strftime("%H:%M:%S")
        return date_str, time_str

    def date_time_india(self):
        return self.date_time("Asia/Kolkata")

    def date_time_london(self):
        return self.date_time("Europe/London")

