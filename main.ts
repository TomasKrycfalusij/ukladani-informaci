let x = 2
let y = 2
let position = [0, 0]
led.plot(x, y)
let list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
function save() {
    basic.clearScreen()
    
    position = [x, y]
    led.plot(x, y)
    console.log(position)
}

save()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (x > -0) {
        
        x -= 1
        console.log(x)
        save()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (x < 4) {
        
        x += 1
        console.log(x)
        save()
    }
    
})
