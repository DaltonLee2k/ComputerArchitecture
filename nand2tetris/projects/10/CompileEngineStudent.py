import sys
from Tokenizer import Tokenizer

class CompileEngine:
    def __init__(self,T):
        pass

    # The following are suggested helper functions.
    # You need not use them if you have other ideas 
    # about getting this done.

    def printXMLToken(self):
        pass

    def checkToken(self,tokens):
        """
        Checks to see if the current token found in 
        self.T.getToken()
        is in the tuple tokens.
        Print the token in appropriate XML if it is.
        Give an error message and halt if it is not.
        """

    def checkType(self,expected_types):
        """
        Checks to see if the current type found in 
        self.T.getType()
        is in the tuple expected types.
        Print the token in appropriate XML and 
        advance to the next token if it is.
        Give an error message and halt if it is not.
        """


    # The following are the compile functions that need to 
    # be implemented. compileExpression has been withheld for a
    # future assignment

    def compileClass(self):
        """
        Compiles <class> :=
            'class' <class-name> '{' <class-var-dec>* <subroutine-dec>* '}'

        The tokenizer is expected to be positionsed at the beginning of the
        file.
        """
        print("<class>")
        print("</class>")

    def compileClassVarDec(self):
        """
        Compiles <class-var-dec> :=
            ('static' | 'field') <type> <var-name> (',' <var-name>)* ';'
        """
        print("<classVarDec>")
        print("</classVarDec>")


    def compileSubroutine(self):
        """
        Compiles <subroutine-dec> :=
            ('constructor' | 'function' | 'method') ('void' | <type>)
            <subroutine-name> '(' <parameter-list> ')' <subroutine-body>

        ENTRY: Tokenizer positioned on the initial keyword.
        EXIT:  Tokenizer positioned after <subroutine-body>.
        """
        print("<subroutineDec>")
        print("</subroutineDec>")

    def compileParameterList(self):
        """
        Compiles <parameter-list> :=
            ( <type> <var-name> (',' <type> <var-name>)* )?

        ENTRY: Tokenizer positioned on the initial keyword.
        EXIT:  Tokenizer positioned after <subroutine-body>.
        """
        print("<parameterList>")
        print("</parameterList>")


    def compileSubroutineBody(self):
        """
        Compiles <subroutine-body> :=
            '{' <var-dec>* <statements> '}'
        """
        print("<subroutineBody>")
        print("</subroutineBody>")


    def compileVarDec(self):
        """
        Compiles <var-dec> :=
            'var' <type> <var-name> (',' <var-name>)* ';'
        """
        print("<varDec>")

        print("</varDec>")

    def compileStatements(self):
        """
        Compiles <statements> := (<let-statement> | <if-statement> |
            <while-statement> | <do-statement> | <return-statement>)*
        """
        print("<statements>")
        print("</statements>")

    def compileLet(self):
        """
        Compiles <let-statement> :=
            'let' <var-name> ('[' <expression> ']')? '=' <expression> ';'
        """
        print("<letStatement>")
        print("</letStatement>")

    def compileDo(self):
        """
        Compiles <do-statement> := 'do' <subroutine-call> ';'

        <subroutine-call> := (<subroutine-name> '(' <expression-list> ')') |
            ((<class-name> | <var-name>) '.' <subroutine-name> '('
            <expression-list> ')')

        <*-name> := <identifier>
        """
        print("<doStatement>")
        print("</doStatment>")


    def compileIf(self):
        """
        Compiles <if-statement> :=
            'if' '(' <expression> ')' '{' <statements> '}' ( 'else'
            '{' <statements> '}' )?
        """
        print("<ifStatement>")
        print("</ifStatement>")

    def compileWhile(self):
        """
        Compiles <while-statement> :=
        'while' '(' <expression> ')' '{' <statements> '}'
        """
        print("<whileStatement>")

        print("</whileStatement>")

    def compileDo(self):
        """
        Compiles <do-statement> := 'do' <subroutine-call> ';'

        <subroutine-call> := (<subroutine-name> '(' <expression-list> ')') |
            ((<class-name> | <var-name>) '.' <subroutine-name> '('
            <expression-list> ')')

        <*-name> := <identifier>
        """
        print("<doStatement>")
      
        print("</doStatement>")

    def compileReturn(self):
        """
        Compiles <return-statement> :=
            'return' <expression>? ';'
        """
        print("<returnStatement>")
        
        print("</returnStatement>")


# The following are not LL(1) and are not part of the initial assignment

    def compileExpression(self):
        """
        Compiles <expression> :=
            <term> (op <term>)*
        """
        print("<expression>")
        print("</expression>")

    def compileExpressionList(self):
        """
        Compiles <expression-list> :=
            (<expression> (',' <expression>)* )?
        """
 
        print("<expressionList>")
        print("</expressionList>")

    def compileTerm(self):
        """
        Compiles a <term> :=
            <int-const> | <string-const> | <keyword-const> | <var-name> |
            (<var-name> '[' <expression> ']') | <subroutine-call> |
            ( '(' <expression> ')' ) | (<unary-op> <term>)
        """
        print("<term>")
        print("</term>")