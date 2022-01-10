from tokens import Token


class Scroller:

    def __init__(self, program: str):
        self.program = program
        self.prev = ""

    @property
    def pointer(self) -> str:
        return self.program[0]

    def next(self, offset: int = 1) -> str:
        return self.program[offset]

    def shift(self, units: int = 1):
        self.prev = self.program[:units][-1]
        self.program = self.program[units:]


def plus(scroller: Scroller) -> Token:
    if scroller.next() == "+":
        return (Token.MUL, Token.POW)[scroller.next(2) == "+"]
    return Token.ADD


def minus(scroller: Scroller) -> Token:
    tokens = {
        ">": (Token.TO, Token.IN)[scroller.next(2) == "?"],
        "-": (Token.DIV, Token.MOD)[scroller.next(2) == "-"]
    }
    return tokens.get(scroller.next(), Token.SUB)


def colon(scroller: Scroller) -> Token:
    if scroller.next() == ":":
        return (Token.EQ, Token.NE)[scroller.next(2) == ":"]
    if scroller.next() == "!" and scroller.next(2) == ":":
        return Token.SIZE
    return Token.ASSIGN


def less(scroller: Scroller) -> Token:
    tokens = {
        "-": Token.FROM,
        "<": Token.SLICE_OPEN,
        ":": Token.LE
    }
    return tokens.get(scroller.next(), Token.LT)


def greater(scroller: Scroller) -> Token:
    if scroller.program[:3] == ">==":
        return Token.COMMENT_CLOSE
    tokens = {
        ">": Token.SLICE_CLOSE,
        ":": Token.GE
    }
    return tokens.get(scroller.next(), Token.GT)


def equal(scroller: Scroller) -> Token | None:
    if scroller.next() == "=":
        try:
            return (Token.COMMENT, Token.COMMENT_OPEN)[scroller.next(2) == "<"]
        except IndexError:
            return Token.COMMENT
    return None


def dot(scroller: Scroller) -> Token:
    if scroller.next() == ".":
        return (Token.WHILE, Token.FOR)[scroller.next(2) == "."]
    return Token.ATTRIBUTE


def question(scroller: Scroller) -> Token:
    if scroller.next() == "?":
        return (Token.TRY, Token.STDIN)[scroller.next(2) == "?"]
    return (Token.IF, Token.TYPE)[scroller.next() == "!"]


def exclamation(scroller: Scroller) -> Token:
    if scroller.next() == "!":
        return (Token.CATCH, Token.THROW)[scroller.next(2) == "!"]
    return Token.STDOUT


def pipe(scroller: Scroller) -> Token:
    return (Token.BINOR, Token.OR)[scroller.next() == "|"]


def ampersand(scroller: Scroller) -> Token:
    return (Token.BINAND, Token.AND)[scroller.next() == "&"]


def tilde(scroller: Scroller) -> Token:
    return (Token.BINNOT, Token.NOT)[scroller.next() == "~"]


def caret(scroller: Scroller) -> Token:
    return (Token.XOR, Token.RANDOM)[scroller.next() == "^"]


def comma(scroller: Scroller) -> Token:
    return (Token.SEP, Token.ELSE)[scroller.next() == ","]


def open_brace(scroller: Scroller) -> Token:
    return (Token.BRACE_OPEN, Token.TABLE_OPEN)[scroller.next() == "{"]


def close_brace(scroller: Scroller) -> Token:
    try:
        return (Token.BRACE_CLOSE, Token.TABLE_CLOSE)[scroller.next() == "}"]
    except IndexError:
        return Token.BRACE_CLOSE


def hash_(scroller: Scroller) -> Token:
    return (Token.LAMBDA, Token.HASH)[scroller.next() == "#"]


def asterisk(scroller: Scroller) -> Token:
    return (Token.FUNCTION, Token.SLICE_STEP)[scroller.next() == "*"]
