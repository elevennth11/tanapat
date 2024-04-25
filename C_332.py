import socket, pickle
import sys
import os

ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port of the server: "))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ip, port))

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
    client_socket.send(message.encode(), (ip, port))
    data, client_address = client_socket.recv(4096)
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
    client_socket.send(data_string, (ip, port))
    os.system('cls')
    data1, client_address1 = client_socket.recv(4096)
    recdata = data1.decode()
    print(recdata)
    temp = []
    humi = []
    while (1):
        message = input("Enter Temp : ")
        try:
            client_socket.send(message.encode(), (ip, port))
            data1, client_address1 = client_socket.recv(4096)
            recdata = pickle.loads(data1)
            if recdata[0] == "temp":
                print(f"Temp data: {recdata[1]}")
                temp.append(recdata[1])
                if 25 <= recdata[1] <= 39:
                    print("Normal")
                elif recdata[1] <= 25:
                    print("Cool")
                elif recdata[1] >= 40:
                    print("Hot")
                print(f"Average temp: {sum(temp)/len(temp)}")
            elif recdata[0] == "humi":
                print(f"Humidity data: {recdata[1]}")
                humi.append(recdata[1])
                if recdata[1] <= 50:
                    print("PUMP : ON")
                elif recdata[1] >= 50:
                    print("PUMP : OFF")
                print(f"Average humidity: {sum(humi)/len(humi)}")
            elif recdata[0] == "all":
                os.system('cls')
                print(f"All data: {recdata[1]} Temp: {recdata[2]} Humi : {recdata[3]} PUMP STATUS : {recdata[4]}")
            elif recdata[0] == "exit":
                message = input(f"{recdata[1]}")
                client_socket.send(message.encode(), (ip, port))
                if message == "y":
                    print(".......Bye Server......")
                    client_socket.close()
                    sys.exit()
            else:
                print(f"Data {recdata[1]}")
        except socket.error as emsg:
            print("Error sending message. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
            sys.exit()

except Exception as e:
    print("An error occurred:", e)