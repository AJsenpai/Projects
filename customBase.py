def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    # we'll see this later, but the following would be better:
    encoding = "".join([digit_map[d] for d in digits])
    return encoding


def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end, this way -ve number
    # could turn positive for calculations
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = "-" + encoding
    return encoding


e = rebase_from10(-10, 2)
# e = rebase_from10(232, 5)
print(e)
print(int(e, 2))
# print(int(e, 5))
