"""
Server side (Backend): Flask
Here, based on the request received from the front end (React), Using Flask, we trigger the Twitter API to create and save information tweets.

Developer:Anandu Sreekumar  

"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from ./delete_tweet import *

app = Flask(__name__)
CORS(app)
tweets = []

#get and create the tweet

@app.route('/api/posts', methods=['GET', 'POST'])

def handle_tweets():
    if request.method == 'POST':
        url = "https://www.google.com/url?q=https://api.twitter.com/2/tweets&source=gmail-imap&ust=1695607170000000&usg=AOvVaw1xx2t_6Rpuy0HaBb6gkmsq"
        payload = json.dumps(request.json)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth oauth_consumer_key="4J9PQgTz5kgxo3jdljuT2Agy6",oauth_token="1702052876053626881-cQVNNjnw6r1Vy2xI57BIHLwuHnylwS",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1695000881",oauth_nonce="VD2b3OGHD9y",oauth_version="1.0",oauth_signature="3Ruo4qsa8lzVzXQiWcaCXIsfM90%3D"',
            'Cookie': 'guest_id=v1%3A169472576653552696; guest_id_ads=v1%3A169472576653552696; guest_id_marketing=v1%3A169472576653552696; personalization_id="v1_8KgnN8Ge/ofv6X6QhsUXbw=="'
}
        response = requests.request("POST", url, headers=headers, data=payload)
        temp = json.loads(response.text)
        #save post information locally
        posts.append(temp)
        return temp
    else:
        return jsonify(posts)

#main class
if __name__ == '__main__':
    app.run(debug=True)