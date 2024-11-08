import sys
import time


def basic_progress_bar(total):
    for i in range(total + 1):
        percent = 100 * i / total
        sys.stdout.write(f"\rProgress: [{int(percent)}%]")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

basic_progress_bar(100)
