# Femtolang

This is a learning project inspired from [teenytiny compiler](https://austinhenley.com/blog/teenytinycompiler1.html) by [@AZHenley](https://github.com/AZHenley).

Femtolang is a simple regular language to evaluate expressions. 

> **_NOTE:_** I just implemented parsing for now.

## Quickstart
You can parse femtolang by running:

```
python3 cli.py
```

### Example

```
> 1 + 1 = 2 -> 3
ok: exp
```

## Femtolang's grammar

This is the (left-regular or bottom-up) grammar in [Backus-Naur form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form):

```bnf
<exp>  ::= <exp> " " op " " d
<exp>  ::= <bool> " -> " d
<exp>  ::= d
op     ::= "+" | "-" | "*" | "/"

<bool> ::= <exp> " " cmp " " d
cmp    ::= "<" | ">" | "=" | ">=" | "<="

d      ::= "0" | "1" | "2" | "3" | "4"
d      ::= "5" | "6" | "7" | "8" | "9"
```

## Lexer/Parser

The lexer/parser is implemented as a pure [DFA (Deterministic Finite Automaton)](https://en.wikipedia.org/wiki/Deterministic_finite_automaton), specifically a [Mealy machine](https://en.wikipedia.org/wiki/Mealy_machine).

Picolang's lexer is the same as the parser due to the fact that the grammar is entirely a Chomsky's level 3 (left-regular grammar).

