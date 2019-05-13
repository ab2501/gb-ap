from socket import *
import sys
import json
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='')
    parser.add_argument('-p', '--port', default='7777')
    return parser


response_dict = {
    'ok': {
        "response": 200,
        "alert": 'Ok'
    },
    'error': {
        'response': 400,
        'error': 'Некорректный запрос'
    }
}


action_dict = ['presence']


def request_handler(request):
    try:
        if request['action'] in action_dict:
            return json.dumps(response_dict['ok'], indent=4).encode(encoding='utf-8')
        else:
            return json.dumps(response_dict['error'], indent=4).encode(encoding='utf-8')
    except KeyError:
        return json.dumps(response_dict['error'], indent=4).encode(encoding='utf-8')


def run_server(address, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(1)
    print(f'Сервер запущен на {address}:{port}')

    while True:
        client, addr = s.accept()
        print(f"Получен запрос на соединение от {str(addr)}")
        data = client.recv(1000000)
        request = json.loads(data.decode('utf-8'))
        response_data = request_handler(request)
        client.send(response_data)
        print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
        client.close()


def main():
    namespace = create_parser().parse_args(sys.argv[1:])
    run_server(namespace.address, int(namespace.port))


if __name__ == "__main__":
    main()
