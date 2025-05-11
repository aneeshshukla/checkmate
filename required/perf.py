import psutil
import pygetwindow as gw
import win32gui
from datetime import datetime

def get_cpu_usage():
    """Returns the CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    """Returns the RAM usage percentage."""
    return psutil.virtual_memory().percent

def get_gpu_usage():
    """Returns the GPU usage if available."""
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return max(gpu.load * 100 for gpu in gpus)
        else:
            return None
    except ImportError:
        return None

def get_focused_app():
    """Returns the title of the currently focused window."""
    try:
        focused_window = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(focused_window)
        return window_title if window_title else "No focused window"
    except Exception as e:
        return f"Error retrieving focused app: {e}"

def collect_metrics():
    """Collects system metrics and stores them in a dictionary."""
    metrics = {
        #"timestamp": datetime.now().isoformat(),
        "cpu_usage": get_cpu_usage(),
        "ram_usage": get_ram_usage(),
        "gpu_usage": get_gpu_usage(),
        "focused_app": get_focused_app(),#get_focused_app(),
    }
    return metrics

def main():
    print("Monitoring system metrics...\n")
    metrics = collect_metrics()
    print("Collected Data:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
