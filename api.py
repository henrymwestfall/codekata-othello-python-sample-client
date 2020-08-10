import requests

from flask import json


class API:
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def get_board(self):
        resp = requests.get(f"{self.url}/boards/{self.key}")

        if resp:
            return json.loads(resp.text)["boards"][0]
        else:
            print("Error fetching board.")
    
    def get_move_needed(self):
        resp = requests.get(f"{self.url}/move_needed/{self.key}")

        if resp:
            return json.loads(resp.text)["needed"]
        else:
            print("Error checking for move needed.")

    def do_move(self, move):
        x, y = move
        resp = requests.post(f"{self.url}/move/{self.key}/{y}/{x}")

        if not resp:
            print("Error making move")

    def set_name(self, name):
        resp = requests.post(f"{self.url}/set_name/{self.key}/{name}")

        if not resp:
            print("Error setting name.")