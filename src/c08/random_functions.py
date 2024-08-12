def are_anagrams(s1, s2):
    """Check if two strings are anagrams."""
    return sorted(s1.lower()) == sorted(s2.lower())


def factorial(n):
    """Return the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
