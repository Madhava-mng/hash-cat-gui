#!/bin/env python3


from base64 import *
from codelib.rot import *
from tkinter import *
from tkinter import filedialog as _fd
from hashmodes import HASH_MODE as HASH_TYPE
from time import sleep as _sleep
from threading import Thread as _thread
from subprocess import run as _run
from os import getenv as _getenv
from os.path import isfile as _isfile
from os import system as _system
from psutil import cpu_percent as _cpu_percent
from psutil import cpu_count as _cpu_count
from psutil import virtual_memory as _virtual_memory
from re import search as _search
from re import ASCII as _ascii


root=Tk()
root.title('hash cat gui')
root.geometry("511x674")
root.configure(bg = 'gray')
icon = PhotoImage(file='./.icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)


# default configaration

if(_isfile('/usr/share/wordlists/rockyou.txt')):
    DICT_FILE = '/usr/share/wordlists/rockyou.txt'
else:
    DICT_FILE = ''

SAVED_HASHES = '/.hashcat/hashcat.potfile'
ROOT_HOME = _getenv('HOME')
HASH_STATUS = 'None'
ATTACK_MODE = ['0', '1', '3', '6', '7']
#attack_under_progress = 0



def notify(value, bg):
    try:
        msg_label = Label(root, text=value, width=62, borderwidth=4, bg=bg, fg="black")
        msg_label.grid(row=3,column=0)
        _sleep(2)
        msg_label.destroy()
    except:
        pass


def station():
    tmp_val = 0
    try:
        frame_2.destroy()
        tmp_val = 1
    except:
        pass
    def update():
        if (False):
            clicked_hash.set("0")
            _thread(target = notify, args=["Invalied hash mode", "tomato3"]).start()
        _thread(target = notify, args=["Value updated", "green"]).start()
        launch.set("hashcat --quiet -a "+clicked_mode.get()+" -m "+clicked_hash.get()+" "+f1_f1_e1.get()+" "+f1_f2_e1.get())
    def import_hash():
        try:
            hash_.set(_fd.askopenfile().name)
            _thread(target = notify, args=["Value set for hash", "green"]).start()
        except:
            pass
    def import_dict():

        try:
            dict_.set(_fd.askopenfile().name)
            dict_file = dict_.get()
            _thread(target = notify, args=["Value set for wordlist", "green"]).start()
        except:
            pass

    def process_start():
        print(f1_f4_e1.get())
        _thread(target = notify, args=["Attack started", "green"]).start()
        _system(f1_f4_e1.get())
        _thread(target = notify, args=["Attack fineshed", "green"]).start()

    def launch_it():
        update()
        if (hash_.get().strip()):
            _thread(target=process_start).start()
        else:
            _thread(target = notify, args=["Attack postponted. due to hash value", "tomato3"]).start()

    frame_1 = LabelFrame(root, text="(Crack Station)" ,bg = "gray",padx=30, pady=20, width=3)
    frame_1.grid(row= 2, column= 0)
    # main frame1 and functions:
    # hash file
    f1_f1 = LabelFrame(frame_1, padx=32, pady=25, text="(hash or file)", bg="gray30", fg='white')
    f1_f1.grid(row=0 , column=0, pady=10)
    hash_ = StringVar()
    f1_f1_e1 = Entry(f1_f1, bg='green', fg='black', width=30, textvariable=hash_)
    f1_f1_b1 = Button(f1_f1, bg='black', fg='green', width=10,height=0, text="Import", command=import_hash)
    f1_f1_e1.grid(row=0, column=1, padx=10)
    f1_f1_b1.grid(row=0, column=2)
    # dictnary file
    f1_f2 = LabelFrame(frame_1, padx=32, pady=25, text="(dictnary file or attack syntax)", bg="gray30", fg='white')
    f1_f2.grid(row=2 , column=0, pady=10)
    dict_ = StringVar()
    dict_.set(DICT_FILE)
    f1_f2_e1 = Entry(f1_f2, bg='green', fg='black', width=30, textvariable=dict_)
    f1_f2_b1 = Button(f1_f2, bg='black', fg='green', width=10,height=0, text="Import", command=import_dict)
    f1_f2_e1.grid(row=0, column=1, padx=10)
    f1_f2_b1.grid(row=0, column=2)
    # options
    #   \_attack mode
    #   \_hash type
    f1_f3 = LabelFrame(frame_1, padx=31, pady=45, bg="gray30", fg='white')
    f1_f3.grid(row=3 , column=0, pady=10)
    # attack mode
    f1_f3_f1 = LabelFrame(f1_f3, padx=1, pady=1, text="(attackmode)", bg="gray", fg='white')
    f1_f3_f1.grid(row=0 , column=0)
    clicked_mode = StringVar()
    clicked_mode.set(ATTACK_MODE[0])
    f1_f3_f1_o1 = OptionMenu(f1_f3_f1 , clicked_mode, *ATTACK_MODE)
    f1_f3_f1_o1.config(bg="black", fg="green", width=7)
    f1_f3_f1_o1.grid(row=0, column=0, padx=4)
    # hash type
    f1_f3_f2 = LabelFrame(f1_f3, padx=1, pady=1, text="(hashtype)", bg="gray", fg='white')
    f1_f3_f2.grid(row=0 , column=1, padx=5, pady=1)
    clicked_hash = StringVar()
    clicked_hash.set(HASH_TYPE[0])
    f1_f3_f2_e1 = Entry(f1_f3_f2, bg='green', fg='black', width=15, textvariable=clicked_hash)
    f1_f3_f2_o1 = OptionMenu(f1_f3_f2 , clicked_hash, *HASH_TYPE)
    f1_f3_f2_o1.config(bg="black", fg="green", width=4)
    f1_f3_f2_e1.grid(row=0, column=0,padx=1, pady=4)
    #f1_f3_f2_o1.grid(row=0, column=1,padx=1)
    # update
    f1_f3_f3 = LabelFrame(f1_f3, padx=1, pady=1, text="(update)", bg="gray", fg='white')
    f1_f3_f3.grid(row=0 , column=2)
    f1_f3_f3_b1 = Button(f1_f3_f3, bg='black', fg='green', width=10,height=0, text="Update", command=update)
    f1_f3_f3_b1.grid(row=0, column=0, padx=1)
    # launch attack
    f1_f4 = LabelFrame(frame_1, text="(edit and launch)", padx=32, pady=25, bg="gray30", fg='white')
    f1_f4.grid(row=4 , column=0, pady=15)
    launch = StringVar()
    #launch.set("hashcat --quite -a "+clicked_mode.get()+" -m "+clicked_hash.get()+" "+hash_.get()+" "+dict_.get())
    update()
    f1_f4_e1 = Entry(f1_f4, bg='green', fg='black', width=30, textvariable=launch)
    f1_f4_b1 = Button(f1_f4, bg='black', fg='green', width=10,height=0, text="Launch", command=launch_it)
    f1_f4_e1.grid(row=0, column=1, padx=10)
    f1_f4_b1.grid(row=0, column=2)
    if(tmp_val !=0):
        _thread(target = notify, args=["Crack Station", "green"]).start()

def status():
    try:
        frame_1.destroy()
        tmp_val = 1
    except:
        pass

    _thread(target = notify, args=["Status Loading", "green"]).start()
    global frame_2

    frame_2 = LabelFrame(root, text="(Status)" ,bg = "gray",padx=0, pady=3, width=3)
    frame_2.grid(row= 2, column= 0)

    f2_f1 = LabelFrame(frame_2, text="(hardware status)", padx=6, pady=0, bg="gray30", fg='white')
    f2_f2 = LabelFrame(frame_2,  padx=0, pady=0, bg="gray30", fg='white')
    f2_f3 = LabelFrame(frame_2,  padx=0, pady=0, bg="gray30", fg='white')

    f2_f1.grid(row=2 , column=0, pady=16)
    f2_f2.grid(row=0 , column=0, pady=16)
    f2_f3.grid(row=1 , column=0, pady=16)


    f2_cpu_p = StringVar()
    f2_cpu_p.set("cpu: ["+str(_cpu_percent())+"%]")
    f2_cpu_c = StringVar()
    f2_cpu_c.set("c-cnt: ["+str(_cpu_count())+"]")
    f2_mem_p = StringVar()
    f2_mem_p.set("mem: ["+str(_virtual_memory().percent)+"%]")
    f2_mem_t = StringVar()
    f2_mem_t.set("mem-tot:[{}]".format(str(_virtual_memory().total/(1024*1024*1024))))

    f2_f2_e1 = Entry(f2_f2, bg='green', fg='black', width=12, textvariable=f2_cpu_p)
    f2_f2_e2 = Entry(f2_f2, bg='green', fg='black', width=11,textvariable=f2_cpu_c)
    f2_f2_e3 = Entry(f2_f2, bg='green', fg='black', width=12,textvariable=f2_mem_p)
    f2_f2_e4 = Entry(f2_f2, bg='green', fg='black', width=18,textvariable=f2_mem_t)

    f2_f2_e1.grid(row=0, column=0, padx=4, pady=4)
    f2_f2_e2.grid(row=0, column=1, padx=4, pady=4)
    f2_f2_e3.grid(row=0, column=2, padx=4, pady=4)
    f2_f2_e4.grid(row=0, column=3, padx=4, pady=4)

    # FRAME 3

    f2_mem_u = StringVar()
    f2_mem_u.set("mem-usd:[{}]".format(str(_virtual_memory().used/(1024*1024*1024))))

    f2_mem_b = StringVar()
    f2_mem_b.set("mem-buf:[{}]".format(str(_virtual_memory().buffers/(1024*1024*1024))))

    f2_mem_c = StringVar()
    f2_mem_c.set("mem-cac:[{}]".format(str(_virtual_memory().cached/(1024*1024*1024))))

    f2_mem_f = StringVar()
    f2_mem_f.set("mem-fre:[{}]".format(str(_virtual_memory().free/(1024*1024*1024))))


    f2_f3_e1 = Entry(f2_f3, bg='green', fg='black', width=13,textvariable=f2_mem_u)
    f2_f3_e2 = Entry(f2_f3, bg='green', fg='black', width=13,textvariable=f2_mem_b)
    f2_f3_e3 = Entry(f2_f3, bg='green', fg='black', width=13,textvariable=f2_mem_c)
    f2_f3_e4 = Entry(f2_f3, bg='green', fg='black', width=14,textvariable=f2_mem_f)

    f2_f3_e1.grid(row=0, column=0, padx=4, pady=4)
    f2_f3_e2.grid(row=0, column=1, padx=4, pady=4)
    f2_f3_e3.grid(row=0, column=2, padx=4, pady=4)
    f2_f3_e4.grid(row=0, column=3, padx=4, pady=4)

    try:
        f2_tmp = _run(["hashcat", "-I"], capture_output=True).stdout.decode().strip()
        list_of_info1 = f2_tmp.split("\n")
        f2_f1_l1 = Listbox(frame_2, height=24, width=60, fg="white", bg="gray30")
        for i in list_of_info1:
                f2_f1_l1.insert(END, i)
        f2_f1_l1.grid(row=2, column=0, pady=5, padx=9)
    except:
        _thread(target = notify, args=["hashcat comand not found make the path accesable", "tomato3"]).start()
        frame_2.destroy()


def cracked(search_value = ""):

    try:
        frame_1.destroy()
        tmp_val = 1
    except:
        pass

    global frame_2

    frame_2 = LabelFrame(root, text="(Cracked)" ,bg = "gray",padx=3, pady=3, width=3)
    frame_2.grid(row= 2, column= 0)
    val= StringVar()
    val.set(search_value)
    f2_f1 = LabelFrame(frame_2, padx=21, pady=9, bg="gray30", fg='white')
    f2_f1.grid(row=1, column=0, padx=1)
    f2_e1 = Entry(f2_f1, bg='green', fg='black', width=39,textvariable=val)
    f2_e1.grid(row=1, column=0, padx=5)
    f2_b1 = Button(f2_f1, bg='black', fg='green', width=10,height=0, text="Search", command=lambda:cracked(f2_e1.get()))
    f2_b1.grid(row=1, column=1, padx=5)

    try:
        with open(ROOT_HOME+SAVED_HASHES, 'r') as file_buffer:
            f2_f1_l1 = Listbox(frame_2, height=29, width=61, fg="white", bg="gray30")
            a = " "
            while(True):
                if(a != ''):
                    a = file_buffer.readline().replace("\n", "")
                    try:
                        _search(r'(.*?)'+search_value.lower().strip()+'(.*).*', a.lower(), _ascii).group()
                        tmp = []
                        for i in range(len(a)):
                            if(a[i] == ":"):
                                tmp.append("")
                                tmp.append("value:  ("+a[i+1:]+')')
                                tmp.append("hash :  ("+a[:i]+')')
                                break
                        for i in tmp:
                            f2_f1_l1.insert(1, i)
                    except:
                        pass
                else:
                    break
            f2_f1_l1.grid(row=0, column=0, padx=1)

    except:
        _thread(target = notify, args=["File Not found "+ROOT_HOME+SAVED_HASHES, "tomato3"]).start()
        frame_2.destroy()



def online():
    _thread(target = notify, args=["In next update", "green"]).start()

def format_():
    _thread(target = notify, args=["In next update", "green"]).start()













# app starts hear

frame=LabelFrame(root,width=3,padx=3,pady=3,bg="gray")


f_b1 = Button(frame, bg="black", fg="green", text='station', width=9, command=station)
f_b2 = Button(frame, bg="black", fg="green", text='status',  width=9, command=status)
f_b3 = Button(frame, bg="black", fg="green", text='cracked', width=9, command=cracked)
f_b4 = Button(frame, bg="black", fg="green", text='online',  width=9, command=online)
f_b5 = Button(frame, bg="black", fg="green", text='format',  width=9, command=format_)


f_b1.grid(row= 0, column= 0)
f_b2.grid(row= 0, column= 1)
f_b3.grid(row= 0, column= 2)
f_b4.grid(row= 0, column= 3)
f_b5.grid(row= 0, column= 4)

frame.grid(row= 1, column= 0)


station()

_thread(target = notify, args=["App started", "green"]).start()

root.mainloop()