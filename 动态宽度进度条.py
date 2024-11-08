import sys
import time

def dynamic_width_progress_bar(total, width=50):
    for i in range(total + 1):
        percent = 100 * i / total
        filled_length = int(width * i // total)
        bar = '#' * filled_length + '-' * (width - filled_length)
        sys.stdout.write(f'\rProgress: [{bar}] {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

dynamic_width_progress_bar(100)
