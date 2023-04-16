import math
import time

# Define the symbols for the heart shape
symbols = ["♥", "❤", "💗", "💕"]

# Define the parameters for the spinning hearts
radius = 10
angular_speed = 0.1

# Clear the screen
def clear_screen():
    print('\033c')

# Main loop for spinning hearts
while True:
    clear_screen()
    for i in range(360):
        angle = math.radians(i)
        x = int(radius * math.cos(angle))
        y = int(radius * math.sin(angle))
        heart_symbol = symbols[i % len(symbols)]
        print(" " * (radius + y) + heart_symbol)
        time.sleep(0.01)