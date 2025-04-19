f = [int(i.rstrip("\n")) for i in open("files/26.2.txt","r")]
def find_possible_sums(numbers):
    possible_sums = {0}
    for num in numbers:
        new_sums = set()
        for s in possible_sums:
            new_sums.add(s + num)
        possible_sums.update(new_sums)
    return possible_sums

f = sorted(f)
result = find_possible_sums(f)
for i in range(10**10):
    if i not in result:
        print(i)
        break