let x = 2
let y = 2
let position = [0, 0]
led.plot(x, y)
let listdat = [0, 0]
function save() {
    
    basic.clearScreen()
    position = [x, y]
    led.plot(x, y)
    console.log("x = ")
}

save()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (x > -0) {
        
        x -= 1
        save()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (x < 4) {
        
        x += 1
        save()
    }
    
})
