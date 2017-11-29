grammar Grammar;

@header {
	import java.util.Set;
	import java.util.HashSet;
}

@members {
	Set<String> S = new HashSet<>();
    final String tab = "    ";
    int count = 0;
    void writeTab() {
        for (int i = 0; i < count; i++) {
            System.out.print(tab);
        }
    }
    Boolean need = false;
}

main
	@init {
		System.out.println("int main() {");
		++count;
	}

	@after {
		--count;
		System.out.println("}");
	}

	: (line)*;

line
	: assignment | ifclause | input | output | cyclewhile;

cyclewhile returns [String s]
    @init {
        writeTab();
        System.out.print("while (");
        ++count;
    }
    @after {
        --count;
        writeTab();
        System.out.println("}");
    }
    :'while' '(' condition ')' '{'
    {
        System.out.println(')' + "{");
    }
    (line)+ '}';

assignment returns [String s]
	@after {
	    if (need == true) {
            writeTab();
            need = false;
        }
		System.out.println($s + ";");
	}
	:VAR ' = ' expr {
		$s = $VAR.text + " = " + $expr.s;
		if (!S.contains($VAR.text)) {
			S.add($VAR.text);
			writeTab();
			System.out.print("int ");
		}
		else
		    need = true;
	};

input returns [String s]
    @after {
        writeTab();
        System.out.println("scanf(\"%d\", &" + $s + ");");
    }
    :'<< ' VAR {
        $s = $VAR.text;
        if (!S.contains($VAR.text)) {
            S.add($VAR.text);
            writeTab();
            System.out.println("int " + $s + ";");
        }
    };

output returns [String s]
    @after {
        writeTab();
        System.out.println("printf(\"%d\", " + $s + ");");
    }
    :'>> ' factor {
        $s = $factor.s;
    };

ifclause 
	@init {
	    writeTab();
		System.out.print("if (");
		++count;
	}

	@after {
		--count;
	    writeTab();
		System.out.println("}");
	}

	: 'if' '('condition')''{'
    {
        System.out.println(')' + "{");
    }
    (line)+'}';

condition returns [String s]
	@after {
		System.out.print($s);
	}
	: l = expr '<' r = expr {$s = $l.s + " < " + $r.s;}
    | l = expr '<=' r = expr {$s = $l.s + " <= " + $r.s;}
    | l = expr '>' r = expr {$s = $l.s + " > " + $r.s;}
    | l = expr '>=' r = expr {$s = $l.s + " >= " + $r.s;}
    | l = expr '<>' r = expr {$s = $l.s + " <> " + $r.s;}
    | l = expr '==' r = expr {$s = $l.s + " == " + $r.s;};

expr returns [String s]
    : {$s = "";}
    | factor {$s = $factor.s;}
	| addsub {$s = $addsub.s;}
	| mod {$s = $mod.s;}
	| multdiv {$s = $multdiv.s;};

mod returns [String s]
    : factor ' mod ' expr {$s = $factor.s + " mod " + $expr.s;};

multdiv returns [String s]
	: {$s = "";}
	| factor {$s = $factor.s;}
	| factor '*' multdiv {$s = $factor.s + " * " + $multdiv.s;}
	| factor '/' multdiv {$s = $factor.s + " / " + $multdiv.s;};

addsub returns [String s]
	: {$s = "";}
	| factor {$s = $factor.s;}
	| multdiv ' + ' expr {$s = $multdiv.s + " + " + $expr.s;}
	| multdiv ' - ' expr {$s = $multdiv.s + " - " + $expr.s;};

factor returns [String s]
	: unit {$s = $unit.s;}
	| '-' unit {$s = "-" + $unit.s;};

unit returns [String s]
	: NUMBER {$s = $NUMBER.text;}
	| VAR {$s = $VAR.text;}
	| '(' expr ')' {$s = "(" + $expr.s + ")";};

WHITESPACE : [ \t\r\n] + -> skip;
NUMBER : [0-9]+;
VAR : [_a-zA-Z][_a-zA-Z0-9]*;
