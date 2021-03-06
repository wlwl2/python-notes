# The Python Standard Library (Python 3)
# https://docs.python.org/3/library/index.html

# Single line comments.

""" Multiline strings
"""

# Built-in Types

## Truth Value Testing

"""
    Any object can be tested for truth value, for use in an if or while
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
not x	# if x is false, then True, else False (highest priority)

## Comparisons

<	    # strictly less than
<=	    # less than or equal
>	    # strictly greater than
>=	    # greater than or equal
==	    # equal
!=	    # not equal
is	    # object identity
is not  # negated object identity

## Numeric Types — int, float, complex

x + y	            # sum of x and y
x - y	            # difference of x and y
x * y	            # product of x and y
x / y	            # quotient of x and y
x // y	            # floored quotient of x and y. See (1)
x % y	            # remainder of x / y. See (2)
-x	                # x negated
+x	                # x unchanged
abs(x)	            # absolute value or magnitude of x
int(x)	            # x converted to integer (3)(6)
float(x)            # x converted to floating point (4)(6)
complex(re, im)	    """ complex number with real part `re`, imaginary
                     part `im`. `im` defaults to zero. (6) """
c.conjugate()       # conjugate of the complex number c.
divmod(x, y)        # the pair (x // y, x % y) (2)
pow(x, y)           # x to the power y (5)
x ** y	            # x to the power y (5)

"""
    Notes:

    (1) Also referred to as integer division. The resultant value is a
        whole integer, though the result’s type is not necessarily int.
        The result is always rounded towards minus infinity: 1//2 is 0,
        (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0.

    (2) Not for complex numbers. Instead convert to floats using
        abs() if appropriate.

    (3) Conversion from floating point to integer may round or truncate
        as in C; see functions math.floor() and math.ceil() for well-defined
        conversions.

    (4) float also accepts the strings “nan” and “inf” with an optional
        prefix “+” or “-” for Not a Number (NaN) and positive or
        negative infinity.

    (5) Python defines pow(0, 0) and 0 ** 0 to be 1

    (6) The numeric literals accepted include the digits 0 to 9 or
        any Unicode equivalent (code points with the Nd property).

"""
