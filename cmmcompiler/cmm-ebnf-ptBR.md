# EBNF da Linguagem `C-`

```ebnf
programa : lista-de-declaracoes
lista-de-declaracoes : lista-de-declaracoes declaracao | declaracao
declaração : declaracao-de-var | declaracao-de-funcao
declaracao-de-var : especificador-de-tipo ID ; | especificador-de-tipo ID [ NUM ] ;
especificador-de-tipo : int | void
declaracao-de-funcao : especificador-de-tipo ID ( params ) statement-composto
params : lista-de-params | void
lista-de-params : lista-de-params , param | param
param : especificador-de-tipo ID | especificador-de-tipo ID [ ]
statement-composto : { declaracoes-locais lista-de-statements }
declaracoes-locais : declaracoes-locais declaracao-de-var | vazio
lista-de-statements : lista-de-statements statement | vazio
statement : statement-expressao | statement-composto | statement-selecao | statement-iteração | statement-retorno
statement-expressao : expressao ; | ;
statement-selecao : if ( expressao ) statement | if ( expressao ) statement else statement
statement-iteração : while ( expressao ) statement
statement-retorno : return ; | return expressao ;
expressao : var = expressao | expressao-simples
var : ID | ID [ expressao ]
expressao-simples : expressao-aditiva operador-relacional expressao-aditiva | expressao-aditiva
operador-relacional : <= | < | > | >= | == | !=
expressao-aditiva : expressao-aditiva operador-soma termo | termo
operador-soma : + | -
termo : termo operador-multiplicacao fator | fator
operador-multiplicacao : * | /
fator : ( expressao ) | var | ativacao | NUM
ativacao : ID ( args )
args : lista-de-argumentos | vazio
lista-de-argumentos : lista-de-argumentos , expressao | expressao
```