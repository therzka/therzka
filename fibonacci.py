"""
fibonacci.py — no cap, this actually slaps 🔥

Computes the n-th Fibonacci number using an iterative approach.
Time complexity: O(n) | Space complexity: O(1) — slay, no memory waste.

Usage:
    python fibonacci.py          # runs a lil demo, bestie
    from fibonacci import fib    # import and vibe
"""


def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed). Not a vibe for n < 0.

    The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(5) = 5, fib(10) = 55.

    Args:
        n: A non-negative integer index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative — that's giving chaos, we don't fw that.
    """
    if n < 0:
        raise ValueError(f"bestie, {n} is giving negative energy — n must be >= 0")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    demo_values = [0, 1, 2, 5, 10, 20]
    print("✨ slay sequence incoming fr fr ✨")
    for i in demo_values:
        print(f"  fib({i}) = {fib(i)} 💅")
    print("no cap, that's the Fibonacci sequence bestie 🔥")
