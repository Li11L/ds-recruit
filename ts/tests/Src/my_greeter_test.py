import unittest
from src.my_greeter import MyGreeter

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)
#   我当前开发环境并没有安装docker，所以测试程序我并没有实际运行过，以下判断仅通过Code Review答出
#   该测试程序在进行结果长度判断前，并没有先验证greeting()函数的返回值是否为字符串，而不是undefined或是null等结果
#   如果想要更完整的测试，可以再添加对greeting()函数的返回值进行判断结果是否正确

    def test_greeting(self):
        self.assertTrue(len(self._my_greeter.greeting())>0)

if __name__ == '__main__':
    unittest.main()
