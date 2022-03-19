import sys

from pynput import keyboard
clicks=0

def on_press(key):
    global clicks
              
    clicks+=1
    print(clicks)

    if clicks>=15:
        with open('log.txt','w') as f:
            f.write(str(clicks)) 
        sys.exit()



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()