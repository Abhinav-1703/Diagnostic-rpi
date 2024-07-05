# Raspberry Pi Diagnostic Script

This repository contains a Python script for collecting diagnostic data from a Raspberry Pi. The script gathers information such as temperature, CPU usage, memory usage, disk usage, network statistics, uptime, CPU frequency, GPU temperature, system load, process information, network interface details, and internet connectivity status.

## Features

- **Temperature Monitoring**: Get the CPU and GPU temperature.
- **CPU Usage**: Monitor the CPU usage percentage.
- **Memory Usage**: Check the percentage of memory used.
- **Disk Usage**: Check the percentage of disk space used.
- **Network Statistics**: Gather data on packet loss percentage.
- **Uptime**: Check how long the system has been running.
- **CPU Frequency**: Get the current CPU frequency.
- **System Load**: Load averages over the last 1, 5, and 15 minutes.
- **Process Information**: List of running processes with their CPU and memory usage.
- **Network Interfaces**: Information about all network interfaces.
- **Internet Connectivity**: Ping a website (Google) to check if the internet connection is active.

## Requirements

- Python 3.x
- `psutil` package

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Set up the environment:**

    It is recommended to use a virtual environment to manage dependencies.

    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install psutil
    ```

## Usage

1. **Run the script:**

    ```sh
    python rpi_diagnostics.py
    ```

2. **Sample Output:**

    ```sh
    temperature: (45.0, 'OK')
    cpu_usage: (15.3, 'OK')
    memory_usage: (60.1, 'OK')
    disk_usage: (45.2, 'OK')
    network_stats: {'packet_loss_percent': 0}, Status: OK
    uptime: ('up 1 hour, 23 minutes', 'OK')
    cpu_frequency: (1400.0, 'OK')
    gpu_temperature: (44.0, 'OK')
    system_load: ((0.15, 0.25, 0.35), 'OK')
    process_info: ([{'pid': 1, 'name': 'init', 'cpu_percent': 0.0, 'memory_percent': 0.1}, ...], 'OK')
    network_interfaces: ({'eth0': ['192.168.1.2'], 'lo': ['127.0.0.1']}, 'OK')
    google_ping_status: ('Internet is connected', 'OK')
    ```

## Customization

You can customize the script by adding or modifying the diagnostic functions. The script uses `psutil` for system-related metrics and `subprocess` for running shell commands.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
