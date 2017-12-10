# Generated from Grammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7(\n\7")
        buf.write("\f\7\16\7+\13\7\3\7\3\7\3\b\3\b\6\b\61\n\b\r\b\16\b\62")
        buf.write("\3\b\5\b\66\n\b\7\b8\n\b\f\b\16\b;\13\b\3\b\3\b\3\b\3")
        buf.write("\t\6\tA\n\t\r\t\16\tB\3\t\3\t\3\n\3\n\7\nI\n\n\f\n\16")
        buf.write("\nL\13\n\3\13\3\13\7\13P\n\13\f\13\16\13S\13\13\2\2\f")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\b\5")
        buf.write("\2\f\f\17\17))\4\2}}\177\177\5\2\13\f\17\17\"\"\3\2C\\")
        buf.write("\5\2\62;C\\c|\3\2c|\2[\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5")
        buf.write("\32\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3")
        buf.write("\2\2\2\17.\3\2\2\2\21@\3\2\2\2\23F\3\2\2\2\25M\3\2\2\2")
        buf.write("\27\30\7/\2\2\30\31\7@\2\2\31\4\3\2\2\2\32\33\7<\2\2\33")
        buf.write("\34\7?\2\2\34\6\3\2\2\2\35\36\7~\2\2\36\b\3\2\2\2\37 ")
        buf.write("\7=\2\2 \n\3\2\2\2!\"\7?\2\2\"\f\3\2\2\2#)\7]\2\2$(\n")
        buf.write("\2\2\2%&\7^\2\2&(\7)\2\2\'$\3\2\2\2\'%\3\2\2\2(+\3\2\2")
        buf.write("\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2\2,-\7_\2\2-")
        buf.write("\16\3\2\2\2.9\7}\2\2/\61\n\3\2\2\60/\3\2\2\2\61\62\3\2")
        buf.write("\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\66\5")
        buf.write("\17\b\2\65\64\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\60")
        buf.write("\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3")
        buf.write("\2\2\2<=\7\177\2\2=>\b\b\2\2>\20\3\2\2\2?A\t\4\2\2@?\3")
        buf.write("\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\b\t\3")
        buf.write("\2E\22\3\2\2\2FJ\t\5\2\2GI\t\6\2\2HG\3\2\2\2IL\3\2\2\2")
        buf.write("JH\3\2\2\2JK\3\2\2\2K\24\3\2\2\2LJ\3\2\2\2MQ\t\7\2\2N")
        buf.write("P\t\6\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\26")
        buf.write("\3\2\2\2SQ\3\2\2\2\13\2\')\62\659BJQ\4\3\b\2\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    REGEXP = 6
    CODE = 7
    WHITESPACE = 8
    NAME = 9
    NAMEPARSER = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "':='", "'|'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "REGEXP", "CODE", "WHITESPACE", "NAME", "NAMEPARSER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "REGEXP", "CODE", 
                  "WHITESPACE", "NAME", "NAMEPARSER" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[6] = self.CODE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            System.out.println("code");
     


