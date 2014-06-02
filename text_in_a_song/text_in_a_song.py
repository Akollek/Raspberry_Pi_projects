import search
from subprocess import call
from flask import *
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET'])
def HandleSongRequest():
#	Search for the song
	results=search.youtube_search(request.values.get('Body', None))
	id=results[0]
	title=results[1]
	filename=id+".m4a"	

#	Download the song
	call(['youtube-dl','-o',filename,'-x',id])
			
#	Play the song
	call(['omxplayer',filename])
	
#	Delete the file
	call(['rm',filename])		


if __name__ == "__main__":
	app.run(debug=True)
