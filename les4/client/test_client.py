import json
import unittest
import lesson3.client.client as client
import lesson3.server.server as server


def assert_equal(x, y):
    assert x == y, "{} != {}".format(x, y)



class ClientSocketMock:
    def send(self, data):
        self.data = data

    def recv(self, number):
        request = json.loads(self.data.decode('utf-8'))
        return server.request_handler(request)


class TestClient(unittest.TestCase):
    client_socket = ClientSocketMock()

   
    def test_convert_dictionary_to_bytes(self):
        test_data = {'test_key': 'test_value'}
        b = client.get_request_data_to_bytes(test_data)
        assert(b, b'{\n    "test_key": "test_value"\n}')

  
    
    def test_send_data_correct(self):
        request_data = client.get_request_data_to_bytes(client.request_data)
        response = client.send_request(self.client_socket, request_data)
        code = json.loads(response)['response']
        assert_equal(code, 200)


    def test_send_data_incorrect(self):
        request_data = client.get_request_data_to_bytes({'test_key': 'test_value'})
        response = client.send_request(self.client_socket, request_data)
        code = json.loads(response)['response']
        assert_equal(code, 400)

    #
    def test_send_data_with_unknown_action(self):
        request_data = client.get_request_data_to_bytes({'action': 'unknown_action'})
        response = client.send_request(self.client_socket, request_data)
        code = json.loads(response)['response']
        assert_equal(code, 400)


if __name__ == '__main__':
    unittest.main()
