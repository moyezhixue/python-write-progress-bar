import time
import sys

def filled_progress_bar(total):
    for i in range(total + 1):
        percent = 100 * i / total
        filled_length = int(100 * i // total)
        bar = '█' * filled_length + '-' * (100 - filled_length)
        sys.stdout.write(f"\rProgress: |{bar}| {percent:.2f}% Complete")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

filled_progress_bar(100)
