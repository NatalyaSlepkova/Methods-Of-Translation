# Generated from Grammar.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7")
        buf.write("\2\17\n\2\f\2\16\2\22\13\2\3\3\3\3\3\3\3\4\3\4\5\4\31")
        buf.write("\n\4\3\5\3\5\3\5\3\5\5\5\37\n\5\3\5\3\5\3\5\5\5$\n\5\7")
        buf.write("\5&\n\5\f\5\16\5)\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\2\2")
        buf.write("\7\2\4\6\b\n\2\3\3\2\13\f\2\60\2\f\3\2\2\2\4\23\3\2\2")
        buf.write("\2\6\30\3\2\2\2\b\32\3\2\2\2\n,\3\2\2\2\f\20\5\4\3\2\r")
        buf.write("\17\5\6\4\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20")
        buf.write("\21\3\2\2\2\21\3\3\2\2\2\22\20\3\2\2\2\23\24\7\3\2\2\24")
        buf.write("\25\7\13\2\2\25\5\3\2\2\2\26\31\5\b\5\2\27\31\5\n\6\2")
        buf.write("\30\26\3\2\2\2\30\27\3\2\2\2\31\7\3\2\2\2\32\33\7\f\2")
        buf.write("\2\33\34\7\4\2\2\34\36\t\2\2\2\35\37\7\t\2\2\36\35\3\2")
        buf.write("\2\2\36\37\3\2\2\2\37\'\3\2\2\2 !\7\5\2\2!#\t\2\2\2\"")
        buf.write("$\7\t\2\2#\"\3\2\2\2#$\3\2\2\2$&\3\2\2\2% \3\2\2\2&)\3")
        buf.write("\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7")
        buf.write("\6\2\2+\t\3\2\2\2,-\7\13\2\2-.\7\7\2\2./\7\b\2\2/\13\3")
        buf.write("\2\2\2\7\20\30\36#\'")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "':='", "'|'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "REGEXP", "CODE", "WHITESPACE", 
                      "NAME", "NAMEPARSER" ]

    RULE_main = 0
    RULE_begin = 1
    RULE_line = 2
    RULE_parserRules = 3
    RULE_lexerRules = 4

    ruleNames =  [ "main", "begin", "line", "parserRules", "lexerRules" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    REGEXP=6
    CODE=7
    WHITESPACE=8
    NAME=9
    NAMEPARSER=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def begin(self):
            return self.getTypedRuleContext(GrammarParser.BeginContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.LineContext)
            else:
                return self.getTypedRuleContext(GrammarParser.LineContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = GrammarParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.begin()
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.NAME or _la==GrammarParser.NAMEPARSER:
                self.state = 11
                self.line()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BeginContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_begin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin" ):
                listener.enterBegin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin" ):
                listener.exitBegin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBegin" ):
                return visitor.visitBegin(self)
            else:
                return visitor.visitChildren(self)




    def begin(self):

        localctx = GrammarParser.BeginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_begin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(GrammarParser.T__0)
            self.state = 18
            self.match(GrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parserRules(self):
            return self.getTypedRuleContext(GrammarParser.ParserRulesContext,0)


        def lexerRules(self):
            return self.getTypedRuleContext(GrammarParser.LexerRulesContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = GrammarParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.NAMEPARSER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.parserRules()
                pass
            elif token in [GrammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.lexerRules()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParserRulesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMEPARSER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NAMEPARSER)
            else:
                return self.getToken(GrammarParser.NAMEPARSER, i)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NAME)
            else:
                return self.getToken(GrammarParser.NAME, i)

        def CODE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.CODE)
            else:
                return self.getToken(GrammarParser.CODE, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_parserRules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParserRules" ):
                listener.enterParserRules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParserRules" ):
                listener.exitParserRules(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRules" ):
                return visitor.visitParserRules(self)
            else:
                return visitor.visitChildren(self)




    def parserRules(self):

        localctx = GrammarParser.ParserRulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parserRules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GrammarParser.NAMEPARSER)
            self.state = 25
            self.match(GrammarParser.T__1)
            self.state = 26
            _la = self._input.LA(1)
            if not(_la==GrammarParser.NAME or _la==GrammarParser.NAMEPARSER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CODE:
                self.state = 27
                self.match(GrammarParser.CODE)


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__2:
                self.state = 30
                self.match(GrammarParser.T__2)
                self.state = 31
                _la = self._input.LA(1)
                if not(_la==GrammarParser.NAME or _la==GrammarParser.NAMEPARSER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.CODE:
                    self.state = 32
                    self.match(GrammarParser.CODE)


                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(GrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LexerRulesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def REGEXP(self):
            return self.getToken(GrammarParser.REGEXP, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_lexerRules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexerRules" ):
                listener.enterLexerRules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexerRules" ):
                listener.exitLexerRules(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerRules" ):
                return visitor.visitLexerRules(self)
            else:
                return visitor.visitChildren(self)




    def lexerRules(self):

        localctx = GrammarParser.LexerRulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lexerRules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GrammarParser.NAME)
            self.state = 43
            self.match(GrammarParser.T__4)
            self.state = 44
            self.match(GrammarParser.REGEXP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





