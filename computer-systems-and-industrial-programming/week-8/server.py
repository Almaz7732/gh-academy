import socket
from repository import MovieRepository

rep = MovieRepository()

HOST = '0.0.0.0'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(3)

print(f"Server start: http://localhost:{PORT}")

try:
    while True:
        client, addr = server.accept()
        request = client.recv(1024).decode()

        if not request:
            client.close()
            continue

        try:
            method, path, _ = request.split(' ', 2)
        except ValueError:
            client.close()
            continue

        if path == '/':
            response =  rep.index()
        elif path == '/api/movies':
            response = rep.get_movies()
        elif path == '/about':
            response = rep.about()
        else:
            content = "<h1>404 Not Found</h1>"
            response = rep.response(content, 'text/html')

        client.sendall(response.encode("utf-8"))
        client.close()
except:
    server.close()
    print("Server closed.")

