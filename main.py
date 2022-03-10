x = 2
y = 2
position = [0,0]
led.plot(x,y)
list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def save():
    basic.clear_screen()
    global position
    position = [x,y]
    led.plot(x,y)
    print(position)
save()



def on_button_pressed_a():
    if x > -0:
        global x
        x -= 1
        print(x)
        save()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if x < 4:
        global x
        x += 1
        print(x)
        save()
input.on_button_pressed(Button.B, on_button_pressed_b)