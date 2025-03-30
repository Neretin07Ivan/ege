print("a,b,c,d")
for a in range(2):
    for d in range(2):
        for b in range(2):
            for c in range(2):
                # (z ∧ y) ∨ ((x → z ) ≡ (y → w))
                if c and (a or d) and (not d or b):
                    print(a,b,c,d)

