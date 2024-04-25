import socket , pickle , random , sys
from datetime import datetime
port = 9876
passwordserver = "332"
temp = 0
humi = 0
pump_status = "off"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

print("Server is listening on port", port)

try:
    while True:
        clientsocket, address = s.accept()
        msg = clientsocket.recv(4096).decode("utf-8")
        if msg == "passwordformclient":
            clientsocket.sendall(str.encode(passwordserver))
        msg1 = clientsocket.recv(4096)
        data_pack = pickle.loads(msg1)
        if data_pack[0] == "connect to server":
            print(f"Hello {address[0]} : {address[1]}")
            datetime_now = datetime.now()
            response = f"Hello {data_pack[1][0].upper()+data_pack[1][1:].lower()} [{datetime_now.ctime()}] "
            clientsocket.sendall(str.encode(response))
        while 1 :
            msg = clientsocket.recv(4096).decode("utf-8")
            if msg.lower() == "temp":
                header = "temp"
                temprandom = random.randrange(50)
                temp = temprandom
                response = [header, temp]
                data_pack = pickle.dumps(response)
                print(f"Temp Send {temp}")
                clientsocket.sendall(data_pack)
            elif msg.lower() == "humi":
                header = "humi"
                humirandom = random.randrange(50)
                humi = humirandom
                if humirandom >= 50:
                    pump_status = "off"
                else:
                    pump_status = "on"
                response = [header, humi]
                data_pack = pickle.dumps(response)
                print(f"Humi Send {humi}")
                clientsocket.sendall(data_pack)
            elif msg.lower() == "all":
                header = "all"
                datetime_now = datetime.now()
                response = [header, datetime_now.ctime(), temp, humi, pump_status]
                print(f"All data: {datetime_now.ctime()} Temp: {temp} Humi : {humi} PUMP STATUS : {pump_status}")
                data_pack = pickle.dumps(response)
                clientsocket.sendall(data_pack)
            elif msg.lower() == "exit":
                header = "exit"
                response = ([header,"Confirm exit (y/n): "])
                data_pack = pickle.dumps(response)
                clientsocket.sendall(data_pack)
                msgcon = clientsocket.recv(4096).decode("utf-8")
                if msgcon.lower() == "y":
                    print(".....Bye Client.....")
                    sys.exit()
            else:
                header = "nothing"
                response = ([header, msg])
                data_pack = pickle.dumps(response)
                clientsocket.sendall(data_pack)
        s.close()
except Exception as e:
    print("An error occurred:", e)

finally:
    print('closing socket')
    s.close()
