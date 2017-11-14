from enum import Enum


class Token(Enum):
    WORD = 0
    STAR = 1
    COMMA = 2
    END = 3
    EMPTY = 4


class LexicalAnalyzer:
    def __init__(self, IS):
        self.curPos = 0
        self.IS = IS
        self.curChar = None
        self.nextChar()
        self.curToken = None
        self.curWord = ''

    def isBlank(self, c):
        return c == " " or c == "\r" or c == "\n" or c == "\t" or c == ";"

    def nextChar(self):
        self.curPos += 1
        self.curChar = self.IS.read(1)
        print(self.curChar)

    def nextToken(self):
        s = ""
        if self.curChar == ";":
            self.curToken = Token.END
            self.nextChar()
            return
        while self.isBlank(self.curChar):
            self.nextChar()
        if self.curChar == ",":
            self.curToken = Token.COMMA
            self.nextChar()
            return
        if self.curChar == '':
            self.curToken = Token.EMPTY
            return
        star = self.curChar == "*"
        while self.curChar != "," and self.curChar != '' and not self.isBlank(self.curChar):
            s += self.curChar
            self.nextChar()
            if star and self.curChar != "*":
                break
        if s[0] == '*':
            self.curToken = Token.STAR
        else:
            self.curToken = Token.WORD
        self.curWord = s


if __name__ == "__main__":
    l = LexicalAnalyzer(open("test", "r"))
    t = []
    while True:
        l.nextToken()
        t.append((l.curToken, l.curWord))
        if l.curToken == Token.END:
            break

    # print(t)