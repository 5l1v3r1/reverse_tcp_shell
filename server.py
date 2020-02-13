#!/usr/bin/env python

import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 1337))
    s.listen()
    print("[+] Listening for incoming connections")
    conn, addr = s.accept()
    print("[+] Client connected")
    return conn, addr

def main():
    conn, addr = connect()
    while True:
        # Enter the command to execute on clients end
        command = input(">_ ").strip().encode('utf-8')
        # send the command to the client
        conn.send(command)
        # read the clients output
        output = conn.recv(4096).decode('utf-8')
        # display the output
        print(output)
    
main()

