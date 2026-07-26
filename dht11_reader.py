import time
import board
import adafruit_dht
# Set up the sensor
dhtDevice = adafruit_dht.DHT11(board.D17)  # Replace D17 with your GPIO pin
while True:
	try:
	    temperature_c = dhtDevice.temperature
	    humidity = dhtDevice.humidity
	    if temperature_c is not None and humidity is not None:
	       temperature_f = temperature_c * 9 / 5 + 32
	       print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F | Humidity: {humidity:.1f}%")
	    else:
	       print("Sensor reading failed, trying again...")
	except RuntimeError as error:
	       print("Runtime Error: {error.args[\^\^0\^\^]}")
#        time.sleep(2.0)
