import json
from subprocess import call



mix_json=open('mix.json','r+')
mix=json.load(mix_json)
mix_json.close()
mix_id=str(mix['mix']['id'])
tracks=str(mix['mix']['tracks_count'])
call(['touch','mix'])
mix=open('mix','w')
mix.write(mix_id)
mix.close()
call(['touch','tracks'])
length=open('tracks','w')
length.write(tracks)
length.close()

	
