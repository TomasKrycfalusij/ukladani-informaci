let x = 2
let y = 2
let position = [0, 0]
led.plot(x, y)
let listdat : number[][] = []
function save() {
    
    basic.clearScreen()
    position = [x, y]
    led.plot(x, y)
    listdat.push(position)
    console.log("--")
    listdat.forEach(function _x(z: any, ignored: any) {
        console.log(z)
    })
    console.log("--")
}

save()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (x > 0) {
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
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    if (y > 0) {
        y -= 1
        save()
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    if (y < 4) {
        y += 1
        save()
    }
    
})
