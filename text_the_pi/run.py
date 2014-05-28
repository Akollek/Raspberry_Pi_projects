import wiringpi
from flask import *
import twilio.twiml
import time


app = Flask(__name__)

@app.route("/", methods=['GET'])
def flashLED():
	wiringpi.wiringPiSetup()
	wiringpi.pinMode(15, 1)
	wiringpi.digitalWrite(15, 0)
	for x in xrange(0,int(request.values.get('Body', None))):
		wiringpi.digitalWrite(15, 1)
		time.sleep(1)
		wiringpi.digitalWrite(15, 0) 
		time.sleep(1)
	return ('A message was received!')

if __name__ == "__main__":
	app.run(debug=True)
