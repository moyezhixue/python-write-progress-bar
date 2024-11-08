import sys
import time

def custom_char_progress_bar(total, char='*'):
    for i in range(total + 1):
        percent = 100 * i / total
        filled_length = int(100 * i // total)
        bar = char * filled_length + '-' * (100 - filled_length)
        sys.stdout.write(f'\rProgress: [{bar}] {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

custom_char_progress_bar(100, char='=')
