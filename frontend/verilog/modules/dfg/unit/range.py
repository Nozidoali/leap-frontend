class Range:
    def __init__(self, start: int, end: int = None):
        self.start = start
        self.end = end


def rangeToString(range: Range) -> str:
    assert isinstance(range, Range), f"Expected Range, got {type(range)}"
    return (
        f"[{range.start}:{range.end}]" if range.end is not None else f"[{range.start}]"
    )
