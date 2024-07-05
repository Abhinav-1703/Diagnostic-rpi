import os
import psutil
import subprocess
import platform
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("system_diagnostics.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger()

def get_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp = float(output.split('=')[1].split("'")[0])
        status = "OK" if temp < 75 else "High"
        return temp, status
    except Exception as e:
        return str(e), "Error"

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=2)
    status = "OK" if usage < 80 else "High"
    return usage, status

def get_memory_usage():
    mem = psutil.virtual_memory()
    status = "OK" if mem.percent < 80 else "High"
    return mem.percent, status

def get_disk_usage():
    disk = psutil.disk_usage('/')
    status = "OK" if disk.percent < 80 else "High"
    return disk.percent, status

def get_network_stats():
    try:
        output = subprocess.check_output(['ping', '-c', '4', 'google.com'], stderr=subprocess.STDOUT, universal_newlines=True)
        packet_loss = re.search(r'(\d+)% packet loss', output).group(1)
        packet_loss = int(packet_loss)
        status = "OK" if packet_loss < 10 else "High"
        return {
            'packet_loss_percent': packet_loss
        }, status
    except subprocess.CalledProcessError as e:
        return str(e), "Error"

def get_uptime():
    try:
        uptime = subprocess.check_output(['uptime', '-p']).decode().strip()
        return uptime, "OK"
    except Exception as e:
        return str(e), "Error"

def get_cpu_frequency():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_clock', 'arm']).decode()
        freq = int(output.split('=')[1]) / 1e6  # Convert to MHz
        return freq, "OK"
    except Exception as e:
        return str(e), "Error"

def get_gpu_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp = float(output.split('=')[1].split("'")[0])
        status = "OK" if temp < 75 else "High"
        return temp, status
    except Exception as e:
        return str(e), "Error"

def get_system_load():
    load = os.getloadavg()
    status = "OK" if load[0] < 1.0 else "High"
    return load, status

def get_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    return processes, "OK"

def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    return {interface: [addr.address for addr in addrs] for interface, addrs in interfaces.items()}, "OK"

def check_internet_connection():
    try:
        if platform.system().lower() == "windows":
            subprocess.check_output(['ping', '-n', '1', 'google.com'], stderr=subprocess.STDOUT, universal_newlines=True)
        else:
            subprocess.check_output(['ping', '-c', '1', 'google.com'], stderr=subprocess.STDOUT, universal_newlines=True)
        return "Internet is connected", "OK"
    except subprocess.CalledProcessError:
        return "Internet is not connected", "Error"

def main():
    diagnostics = {
        'temperature': get_temperature(),
        'cpu_usage': get_cpu_usage(),
        'memory_usage': get_memory_usage(),
        'disk_usage': get_disk_usage(),
        'network_stats': get_network_stats(),
        'uptime': get_uptime(),
        'cpu_frequency': get_cpu_frequency(),
        'gpu_temperature': get_gpu_temperature(),
        'system_load': get_system_load(),
        'network_interfaces': get_network_interfaces(),
        'google_ping_status': check_internet_connection(),
    }

    for key, (value, status) in diagnostics.items():
        logger.info(f"{key}: {value}, Status: {status}")

if __name__ == "__main__":
    main()
