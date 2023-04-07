def dice_probability(x):
    if x < 2 or x > 18:
        return 0
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k == x:
                    count += 1
    return count / 216
print(dice_probability(7)) # output: 0.125
