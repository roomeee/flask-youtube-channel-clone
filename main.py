from flask import Flask, jsonify, render_template
import requests
from numerize.numerize import numerize
channel = {
    'clever': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
    'taylor': 'UCANLZYMidaCbLQFWXBC95Jg',
    'lana': 'UC3N5y6UWKJaKqoU2b_0MfTQ'
}

app = Flask(__name__)

import requests


data = {
    ' content': [],
    "cursorNext": 'nn'

}


@app.route('/')
def index():
    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    querystring = {"id": channel['lana'], "hl": "en", "gl": "US"}

    headers = {
        "X-RapidAPI-Key": "6df3629cc0msh6c3b9859d31a3ebp1a49c3jsnf4bbc504eda7",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data= response.json()
    contents= data['contents']
    videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
    first_video= videos[0]
    # print(videos)    # print(response.json())

    return render_template('index.html',
                           videos=videos, first_video=first_video)


@app.template_filter()
def numberize(views):
    return numerize(views, 1)


@app.template_filter()
def highest_quality_image(images):
    return images[3]['url'] if len(images) >= 4 else images[0]['url']


app.run(host='0.0.0.0', port=81)
