join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))
print(join_to_biggest([11, 2, 56, 9]))