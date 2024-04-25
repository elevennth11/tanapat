import socket, sys, pickle, os

ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port of the server: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

full_msg = ""
while True:
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
        s.sendall(str.encode(message))
        serverpassword = s.recv(4096).decode("utf-8")
        print(serverpassword)
        while True:
            if serverpassword != password:
                print("Incorrect password. Please try again.")
                password = input("Enter password: ")
                continue
            else:
                break
        message = (["connect to server",nickname])
        data_string = pickle.dumps(message)
        s.sendall(data_string)
        msg = s.recv(4096).decode("utf-8")
        os.system('cls')
        print(msg)
        temp = []
        humi = []
        while (1):
            message = input("Enter message: ")
            try:
                s.sendall(str.encode(message))
                msg = s.recv(4096)
                data_pack = pickle.loads(msg)
                if data_pack[0] == "temp":
                    print(f"Temp data: {data_pack[1]}")
                    temp.append(data_pack[1])
                    if 25 <= data_pack[1] <= 39:
                        print("Normal")
                    elif data_pack[1] <= 25:
                        print("Cool")
                    elif data_pack[1] >= 40:
                        print("Hot")
                    print(f"Average temp: {sum(temp)/len(temp)}")
                elif data_pack[0] == "humi":
                    print(f"Humi data: {data_pack[1]}")
                    humi.append(data_pack[1])
                    if data_pack[1] <= 50:
                        print("PUMP : ON")
                    elif data_pack[1] >= 50:
                        print("PUMP : OFF")
                    print(f"Average humi: {sum(humi)/len(humi)}")
                elif data_pack[0] == "all":
                    os.system('cls')
                    print(f"All data: {data_pack[1]} Temp: {data_pack[2]} Humi : {data_pack[3]} PUMP STATUS : {data_pack[4]}")
                elif data_pack[0] == "exit":
                    message = input(f"{data_pack[1]}")
                    s.sendall(str.encode(message))
                    if message.upper() == "Y":
                        print(".......Bye Server......")
                        s.close()
                        sys.exit()
                else:
                    print(f"Server Send {data_pack[1]}")
            except socket.error as emsg:
                print("Error sending message. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
                sys.exit()


    except socket.error as emsg:
        print("Error sending message. Error Code : " + str(emsg[0]) + " Message " + emsg[1])
        sys.exit()
