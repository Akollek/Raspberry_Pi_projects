
import json
from subprocess import call



token_json=open('token.json','r+')
token_data=json.load(token_json)
token_json.close()
token=str(token_data['play_token'])
call(['touch','token'])
token_file=open('token','w')
token_file.write(token)
token_file.close()


	