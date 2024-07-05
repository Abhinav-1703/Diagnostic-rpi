import os
import psutil
import subprocess
import time

def get_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp = float(output.split('=')[1].split("'")[0])
        return temp
    except Exception as e:
        return str(e)

def get_cpu_usage():
    return psutil.cpu_percent(interval=2)

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

def get_uptime():
    try:
        return subprocess.check_output(['uptime', '-p']).decode().strip()
    except Exception as e:
        return str(e)

def get_cpu_frequency():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_clock', 'arm']).decode()
        freq = int(output.split('=')[1]) / 1e6  # Convert to MHz
        return freq
    except Exception as e:
        return str(e)

def get_gpu_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
        temp = float(output.split('=')[1].split("'")[0])
        return temp
    except Exception as e:
        return str(e)

def get_system_load():
    return os.getloadavg()

def get_process_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    return processes

def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    return {interface: [addr.address for addr in addrs] for interface, addrs in interfaces.items()}

def get_filesystem_usage():
    return {part.mountpoint: psutil.disk_usage(part.mountpoint)._asdict() for part in psutil.disk_partitions()}

def get_swap_usage():
    swap = psutil.swap_memory()
    return swap.percent

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
        'process_info': get_process_info(),
        'network_interfaces': get_network_interfaces(),
        'filesystem_usage': get_filesystem_usage(),
        'swap_usage': get_swap_usage(),
    }

    for key, value in diagnostics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
