def substrings(number: str) -> int:
    modulo = int(1e9 + 7)
    result = sub_sum = int(number[0])

    for digit_idx in range(1, len(number)):
        digit = int(number[digit_idx])
        digit_presence = digit_idx + 1
        sub_sum = (sub_sum * 10 + digit * digit_presence) % modulo
        result = (result + sub_sum) % modulo

    return result