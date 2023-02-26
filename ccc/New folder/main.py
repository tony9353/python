with open("scores.txt", "r") as f:
    scores = f.read().split("\n")

a = (3 * int(scores[0])) + (2 * int(scores[1])) + int(scores[2])
b = (3 * int(scores[3])) + (2 * int(scores[4])) + int(scores[5])

with open("result.txt", "w") as f:
    if a > b:
        f.write("A")
    elif a < b:
        f.write("B")
    else:
        f.write("T")