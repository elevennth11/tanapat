import socket , pickle
from datetime import datetime

def capitalize_name(nickname):
    return nickname.capitalize()

port = 9876

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
correct_password = "331"

try:
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
            response = "32"
            server_socket.sendto(response.encode(), server_address2)
            
        else:
            response = (data2.decode())
            server_socket.sendto(response.encode(), server_address2)
    server_socket.close()


except Exception as e:
    print("An error occurred:", e)

finally:
    print('closing socket')
    server_socket.close()