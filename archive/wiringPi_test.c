#include <wiringPi.h>

// Define GPIO18 number
#define GPIO18 4

// Main function
int main(void) {
        int i;

        // Initialize WiringPi
        if(wiringPiSetupGpio() == -1) return 1;

        // Set GPIO18 pin to output mode
        pinMode(GPIO18, OUTPUT);

        // Repeat LED blinking 10 times
        for(i=0; i<10; i++){
                digitalWrite(GPIO18, 0);
                delay(950);
                digitalWrite(GPIO18, 1);
                delay(50);
        }

        // Turn off LED
        digitalWrite(GPIO18, 0);

        return 0;
}