import unittest
import lesson3.server.server as server


def assert_equal(x, y):
    assert x == y, "{} != {}".format(x, y)


class TestServer(unittest.TestCase):
    def test_get_success_response(self):
        success_response = server.action_dict['ok']
        assert_equal(success_response['response'], 200)

    def test_get_error_response(self):
        success_response = server.action_dict['error']
        assert_equal(success_response['response'], 400)

  


if __name__ == '__main__':
    unittest.main()
