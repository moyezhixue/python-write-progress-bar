import time
import sys

def animated_progress_bar(total):
    animation = "|/-\\"
    idx = 0
    for i in range(total + 1):
        percent = 100 * i / total
        sys.stdout.write(f"\rProgress: [{animation[idx]}] {percent:.2f}%")
        idx = (idx + 1) % len(animation)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

animated_progress_bar(100)
