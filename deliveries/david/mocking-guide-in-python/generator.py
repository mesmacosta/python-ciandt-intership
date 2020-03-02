from itertools import islice
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr
f = fib()
print(list(islice(f, 0, 20)))