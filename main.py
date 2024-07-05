import os
import psutil
import subprocess

def get_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp = float(output.split('=')[1].split("'")[0])
        return temp
    except Exception as e:
        return str(e)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_network_stats():
    net = psutil.net_io_counters()
    return {
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv,
        'packets_sent': net.packets_sent,
        'packets_recv': net.packets_recv,
    }

def main():
    diagnostics = {
        'temperature': get_temperature(),
        'cpu_usage': get_cpu_usage(),
        'memory_usage': get_memory_usage(),
        'disk_usage': get_disk_usage(),
        'network_stats': get_network_stats(),
    }
    
    for key, value in diagnostics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
