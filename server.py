from youtube_search import YoutubeSearch
import webbrowser
from pytube import YouTube
import urllib.request
import os
import hashlib
import socket


# from bs4 import BeautifulSoup

import socket
import json
import threading

# Sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Java Programming", "author": "Jane Smith"}
]


def send_response(client_socket, response):
    client_socket.sendall(response.encode('utf-8'))


def receive_request(client_socket):
    request = client_socket.recv(1024)
    return request.decode('utf-8')


def handle_client_connection(client_socket):
    request_data = receive_request(client_socket)
    print('Received:', request_data)

    if request_data == 'GET /books HTTP/1.1':
        response_data = json.dumps(books)
    else:
        response_data = 'HTTP/1.1 404 Not Found\r\n\r\n'

    send_response(client_socket, response_data)
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(5)
    print('Server listening on port 8888...')

    while True:
        client_socket, _ = server_socket.accept()
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()


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


if __name__ == '__main__':
    start_server()