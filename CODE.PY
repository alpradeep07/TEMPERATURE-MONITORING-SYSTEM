import time
import Adafruit_DHT  # Library for DHT sensors (install via pip)
import serial        # For serial communication (optional)

# Define the sensor type and the pin it's connected to
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Pin number where the sensor is connected (GPIO4 for Raspberry Pi)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if temperature is not None:
            # Print temperature and humidity to the serial monitor
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Humidity: {humidity:.2f}%")
        else:
            print("Failed to retrieve data from the sensor.")
        
        # Pause for a bit to avoid overloading
        time.sleep(2)

except KeyboardInterrupt:
    print("Terminating the program.")
