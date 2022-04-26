from __future__ import annotations


def iswh0(h: list[int]) -> bool:
    a, b = h[0], h[1]

    for i in range(7):
        r = a % 3

        if b >= r and h[i + 2] >= r:
            a, b = b - r, h[i + 2] - r
        else:
            return False

    return a % 3 == 0 and b % 3 == 0


def iswh2(h: list[int]) -> bool:
    s = 0

    for i in range(9):
        s += i * h[i]

    for p in range(s * 2 % 3, 9, 3):
        if h[p] >= 2:
            h[p] -= 2

            if iswh0(h):
                h[p] += 2
                return True
            else:
                h[p] += 2

    return False


def islh(h: list[int]) -> bool:
    head: int | None = None

    for i in range(3):
        s = sum(h[9 * i:9 * i + 9])

        if s % 3 == 1:
            return False
        elif s % 3 == 2:
            if head is None:
                head = i
            else:
                return False

    for i in range(27, 34):
        if h[i] % 3 == 1:
            return False
        elif h[i] % 3 == 2:
            if head is None:
                head = i
            else:
                return False

    for i in range(3):
        if i == head:
            if not iswh2(h[9 * i:9 * i + 9]):
                return False
        else:
            if not iswh0(h[9 * i:9 * i + 9]):
                return False

    return True


def issp(h: list[int]) -> bool:
    for i in range(34):
        if h[i] != 0 and h[i] != 2:
            return False

    return True


def isto(h: list[int]) -> bool:
    for i in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25]:
        if h[i] > 0:
            return False

    for i in [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]:
        if h[i] == 0:
            return False

    return True
