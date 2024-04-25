import socket
from datetime import datetime
  
def capitalize_name(nickname):
    return nickname.capitalize()

port = 9876

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    server_socket.bind(('0.0.0.0', port))
    print("Server is listening on port", port)

    while True:
        
        data, server_address = server_socket.recvfrom(1024)
        command = data.decode().lower()
        print("Received data from", server_address, ":", data.decode())
        nickname = data.decode()
        capitalized_nickname = capitalize_name(nickname)
        response = f"Hello {capitalized_nickname} [{datetime.now()}]"
        server_socket.sendto(response.encode(), server_address)

except Exception as e:
    print("An error occurred:", e)

finally:
    print('closing socket')
    server_socket.close()