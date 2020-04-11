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

addr = (serverName, port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
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
            s.sendto(str.encode(request), addr)
            response = s.recvfrom(128)
            response = response[0].decode()
            print('Pergjigjia: ', repr(response))
        except:
            print("Ka ndodhur nje gabim")

