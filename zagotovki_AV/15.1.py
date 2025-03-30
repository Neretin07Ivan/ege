for A in range(1000,1,-1):
    for x in range(100):
        for y in range(100):
            # (y + 2x ≠ 48) ∨ (A < x) ∨ (A < y)
            if not((y + 2*x != 48) or (A < x) or (A < y)):
                break
        if not ((y + 2 * x != 48) or (A < x) or (A < y)):
            break
    else:
        print(A)
        exit()