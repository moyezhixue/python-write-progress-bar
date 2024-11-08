import time
import sys

def dynamic_progress_bar(total):
    for i in range(total + 1):
        percent = 100 * i / total
        hashes = '#' * int(percent / 5)
        spaces = ' ' * (20 - len(hashes))
        sys.stdout.write(f"\rProgress: [{hashes}{spaces}] {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

dynamic_progress_bar(100)
