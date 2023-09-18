"""
Server side (Backend): Flask
Here, based on the request received from the front end (React), Using Flask, we trigger the Twitter API to  delete tweets.

Developer: Dheeraj Nandigama 

"""
#importing lib

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

#delete the tweet

@app.route('/api/posts/<int:id>', methods=['DELETE'])

def delete_tweet(id):
    url = f"https://api.twitter.com/2/tweets/{id}"

    headers = {

        'Authorization': 'OAuth oauth_consumer_key="pjq5vlo868oXu4ls1t0M7aafU",oauth_token="1702447400961572864-wO3gkrTTSjAeKRJsZrFwdMJQ7o9da4",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1694988856",oauth_nonce="Pymm9hEUJeq",oauth_version="1.0",oauth_signature="jsdNXENEqNEvMlr%2BPbgPbud6JJ8%3D"',

        'Cookie': 'guest_id=v1%3A169472576653552696; guest_id_ads=v1%3A169472576653552696; guest_id_marketing=v1%3A169472576653552696; personalization_id="v1_8KgnN8Ge/ofv6X6QhsUXbw=="'

        }

    response = requests.request("DELETE", url, headers=headers)

    post = next((x for x in posts if x['id'] == id), None)

    if post:

        posts.remove(post)

    return response.text