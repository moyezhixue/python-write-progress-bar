import sys
import time

def colored_progress_bar(total):
    GREEN = '\033[92m'
    RESET = '\033[0m'
    for i in range(total + 1):
        percent = 100 * i / total
        filled_length = int(100 * i // total)
        bar = GREEN + '#' * filled_length + RESET + '-' * (100 - filled_length)
        sys.stdout.write(f'\rProgress: |{bar}| {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

colored_progress_bar(100)
