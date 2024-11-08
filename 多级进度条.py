import time
import sys

def multi_level_progress_bar(total, levels=5):
    for i in range(total + 1):
        percent = 100 * i / total
        for level in range(levels):
            level_percent = 100 * (i + level) / (total + levels - 1)
            hashes = '#' * int(level_percent / (100 / levels))
            spaces = ' ' * (levels - len(hashes))
            sys.stdout.write(f"\rLevel {level + 1}: [{hashes}{spaces}]")
        sys.stdout.write(f" {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")

multi_level_progress_bar(100)
