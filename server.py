import socket
import time

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)          #создаём socket
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)    #отключили покетирование
main_socket.bind(('localhost',10000))       #устанавливаем IP адрес и порт
main_socket.setblocking(False)      #предотвращаем завершение
main_socket.listen(5)
print('socket создан')

players = []
#работа сервера
while True:
    try:
        #проверим желание войти в игру
        new_socket, addr = main_socket.accept()
        print('Подключился', addr)
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError:
       pass
    for soc in players:
        try:
            data = soc.recv(1024).decode()
            print('Сообщение получено', data)
        except:
            pass
    time.sleep(1)
