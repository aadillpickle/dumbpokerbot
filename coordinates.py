from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f'You clicked at {(x, y)}')

# Listen to mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
