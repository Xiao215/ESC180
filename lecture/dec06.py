# Turing's halting problem
# Geodel's Incompleteness Theorum
def f():
    while True:
        pass


def g():
    n = 3
    while True:
        if n % 2 == 0 and is_prime(n):
            return
        n += 1
# g is not gonna half s


def fermat(p):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p+j**p == k**p:
                        return i, j, k
        n += 1
# Halting problem: will the function f halt (meaning return) on input x

# Proof:
# Assume that halt(f,x) exists, we will prove that this leads to a contradiction
# Assume halt (f,x) exists


def halt(f, x):
    """return True if f(x) halts, False otherwise"""


def confused(f):
    if halt(f, f):
        while True:
            pass
        else:
            return False
# confused(confused) halts => half(confused, confused) is False
#                          => confused(confused) does not halt

# confused(confused) does not halt => halt(confused, confused) is True
#                                 => confused(confused) halts

# We proved that confused(confused) can neither halt or not halt
