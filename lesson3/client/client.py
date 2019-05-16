import sys
from socket import *
import time
import json
import argparse


request_data = {
    "action": "presence",
    "time": int(time.time()),
    "type": "status",
    "user": {
        "account_name":  "C0deMaver1ck",
        "status":      "Yep, I am here!"
    }
}


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', default='localhost')
    parser.add_argument('port', default='7777')
    return parser


def create_socket_connection():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect()
    return s


def get_request_data_to_bytes(data):
    return json.dumps(data, indent=4).encode(encoding='utf-8')


def send_request(s, data):
    s.send(data)
    response = s.recv(1000000)
    response_data = response.decode(encoding='utf-8')
    return response_data


def main():
    namespace = create_parser().parse_args(sys.argv[1:])
    s = create_socket_connection(namespace.address, int(namespace.port))
    data = get_request_data_to_bytes(request_data)
    s.close()
    response = send_request(s, data)
    print(f"Ответ от сервера:{response}")


if __name__ == "__main__":
    main()
