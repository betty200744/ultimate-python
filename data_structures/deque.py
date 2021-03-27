"""
a deque is a lifo stack, and a fifo queue
time comple
"""
from collections import deque


def main():
    dp = deque()
    for i in range(1, 5):
        dp.append(i)
        dp.appendleft(i * 2)
    print(dp)


if __name__ == '__main__':
    main()
