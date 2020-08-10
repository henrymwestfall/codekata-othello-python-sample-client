import threading
import time
import sys

from api import API
from ai import AI
from game import Board

class Runner:
    def __init__(self, ai, api_url, api_key):
        self.ai = ai
        self.api_url = api_url
        self.api_key = api_key
        self.api = API(self.api_key, self.api_url)

        self.refresh_rate = 0.5

    def wait_for_turn(self):
        while not self.api.get_move_needed():
            time.sleep(self.refresh_rate)

    def do_move(self):
        move = self.ai.do_move(Board(self.api.get_board()))
        self.api.do_move(move)

def main():
    if len(sys.argv) < 3:
        print("Expected API url as command line argument and API key(s) as the rest.")
        sys.exit(1)
    
    for i in range(2, len(sys.argv)):
        def thread():
            runner = Runner(AI(), sys.argv[1], sys.argv[i])
            print(f"Starting thread {i}. API: {sys.argv[1]}, API KEY: {sys.argv[i]}")
            print(f"Thread {i} connecting to server...")
            while True:
                runner.api.set_name(runner.ai.name)
                runner.wait_for_turn()
                print(f"Thread {i} starting turn.")
                runner.do_move()
                print(f"Thread {i} ending turn.")

        t = threading.Thread(target=thread)
        #t.daemon = True
        t.start()

if __name__ == "__main__":
    main()