"""
--------------------------------------------------------------------------
Blink USR3 LED
--------------------------------------------------------------------------
License:   
Copyright 2025 - Hamza Saeed
--------------------------------------------------------------------------
Blinks the USR3 LED on the PocketBeagle at 5 Hz.
"""
import Adafruit_BBIO.GPIO as GPIO
import time

# Constants
LED_PIN = "USR3"
BLINK_FREQ_HZ = 5
BLINK_DELAY_S = (1.0 / BLINK_FREQ_HZ) / 2.0  # Calculate delay for on/off state


GPIO.setup(LED_PIN, GPIO.OUT)

print("Blinking USR3 LED at 5 Hz. Press Ctrl-C to exit.")

try:
    while True:
        # Turn LED ON
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(BLINK_DELAY_S)

        # Turn LED OFF
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(BLINK_DELAY_S)
except KeyboardInterrupt:

    GPIO.cleanup()

print("\nProgram finished.")