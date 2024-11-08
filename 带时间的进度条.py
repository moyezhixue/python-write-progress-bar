import sys
import time

def time_aware_progress_bar(total):
    start_time = time.time()
    for i in range(total + 1):
        percent = 100 * i / total
        filled_length = int(100 * i // total)
        bar = '#' * filled_length + '-' * (100 - filled_length)
        elapsed_time = time.time() - start_time
        if percent > 0:
            estimated_total_time = elapsed_time / (percent / 100)
            remaining_time = estimated_total_time - elapsed_time
            sys.stdout.write(f'\rProgress: [{bar}] {percent:.2f}% - Elapsed: {elapsed_time:.2f}s, Remaining: {remaining_time:.2f}s')
        else:
            sys.stdout.write(f'\rProgress: [{bar}] {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # 模拟工作进度
    sys.stdout.write('\n')

time_aware_progress_bar(100)
