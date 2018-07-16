from pynput import mouse
from pynput.mouse import Button
from pynput import keyboard
import pickle

history = []

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    history.append((x, y))

def on_click(x, y, button, pressed):
    print(button, '{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    history.append(button)
    if button == Button.middle:
        return keyboard_listener.start()

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        ((x, y))))
    history.append((dx, dy))

mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)

def on_press(key):
    history.append(key)
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    if key == keyboard.Key.shift_r:
        mouse_listener.start()
    if key == keyboard.Key.shift_l:
        pickle.dump(history, open("history", mode="a"))
        return False

def on_release(key):
    print('{0} released'.format(
        key))

# Collect events until released
keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

keyboard_listener.start()
keyboard_listener.join()


