#!/usr/bin/env python3

from __future__ import annotations

from dfa import DFA, ParseError
from tmap import tmap

RED = "\033[1;31m"
PRP = "\033[0;35m"
BLD = "\033[1m"
NC = "\033[0m"


def parse(input: str):
    dfa = DFA("d", {"exp"}, tmap)

    source = "stdin"
    try:
        state, event, status = any, any, any
        for state, event, status in dfa.parse(input):
            pass

        if status:
            print("ok:", state)
        else:
            print(f"{RED}error{NC}: {BLD}expected `expression`, found `{state}`")
            print(f"  {PRP}-->{NC} {source}")
            print(f" {PRP}  |{NC} ")
            print(f" {PRP}0 |{NC} {RED}{input}{NC}")
            print(f" {PRP}  |{NC} ", end="")
            print(RED + "^" * len(input) + f" this is not a complete expression{NC}")
            print(f" {PRP}  |{NC} ")
            print(f" {PRP}  ={NC} {BLD}help{NC}: try with an arithmetic expression")
            print(
                f" {PRP}  ={NC} {BLD}help{NC}: avoid writing boolean expressions alone"
            )

    except ParseError as e:
        expected = "`" + "`, `".join(list(tmap[e.state].keys())) + "`"

        if len(list(tmap[e.state].keys())) > 1:
            print(
                f"{RED}error{NC}: {BLD}expected one of {expected}{NC}, found `{e.char}`"
            )
        else:
            print(f"{RED}error{NC}: {BLD}expected {expected}{NC}, found `{e.char}`")

        print(f"  {PRP}-->{NC} {source}")
        print(f" {PRP}  |{NC} ")
        print(f" {PRP}0 |{NC} ", end="")
        for i, c in enumerate(input):
            if i == e.pos:
                print(f"{RED}{c}{NC}", end="")
            else:
                print(c, end="")
        print()
        print(f" {PRP}  |{NC} ", end="")
        print(" " * e.pos + f"{RED}^ unexpected character{NC}")
        print(f" {PRP}  |{NC} ")
        if len(list(tmap[e.state].keys())) > 1:
            print(f" {PRP}  ={NC} {BLD}help{NC}: try one of the following characters:")
            print(f" {PRP}  ={NC} {BLD}help{NC}:   {expected}")
        else:
            print(f" {PRP}  ={NC} {BLD}help{NC}: try placing a {expected}")


if __name__ == "__main__":
    while True:
        expression = input("> ")
        parse(expression)
