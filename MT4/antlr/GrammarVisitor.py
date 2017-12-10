# Generated from Grammar.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#main.
    def visitMain(self, ctx:GrammarParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#begin.
    def visitBegin(self, ctx:GrammarParser.BeginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#line.
    def visitLine(self, ctx:GrammarParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parserRules.
    def visitParserRules(self, ctx:GrammarParser.ParserRulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lexerRules.
    def visitLexerRules(self, ctx:GrammarParser.LexerRulesContext):
        return self.visitChildren(ctx)



del GrammarParser