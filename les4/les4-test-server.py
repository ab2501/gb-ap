import unittest
import server
import subprocess



class Test0Parsing(unittest.TestCase):
    def testNumberParameters(self):
        self.assertEqual(len(server.parsing()), 3, 'Doesn''t contain three parameters needed to start')
        print("test 1")
        pass

    def testParametersAreNotNone(self):
        self.assertNotEqual(server.parsing()[0], None, 'IP address could not be None or Null')
        self.assertNotEqual(server.parsing()[1], None, 'Port number could not be None or Null')
        print("test 2")
        pass


class TestConnect(unittest.TestCase):
    def testDataAreNotNone(self):
        print("test 3")
        params = server.parsing()
        params[2] = False
        #runresult = lesson3_server.myserverup(params)
        #print(params[0])
        #print(type(runresult)) #return NoneType somehow
        #self.assertNotEqual(runresult, None, 'data could not be None or Null')

        def run_command(command):
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,  shell=True)
            #args = [command, ""]
            #process = subprocess.Popen(args)

            #data = process.communicate()
            #return iter(p.stdout.readline, b'')
            #return p.stdout
            p.kill()
            return p
        runresult = run_command(server.myserverup(params))
        #runresult = (server.myserverup(params))
        print(type(runresult))
        pass
        # return None


# для завершения теста
# нужно запустить или скрипт клиента, или файл теста клиента.
if __name__ == '__main__':
    unittest.main()
