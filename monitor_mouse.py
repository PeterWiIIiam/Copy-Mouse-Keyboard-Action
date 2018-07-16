from pynput import mouse
from pynput.mouse import Button

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print(button, '{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    print(Button.left, button == Button.left)


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
def with_statements():
    print("1")
# Collect events until released
listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)

listener.start()
listener.join()

