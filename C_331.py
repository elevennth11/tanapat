import socket, pickle
import sys
import os

ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port of the server: "))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    nickname = input("Enter your nickname: ")
    while True:
        if not nickname.isalpha():
            print("Invalid input. Please enter text only.")
            nickname = input("Enter nickname: ")
            continue
        elif len(nickname) > 10:
            print("Invalid input. Nickname should not be more than 10 characters.")
            nickname = input("Enter nickname: ")
            continue
        else:
            break
    password = input("Enter password: ")
    message = "passwordformclient"
    client_socket.sendto(message.encode(), (ip, port))
    data, client_address = client_socket.recvfrom(1024)
    serverpassword = data.decode()
    while True:
        if password!= serverpassword:
            print("Incorrect password. Please try again.")
            password = input("Enter password: ")
            continue
        else:
            break
    message = (["connect to server",nickname])
    data_string = pickle.dumps(message)
    client_socket.sendto(data_string, (ip, port))
    os.system('cls')
    data1, client_address1 = client_socket.recvfrom(1024)
    recdata = data1.decode()
    print(recdata)
    while (1):
        message = input("Enter message: ")
        try:
            client_socket.sendto(message.encode(), (ip, port))
            data1, client_address1 = client_socket.recvfrom(1024)
            recdata = data1.decode()
            os.system('cls')
            print(f"Temp data: {recdata}")
        except socket.error as emsg:
            print("Error sending message. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
            sys.exit()

except Exception as e:
    print("An error occurred:", e)