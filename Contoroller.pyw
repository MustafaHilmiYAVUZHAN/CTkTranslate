from pynput import keyboard
from os import spawnl,P_NOWAIT,getcwd,path,system
from sys import exit as ex
from sys import executable
from subprocess import Popen
def on_press(key,process):
    try:
        print(len(process))
        print(type(key.char))
        if key.char.encode("utf-8")==b'\x14':
            print("open....")
            print(executable+" "+path.join(getcwd(),"Translate.pyw"))
            print("poolllll")
            

            if len(process)==0:
                process.append(Popen([executable,path.join(getcwd(),"Translate.pyw")]))
                print(process[-1].poll())
            elif  process[-1].poll() is not None :
                process.append(Popen([executable,path.join(getcwd(),"Translate.pyw")]))
                print(process[-1].poll())

            #system("python Translate.pyw")
            #₺₺₺system("translate.exe")
        print('alphanumeric key {0} pressed'.format(
            key.char))
        return process
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
process=[]
with keyboard.Listener(
        on_press=lambda key:exec('process=on_press(key ,process)'),
        on_release=on_release) as listener:
    listener.join()