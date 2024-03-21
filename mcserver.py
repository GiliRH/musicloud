from youtube_search import YoutubeSearch
import webbrowser
from pytube import YouTube
import urllib.request
import os
import hashlib
import socketio

# from bs4 import BeautifulSoup

import socket
import json
import threading


sio = socketio.Server()
k = 0


def download_mp3(name, destination):
    results = YoutubeSearch(name, max_results=10).to_dict()
    for v in results:
        print('https://www.youtube.com' + v['url_suffix'] + ' title: ' + v['title'])
        url = 'https://www.youtube.com' + results[0]['url_suffix']
    yt = YouTube(url)
    # check for destination to save file
    # select only mp3
    stream = yt.streams.filter(only_audio=True).first()
    # download the file
    out_file = stream.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


def download_mp4(name, destination):
    results = YoutubeSearch(name, max_results=10).to_dict()
    for v in results:
        print('https://www.youtube.com' + v['url_suffix'] + ' title: ' + v['title'])
        url = 'https://www.youtube.com' + results[0]['url_suffix']
    yt = YouTube(url)
    # check for destination to save file
    # select only mp4
    stream = stream = yt.streams.get_highest_resolution()
    # download the file
    out_file = stream.download(output_path=destination)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


@sio.on('connect')
def connect(sid, environ):
    print(f'Client connected with sid: {sid}')


# Define a function to handle client disconnection event
@sio.on('disconnect')
def disconnect(sid):
    print(f'Client disconnected with sid: {sid}')


# Define a function to handle custom events from clients
@sio.on('message')
def message(sid, data):
    print(f'Message received from client with sid {sid}: {data}')
    # Broadcast the received message to all connected clients except the sender
    sio.emit('message', data, room=sid)


@sio.on('kawabanga')
def kawabanga(sid):
    global k
    k += 1
    sio.emit('message', f'kawabanga {k}', room=sid)


if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)