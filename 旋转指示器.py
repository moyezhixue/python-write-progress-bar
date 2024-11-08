import time
import sys

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def spinning_progress_bar(total):
    spinner = spinning_cursor()
    for i in range(total + 1):
        percent = 100 * i / total
        sys.stdout.write(f"\rProgress: {next(spinner)} {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

spinning_progress_bar(100)
