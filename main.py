x = 2
y = 2
position = [0,0]
led.plot(x, y)
listdat:List[List[number]] = []

def _x(z, ignored):
    print(z)

def save():
    global position
    basic.clear_screen()
    position = [x, y]
    led.plot(x, y)
    listdat.append(position)
    print("--")
    listdat.for_each(_x)
    print("--")

save()

def on_button_pressed_a():
    global x
    if x > 0:
        x -= 1
        save()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    if x < 4:
        x += 1
        save()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_event_pressed():
    global y
    if y > 0:
        y -= 1
        save()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_pin_pressed_p2():
    global y
    if y < 4:
        y += 1
        save()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)