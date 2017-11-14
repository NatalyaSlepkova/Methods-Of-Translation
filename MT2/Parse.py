from LexicalAnalyzer import Token
from LexicalAnalyzer import LexicalAnalyzer
from MyException import ParseException
from io import StringIO
import Tester

BoolToken = False

class Tree:
    def __init__(self, s, a=None):
        self.name = s
        self.children = a

class Parser:
    def __init__(self):
        self.LA = None

    def parse(self, IS):
        self.LA = LexicalAnalyzer(IS)
        self.LA.nextToken()
        return self.S()
    #
    # def next(self, t):
    #     self.LA.nextToken()
    #     return Tree(t.name)

    def S(self):
        token = self.LA.curToken
        children = []
        if token == Token.WORD:
            children.append(self.Word())
            children.append(self.VARLIST())
            return Tree('S', children)
        else:
            raise ParseException('Type not found')


    def Word(self):
        token = self.LA.curToken
        if token == Token.WORD:
            global BoolToken
            BoolToken = True
            t = Tree(self.LA.curWord)
            self.LA.nextToken()
            return t
        else:
            raise ParseException('Word not found')

    def Star(self):
        token = self.LA.curToken
        if token == Token.STAR:
            global BoolToken
            BoolToken = True
            t = Tree(self.LA.curWord)
            self.LA.nextToken()
            return t
        else:
            raise ParseException('Star not found')


    def VARLIST(self):
        token = self.LA.curToken
        children = []
        global BoolToken
        BoolToken = False
        if token == Token.END:
            return Tree('SEMICOLON')
        if token == Token.STAR:
            star = self.Star()
            children.append(star)
            if self.LA.curToken != Token.WORD:
                raise ParseException('Word not found after Star')
        if self.LA.curToken == Token.WORD:
            word = self.Word()
            children.append(word)
            if self.LA.curToken == Token.COMMA:
                children.append(Tree('COMMA'))
                self.LA.nextToken()
            elif self.LA.curToken != Token.END:
                raise ParseException('Token not found after Word')
        if BoolToken == False:
            raise ParseException('A token was expected but not found')
        varlist = self.VARLIST()
        children.append(varlist)
        return Tree('VARLIST', children)

f = open("tree.txt", "w")

def dfs(v, tab=''):
    global f
    if v.name != 'S':
        print(tab, end=' ', file=f)
    print(v.name, file=f)
    if v.children != None:
        tab += '-->'
        for k in v.children:
            dfs(k, tab)

if __name__ == "__main__":
    try:
        # parser = Parser(open("test", "r"))
        # T = Parser().parse(open("test", "r"))
        s = "int a;"
        T = Parser().parse(StringIO(s))
    except ParseException as PE:
        print(PE.message, file=f)
    else:
        dfs(T)
    f.close()
