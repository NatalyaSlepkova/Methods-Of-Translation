grammar Grammar;

main : begin (line)*;

begin : '->' NAME ';';

line : parserRules | lexerRules;

parserRules : NAMEPARSER ':=' (NAME | NAMEPARSER) CODE? ('|' (NAME | NAMEPARSER) CODE?)* ';';

lexerRules : NAME '=' REGEXP ';';

REGEXP : '[' (~('\''|'\r' | '\n') | '\\\'')* ']';
CODE : '{' (~[{}]+ CODE?)* '}' {System.out.print("code");};
//CODE : NAME;
WHITESPACE : [ \t\r\n] + -> skip;
NAME : [A-Z][a-zA-Z0-9]*;
NAMEPARSER : [a-z][a-zA-Z0-9]*;