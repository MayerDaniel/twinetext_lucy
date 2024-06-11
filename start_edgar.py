import imessage
import threading
import sys
import time
import os
import adventure

class Listener:
    def __init__(self):
        self.Adv = adventure.Adventure(sys.argv[1])

    def listen(self):
        print ("The adventure is listening!")
        homedir = os.environ['HOME']
        path = homedir + "/Library/Messages/"
        self.Adv.start_adventure('5047567435')
        try:
            while True:
                time.sleep(1)
                messages = imessage.get_last_message()
                threads = []
                for message in messages:
                    t = threading.Thread(target=self.Adv.read(message))
                    threads.append(t)
                    t.start()
        except KeyboardInterrupt:
            sys.exit(0)
        

def main():
    l = Listener()
    l.listen()

if __name__ == '__main__':
    main()
