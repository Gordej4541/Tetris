import socket
import time


# Добавь в код сервера функцию find() из игры Бактерии.Пусть она принимает полученный от игрока пакет и
# возвращает обрезанные значения — без < и >.

# У нашего приложения нет иконки в заголовке.Исправь это.
#
# Создай репозиторий в своем GitHub,
# подключи проект к нему и закоммить туда свой код.

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('192.168.0.225', 10000))

main_socket.setblocking(False)
main_socket.listen(5)
print("Сокет создался")


def find(vector: str):
    first = None
    for num, sign in enumerate(vector):
        if sign == "<":
            first = num
        if sign == ">" and first is not None:
            second = num
            result = vector[first + 1:second]  # Поменяли
            return result
    return ""

players = []
run = True
while run:
    try:
        new_socket, addr = main_socket.accept()
        print("Подключился", addr)
        players.append(new_socket)
    except BlockingIOError:
        pass

    for sock in players:
        try:
            data = sock.recv(1024).decode()
            print("Получил", data)
            sock.close()
            run = False
            break
        except:
            pass

    time.sleep(1)