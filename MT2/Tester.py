import unittest
from io import StringIO
from Parse import Parser
from MyException import ParseException
import LexicalAnalyzer

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.lines = []

    def test_simple_right(self):
        self.lines.append('int a;')
        self.lines.append('string abc;')
        self.lines.append('bool abc, def, ghi;')
        for s in self.lines:
            try:
                self.parser.parse(StringIO(s))
            except ParseException as PE:
                self.fail(PE.message)

    def test_simple_wrong(self):
        self.lines.append('int')
        self.lines.append('string a,')
        self.lines.append('bool abc')
        for s in self.lines:
            with self.assertRaises(ParseException):
                self.parser.parse(StringIO(s))

    def test_average_right(self):
        self.lines.append('int ***abc, *def;')
        self.lines.append('string a, *b, **c;')
        for s in self.lines:
            try:
                self.parser.parse(StringIO(s))
            except ParseException as PE:
                self.fail(PE.message)

    def test_average_wrong(self):
        self.lines.append('bool *')
        self.lines.append('int *a,')
        self.lines.append('string ***abc, ***')
        for s in self.lines:
            with self.assertRaises(ParseException):
                self.parser.parse(StringIO(s))

if __name__ == "__main__":
    unittest.main()