import paho.mqtt.publish as publish

publish.single("ifn649", "LED_ON", hostname="3.27.23.183")
print("Done")