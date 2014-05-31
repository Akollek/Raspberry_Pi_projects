
import json
from subprocess import call



song_json=open('song.json','r+')
song=json.load(song_json)
song_json.close()
url=str(song['set']['track']['url'])
name=str(song['set']['track']['name'])
artist=str(song['set']['track']['performer'])
duration=str(song['set']['track']['play_duration'])
track_id=str(song['set']['track']['id'])
title=name+" by "+artist
call(['touch','song'])
song=open('song','w')
song.write(url)
song.close()
call(['touch','title'])
title_file=open('title','w')
title_file.write(title)
title_file.close()
call(['touch','duration'])
dur=open('duration','w')
dur.write(duration)
dur.close()
call(['touch','track'])
track=open('track','w')
track.write(track_id)
track.close()
	
