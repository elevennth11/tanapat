import socket

ip = input("Enter the IP address of the server: ")
port = int(input("Enter the port of the server: "))
password = input("Enter password: ")
nickname = input("Enter your nickname (up to 10 characters): ")

correct_password = "331"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while password != correct_password:
        print("Incorrect password. Please try again.")
        print("Password correct. Proceed to next step.")
        
        if not nickname.isalpha():
            print("Invalid input. Please enter text only.")
            continue
    
        if len(nickname) > 10:
            print("Invalid input. Nickname should not exceed 10 characters.")
            continue

        break
    print(type(password))
    print("Your nickname is:", nickname)

    message = input("Enter message to send: ")
    client_socket.sendto(message.encode(), (ip, port))
    print("Message sent to the server successfully!")

    data, client_address = client_socket.recvfrom(1024)
    print("Received data from server:", data.decode())

    client_socket.close()

except Exception as e:
    print("An error occurred:", e)