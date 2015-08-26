first = raw_input("Enter a base:")
second = raw_input("Enter an exponent:")
solution = int(first) ** int(second)

print "{} to the power of {} = {}".format(first, second, solution)


def square(number):
    """Return the result of input number to
            the power of 2."""
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square(input_num)
print output_num
