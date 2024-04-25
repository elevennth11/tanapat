import socket , pickle , random , sys
from datetime import datetime

def capitalize_name(nickname):
    return nickname.capitalize()

port = 9876

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
correct_password = "331"

temp = 0
humi = 0
pump_status = "off"

try:

    while True:
        server_socket.bind(("", port))
        print("Server is listening on port", port)
        data, server_address = server_socket.recvfrom(1024)
        command = data.decode().lower()
        if command == "passwordformclient":
            response = correct_password
            server_socket.sendto(response.encode(), server_address)
        data1, server_address1 = server_socket.recvfrom(1024)
        data_arr = pickle.loads(data1)
        if data_arr[0] == "connect to server":
            datetime_now = datetime.now()
            print(f"Hello {server_address1[0]} : {server_address1[1]}")
            response = f"Hello {data_arr[1][0].upper()+data_arr[1][1:].lower()} [{datetime_now.ctime()}] "
            server_socket.sendto(response.encode(), server_address1)
        while 1:
            data2, server_address2 = server_socket.recvfrom(1024)
            if data2.decode().lower() == "temp":
                header = "temp"
                tempram = random.randrange(50)
                temp = tempram
                response = ([header, tempram])
                data_pack = pickle.dumps(response)
                print(f"Temp send {tempram}")
                server_socket.sendto(data_pack, server_address2)
            elif data2.decode().lower() == "humi":
                header = "humi"
                humiram = random.randrange(100)
                humi = humiram
                if humiram >= 50:
                    pump_status = "off"
                elif humiram <= 50:
                    pump_status = "on"
                response = ([header, humiram])
                data_pack = pickle.dumps(response)
                print(f"Humidity send {humiram}")
                server_socket.sendto(data_pack, server_address2)
            elif data2.decode().lower() == "all":
                header = "all"
                datetime_now = datetime.now()
                response = ([header, datetime_now.ctime(), temp, humi, pump_status])
                data_pack = pickle.dumps(response)
                print(f"All data send {temp} {humi} {pump_status}")
                print(f"All data: {datetime_now.ctime()} Temp: {temp} Humi : {humi} PUMP STATUS : {pump_status}")
                server_socket.sendto(data_pack, server_address2)
            elif data2.decode().lower() == "exit":
                header = "exit"
                response = ([header,"Confirm exit (y/n): "])
                data_pack = pickle.dumps(response)
                server_socket.sendto(data_pack, server_address2)
                data2, server_address2 = server_socket.recvfrom(1024)
                if data2.decode().lower() == "y":
                    print(".....Bye Client.....")
                    sys.exit()
            else:
                header = "nothing"
                response = ([header, data2.decode()])
                data_pack = pickle.dumps(response)
                server_socket.sendto(data_pack, server_address2)
        server_socket.close()


except Exception as e:
    print("An error occurred:", e)

finally:
    print('closing socket')
    server_socket.close()