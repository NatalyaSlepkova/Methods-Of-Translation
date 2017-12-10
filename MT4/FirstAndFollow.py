from antlr4 import*
from antlr.GrammarParser import GrammarParser
from antlr.GrammarLexer import GrammarLexer
from antlr.GrammarVisitor import GrammarVisitor
import org.antlr.v4.runtime.tree.ParseTree

class FirstAndFollow:
    input = open("InGrammar", "r")
    lexer = GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = ParseTreeVisitor

    changed = True
    while changed == True:
        changed = False





