def main():
    print(len(list(filter(check, range(158126, 524574 + 1)))))


def check(num):
    valid = True
    num = str(num)
    digits = [int(c) for c in num]
    for i, n in enumerate(digits[:len(digits) - 1]):
        if n > digits[i + 1]:
            valid = False
            break
    d_digit = False

    for i, n in enumerate(digits[:len(digits) - 1]):
        if n == digits[i + 1]:
            d_digit = True
            break

    if d_digit is False:
        valid = False
    return valid

if __name__ == '__main__':
    main()