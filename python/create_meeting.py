import requests
import json
import time
import jwt
import os
from dotenv import load_dotenv
from uuid import uuid4

def create_jwt():
	dotenv_path = "../.env"
	load_dotenv(dotenv_path)

	app_id      = os.environ.get("APP_ID")
	key_file    = os.environ.get("KEY_PATH")
	secret      = open(key_file, "r").read()
	iat         = int(time.time())
	exp         = iat + 3600

	payload = dict()
	payload.setdefault("application_id", app_id)
	payload.setdefault("iat", iat)
	payload.setdefault("nbf", iat)
	payload.setdefault("exp", exp)
	payload.setdefault("jti", str(uuid4()))

	token = jwt.encode(payload, secret, algorithm="RS256")
	return(token)

def create_meeting(token):
	url = "https://api-eu.vonage.com/beta/meetings/rooms"
	payload = json.dumps({
  		"display_name": "Pink Meetings Are Better",
  		"metadata": "This is a fantastic description of the Meeting",
  		"type": "long_term",
  		"expires_at": "2023-12-31T23:59:59.000Z",
 		"recording_options": {
    		"auto_record": False,
    		"record_only_owner": False
  		},
  		"expire_after_use": False,
  		"theme_id": "{{your_theme_id_here}}",
	  	"join_approval_level": "explicit_approval",
  		"initial_join_options": {
  			"microphone_state": "off"
  		},
  		#"callback_urls": {
  			#"rooms_callback_url": "{{callback_url}}",
  			#"sessions_callback_url": "{{callback_url}}",
  			#"recordings_callback_url": "{{callback_url}}"
  		#},
  		"available_features": {
  			"is_recording_available": True,
  			"is_chat_available": True,
  			"is_whiteboard_available": True
  		}
	})
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer ' + token
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	

token = create_jwt()
create_meeting(token)
