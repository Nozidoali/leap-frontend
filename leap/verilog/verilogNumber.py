#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 14:12:59
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 14:14:06
"""

from typing import Optional


class Number:
    def __init__(self, length: Optional[int], base: Optional[str], mantissa: str):
        assert isinstance(mantissa, str), "Mantissa is expected to be a string."
        assert length is None or isinstance(length, int)
        self.length = length
        self.base = base
        self.mantissa = mantissa

    def as_integer(self):
        base_map = {"h": 16, "b": 2, "d": 10, "o": 8}

        if self.base is None:
            int_base = 10
        else:
            base = self.base.lower()
            assert base in base_map, "Unknown base: '{}'".format(base)
            int_base = base_map[base]

        return int(self.mantissa, base=int_base)

    def __int__(self):
        return self.as_integer()

    def as_bits_lsb_first(self):
        """
        Get integer value as a list of bits.
        If the length of the Number is not None then the list is either extended or truncated to the given length.
        Extension is sign extended.
        :return:
        """
        value = self.as_integer()
        x = value
        bits = []
        while x != 0:
            bits.append(x & 1)
            x //= 2

        if self.length is not None:
            if len(bits) < self.length:
                sign = 1 if value < 0 else 0
                # Extend.
                bits.extend([sign] * (self.length - len(bits)))
            elif len(bits) > self.length:
                # Truncate
                bits = bits[0 : self.length]

        return bits

    def as_bits_msb_first(self):
        return list(reversed(self.as_bits_lsb_first()))

    def __repr__(self):
        if self.base is None:
            return "{}".format(self.as_integer())
        elif self.length is None:
            return "'{}{}".format(self.base, self.mantissa)
        else:
            return "{}'{}{}".format(self.length, self.base, self.mantissa)


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def to_indices(self):
        """
        Convert to list of indices in the range.
        :return:
        """
        return list(reversed(range(self.end.as_integer(), self.start.as_integer() + 1)))

    def __repr__(self):
        return "[{}:{}]".format(self.start, self.end)


class Vec:
    def __init__(self, name: str, range: Range):
        self.name = name
        self.range = range

    def __repr__(self):
        return "{}{}".format(self.name, self.range)


def test_class_number():
    assert Number(None, None, "12").as_bits_lsb_first() == [0, 0, 1, 1]
    assert Number(None, None, "12").as_bits_msb_first() == [1, 1, 0, 0]
    assert Number(5, None, "12").as_bits_msb_first() == [0, 1, 1, 0, 0]
    assert Number(3, None, "12").as_bits_msb_first() == [1, 0, 0]
    assert Number(3, "h", "c").as_bits_msb_first() == [1, 0, 0]
