import socket

serverName = input(
    "Emri i serverit: ")
port = input(
    "Porti i serverit: ")
if (serverName == ''):
    serverName = 'localhost'
if (port == ''):
    port = 13000
else:
    try:
        port = int(port)
    except:
        print("Porti i dhene eshte invalid")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, port))
    while True:
        try:
            request = input(
                "Kerkesa ('quit' per te ndalur procesin): ")
            if (request == "quit" or request == "QUIT"):
                break
            elif (len(request.encode()) > 128):
                print("Kerkesa eshte e limituar ne 128 byte")
                continue
            elif (request == ""):
                continue
            s.sendall(str.encode(request))
            response = s.recv(128).decode()
            print('Pergjigjia: ', repr(response))
        except:
            print("Ka ndodhur nje gabim")
