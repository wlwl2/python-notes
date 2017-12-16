# Python 3

# Single line comments.

""" Multiline strings
"""

# Built-in Types
## Truth Value Testing
""" Any object can be tested for truth value, for use in an if or while
condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a
__bool__() method that returns False or a __len__() method that returns zero,
when called with the object. [1] Here are most of the built-in objects
considered false:

constants defined to be false: None and False. zero of any numeric type: 0, 0.0,
0j, Decimal(0), Fraction(0, 1) empty sequences and collections: '', (), [], {},
set(), range(0) Operations and built-in functions that have a Boolean result
always return 0 or False for false and 1 or True for true, unless otherwise
stated. (Important exception: the Boolean operations or and and always return
one of their operands.)
"""
# 4.2. Boolean Operations — and, or, not
# These are the Boolean operations, ordered by ascending priority:
# Operation	# Result
x or y	# if x is false, then y, else x
x and y	# if x is false, then x, else y
not x	# if x is false, then True, else False

## Comparisons

<	# strictly less than
<=	# less than or equal
>	# strictly greater than
>=	# greater than or equal
==	# equal
!=	# not equal
is	# object identity
is not # negated object identity

# Numeric Types — int, float, complex
