import unittest
import client



class TestParsing(unittest.TestCase):
    def testNumberParameters(self):
        self.assertEqual(len(client.parsing()), 2, 'Doesn''t contain two parameters needed to start')
        print("test 1")
        pass

    def testParametersAreNotNone(self):
        self.assertNotEqual(client.parsing()[0], None, 'IP address could not be None or Null')
        self.assertNotEqual(client.parsing()[1], None, 'Port number could not be None or Null')
        print("test 2")
        pass


class TestConnect(unittest.TestCase):
    def testDataAreNotNone(self):
        print("test 3")
        params = client.parsing()
        runresult = client.myconnect(params)
        self.assertNotEqual(runresult, None, 'data could not be None or Null')
        pass



if __name__ == '__main__':
    unittest.main()
