def multi(max, mapping, separator):
    result = []
    for i in range(1, max + 1):
        fbzz = ''.join([mapping[x] for x in mapping if i % x == 0])
        result.append(fbzz if len(fbzz) else str(i))
    return separator.join(result)


if __name__ == '__main__':
    print("USAGE: multi(max, mapping, separator) -> string")
