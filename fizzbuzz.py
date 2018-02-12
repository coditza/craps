def multi(max, mapping):
    for i in range(1, max + 1):
        fbzz = ''.join([mapping[x] for x in mapping if i % x == 0])
        print(fbzz if len(fbzz) else i)


if __name__ == '__main__':
    multi(15, {3: 'Fizz', 5: 'Buzz'})
    multi(15, {2: 'Two', 3: 'Three', 5: 'Five'})
