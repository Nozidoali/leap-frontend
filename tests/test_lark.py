import lark


def test_00_lark():
    grammar = """
    start: expression

    ?expression: NAME
                | "(" expression ")"
                | expression "==" expression -> eq
                | "!" expression -> not
    
    %import common.CNAME -> NAME
    %import common.WS
    %ignore WS
    """
    parser = lark.Lark(grammar, parser="earley", lexer="dynamic_complete")
    tree = parser.parse("!(a == b)")
    tree = parser.parse("!a == b")
    print(tree.pretty())


if __name__ == "__main__":
    test_00_lark()
