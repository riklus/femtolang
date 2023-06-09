from typing import TypeVar, Generic, Iterable

S = TypeVar("S")
E = TypeVar("E")


class ParseError(Exception):
    def __init__(self, pos: int, char, state) -> None:
        super().__init__()
        self.pos = pos
        self.char = char
        self.state = state
        self.__traceback__ = None


class DFA(Generic[S, E]):
    def __init__(self, initial: S, accept: set[S], tmap: dict[S, dict[E, S]]) -> None:
        self.initial = initial
        self.accept = accept
        self.tmap = tmap

    def parse(self, input: Iterable[E]):
        state = self.initial
        status = state in self.accept
        for i, event in enumerate(input):
            status = state in self.accept
            yield state, event, status
            try:
                state = self.tmap[state][event]
            except KeyError as _:
                raise ParseError(i, event, state)

        yield state, None, state in self.accept
