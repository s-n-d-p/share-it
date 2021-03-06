# share-it

Can't find data cable to transfer a file? I got you covered :)

## What is share-it?

Derived from the concept of ShareIt/Xender (file transfer applications), share-it is the pythonic way to do the same only with much ease!

## Installation & Usage

1. Make sure you have python2 installed on your system
2. You can switch to a virtual env (optional, but a good practice)
   (a) Install virtualenv.
   (b) Use the following commands:
       i. `virtualenv -p $(whereis python2) <env_name>`
      ii. `source <env_name>/bin/activate`
     iii. For exiting virtual env. use - `deactivate`
3. `pip install -r requirements.txt`
4. Set `UPLOAD_FOLDER` & `PASSWORD` enironment variable. Note that this is optional.
   (a) Default value for `UPLOAD_FOLDER` is script's directory.
   (b) Default value for `PASSWORD` is `muggle`.
5. To transfer from any device to PC, connect devices on the same network and start the app using:

    `UPLOAD_FOLDER=/path/to/upload/directory python /path/to/share-it/app.py`

6. Default port is 8000 (`PORT` can be set in the environment if you want to use different port).
7. Head to IP_ADDRESS:PORT on the other device, for e.g. 192.168.68.43:8000 (To find local IP: `ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'`)
8. To transfer from PC to any device, type the following command in the directory containing the file to be shared:

    `python3 -m http.server 8000`
    and visit IP_ADDRESS:PORT on the device (port can be any valid free port)

## Bonus Content :sunglasses:

1. Add the following to your rc file (e.g. .bashrc, .zshrc)

    <pre>if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
    fi
    </pre>

2. Then create a .bash_aliases file in home directory with the following content:

    `alias send="python3 -m http.server 8000"`
    
    `alias recv="python <path/to/share-it>/app.py"`

3. Restart your terminal, or source the .rc file
4. For sending from PC, type `send`
5. For recieving on PC, type `recv`
