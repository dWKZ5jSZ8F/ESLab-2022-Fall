#include "mbed.h"

PwmOut led(PA_15);
InterruptIn button(BUTTON1);
int button_switch = 0;

void button_pressed(){
    button_switch++;
}

void button_released(){
    if (button_switch > 2){
        button_switch = 0;
    }
}

int main()
{
    led.period(0.20f);     
    led.write(0.50f);
    button.fall(&button_pressed);
    button.rise(&button_released);
    
    while (1){
        if (button_switch == 1){
            led.resume();
        }else if (button_switch == 2) {
            ThisThread::sleep_for(50);
            led.period(0.20f);      
            led.write(0.50f);
        }else{
            led.suspend();
        }
    }
}
