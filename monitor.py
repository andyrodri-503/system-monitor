import psutil  
import time    
import os      
from datetime import datetime  

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_stats():
    """Continuously display CPU and memory usage with visual bars and timestamp."""
    while True:
        clear_screen()  # clear previous output

        # Get CPU and memory stats
        cpu = psutil.cpu_percent(interval=1)  # CPU usage %
        mem = psutil.virtual_memory()
        total_mem = round(mem.total / (1024**3), 2)  # Convert bytes to GB
        used_mem = round(mem.used / (1024**3), 2)
        mem_percent = mem.percent
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time

        # Create simple visual bars
        cpu_bar = "#" * int(cpu // 5)          # CPU bar max 20 chars
        mem_bar = "#" * int(mem_percent // 5)  # Memory bar max 20 chars

        # Display stats
        print("=" * 40)
        print(f"Time: {now}")
        print(f"CPU Usage:    {cpu}%  [{cpu_bar:<20}]")
        print(f"Memory Usage: {used_mem}/{total_mem} GB ({mem_percent}%)  [{mem_bar:<20}]")
        print("=" * 40)
        print("Press Ctrl + C to stop")

        time.sleep(1)  # wait 1 second before updating

if __name__ == "__main__":
    try:
        display_stats()
    except KeyboardInterrupt:
        print("\nExiting monitor...")  # Exit message
