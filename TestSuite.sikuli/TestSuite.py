import HTMLTestRunner
import unittest
from sikuli import *

class TestDemo(unittest.TestCase):
    def testA(self):
        openApp('notepad.exe')
        wait(2)
        type('Testando a funcao type do sikuli, e depois savlar o arquivo.')
        wait(1)
        type("s", Key.CTRL)
        type(Key.HOME + Key.DELETE + 'Teste_Sikuli' + Key.ENTER)
        self.assertTrue(True)
    def testB(self):
        assert False

def suite():
    suite = unittest.TestSuite()
    # TestDemo
    suite.addTest(TestDemo('testA'))
    suite.addTest(TestDemo('testB'))
    return suite

if __name__ == '__main__':
    suite = suite()
    unittest.TextTestRunner(verbosity=2)
    output = open('./TestSuite.sikuli/result.html', 'w')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=output,
        title='Testestestsest',
        description='asdfasdinfoasdinf'
    )
    runner.run(suite)