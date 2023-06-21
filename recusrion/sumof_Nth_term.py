def nth_term(n):
    if n == 0:
        return 0
    return (n+nth_term(n-1))
print(nth_term(6))