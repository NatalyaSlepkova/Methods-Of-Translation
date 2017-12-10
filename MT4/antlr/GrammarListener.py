# Generated from Grammar.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#main.
    def enterMain(self, ctx:GrammarParser.MainContext):
        pass

    # Exit a parse tree produced by GrammarParser#main.
    def exitMain(self, ctx:GrammarParser.MainContext):
        pass


    # Enter a parse tree produced by GrammarParser#begin.
    def enterBegin(self, ctx:GrammarParser.BeginContext):
        pass

    # Exit a parse tree produced by GrammarParser#begin.
    def exitBegin(self, ctx:GrammarParser.BeginContext):
        pass


    # Enter a parse tree produced by GrammarParser#line.
    def enterLine(self, ctx:GrammarParser.LineContext):
        pass

    # Exit a parse tree produced by GrammarParser#line.
    def exitLine(self, ctx:GrammarParser.LineContext):
        pass


    # Enter a parse tree produced by GrammarParser#parserRules.
    def enterParserRules(self, ctx:GrammarParser.ParserRulesContext):
        pass

    # Exit a parse tree produced by GrammarParser#parserRules.
    def exitParserRules(self, ctx:GrammarParser.ParserRulesContext):
        pass


    # Enter a parse tree produced by GrammarParser#lexerRules.
    def enterLexerRules(self, ctx:GrammarParser.LexerRulesContext):
        pass

    # Exit a parse tree produced by GrammarParser#lexerRules.
    def exitLexerRules(self, ctx:GrammarParser.LexerRulesContext):
        pass


