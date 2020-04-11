import re
import random
import os
import sys

from socket import *
from datetime import *
from math import gcd
from _thread import *


def ipaddress():
    return "IP Adresa e klientit eshte: %s" % addr[0]


def porti():
    return "Klienti eshte duke perdorur portin %s" % addr[1]


def count(request):
    bashketinglloret = "BCDFGHJKLMNPQRSTVWXZ"
    zanoret = "AEOYUI"
    nrbash = 0
    nrzan = 0
    message = str(request[1:]).upper()
    for char in message:
        if(char in zanoret):
            nrzan += 1
        elif(char in bashketinglloret):
            nrbash += 1
    return "Teksti i pranuar permban "+str(nrzan)+" zanore dhe "+str(nrbash)+" bashketingellore"


def reverse(request):
    my_str = str(request[1:])
    my_str = re.sub("\[|\]|\,|\'", "", my_str)
    rev_str = my_str[::-1]
    return rev_str


def palindrome(request):
    my_str = str(request[1:])
    my_str = my_str.casefold()
    my_str = re.sub("\[|\]|\,", "", my_str)
    rev_str = my_str[::-1]
    return "Teksti i dhene eshte palindrome" if list(my_str) == list(rev_str) else "Teksti i dhene nuk eshte palindrome"


def time():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S %p")


def game():
    s = random.sample(range(1, 35), 5)
    s.sort()
    return str(s)


def gcf(n1, n2):

    n1 = int(n1)
    n2 = int(n2)
    return str(gcd(n1, n2))


def convert(type, number):
    if (not(is_number(number))):
        return "Keni dhene vlere invalide"

    number = float(number)
    if (type == "cmToFeet"):
        return number * 0.0328084
    elif (type == "FeetToCm"):
        return number / 0.0328084
    elif (type == "kmToMiles"):
        return number * 0.6213712
    elif (type == "MilesToKm"):
        return number / 0.6213712
    else:
        return "Keni shtypur gabim konvertimin"

# Metodat shtese


def path():

    return os.path.dirname(sys.executable)


def printi(text, number):

    number = int(number)
    text = str(text)
    return text * number


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def handle_request(data, conn):
    try:
        request = data.split()
        response = ""
        if request[0] == "IPADDRESS":
            response = ipaddress()
        elif request[0] == "PORT":
            response = porti()
        elif request[0] == "COUNT":
            response = count(request)
        elif request[0] == "REVERSE":
            response = reverse(request)
        elif request[0] == "PALINDROME":
            response = palindrome(request)
        elif request[0] == "TIME":
            response = time()
        elif request[0] == "GAME":
            response = game()
        elif request[0] == "GCF":
            response = gcf(request[1], request[2])
        elif request[0] == "CONVERT":
            response = str(convert(request[1], request[2]))
        elif request[0] == "PATH":
            response = path()
        elif request[0] == "PRINT":
            response = printi(request[1], request[2])
        else:
            response = "Keni shtypur gabim kerkesen"
        conn.sendall(str.encode(response))
    except:
        response = "Ka ndodhur nje gabim"
        conn.sendall(str.encode(response))


def client_thread(conn):
    while True:
        data = conn.recv(128).decode()
        if not data:
            break
        handle_request(data, conn)
    conn.close()


host = 'localhost'
port = 13000
s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))
s.listen(5)
print("Serveri eshte startuar")


while True:
    conn, addr = s.accept()
    print("Lidhur me " + addr[0] + ":" + str(addr[1]))
    start_new_thread(client_thread, (conn,))

s.close()
