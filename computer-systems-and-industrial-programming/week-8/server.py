import socket
from repository import MovieRepository


HOST = '0.0.0.0'
PORT = 8080
API_KEY = 'a8e10d85'
rep = MovieRepository(api_key=API_KEY)


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
            method, fullpath, _ = request.split(' ', 2)
            if '?' in fullpath:
                path, query = fullpath.split('?', 1)
            else:
                path = fullpath
                query = ""
        except ValueError:
            client.close()
            continue

        params = {}
        if query:
            for pair in query.split('&'):
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    params[key] = value

        if path == '/':
            response =  rep.index()
        elif path == '/online-movies':
            response = rep.online_movies()
        elif path == '/api/movies':
            response = rep.get_movies()
        elif path == '/api/search':
            search_query = params.get('search', '')
            response = rep.search(search_query)
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

