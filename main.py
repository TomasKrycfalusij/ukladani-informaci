x = 2
y = 2
position = [0,0]
led.plot(x,y)
listdat = [0,0]

def save():
    global position, listdat
    basic.clear_screen()
    position = [x,y]
    led.plot(x,y)
    listdat.insert("x =", x)
    print(listdat)
save()



def on_button_pressed_a():
    if x > -0:
        global x
        x -= 1
        save()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if x < 4:
        global x
        x += 1
        save()
input.on_button_pressed(Button.B, on_button_pressed_b)