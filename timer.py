import time

def countdown_timer(total_seconds):
    while total_seconds > 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer)
        time.sleep(1)
        total_seconds -= 1
