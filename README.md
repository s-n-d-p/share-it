# share-it

Can't find data cable to transfer a file? I got you covered :)

## What is share-it?

Derived from the concept of ShareIt/Xender (file transfer applications), share-it is the pythonic way to do the same only with much ease!

## Installation & Usage

1. Make sure you have python installed on your system
2. You can switch to a virtual env (optional, but a good practice)
3. `pip install -r requirements.txt`
4. Set `UPLOAD_FOLDER` & `PASSWORD` (on line 6 and 7) inside app.py file
5. To transfer from any device to PC, connect devices on the same network and start the app using:

    `python /home/sandeep/repos/share-it/app.py`

6. Default port is 8000 (`PORT` can be set in the environment if you want to use different port).
7. Head to PC_IP_ADDRESS:PORT on the other device, for e.g. 192.168.68.43:8000
8. To transfer from PC to any device, type the following command in the directory containing the file to be shared:

    `python3 -m http.server 8000`
    and visit PC_IP_ADDRESS:PORT on the device (port can be any valid free port)

## Bonus Content :sunglasses:

To make life even geekier, set the aliases like so:

1. Add the following to your bash configuration file (e.g. .bashrc)

    <pre>if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
    fi
    </pre>

2. Then create a .bash_aliases file in home directory with the following content:

    `alias send="python3 -m http.server 8000"`
    `alias recv="python /home/sandeep/repos/share-it/app.py"`

3. Restart your terminal, or do

    `source ~/.bashrc`

4. For sending from PC, type `send`
5. For recieving on PC, type `recv`
