low = int(input('Enter a low number: '))  # 1
high = int(input('Enter a high number: '))  # 20
while low <= high:
    # if 0 < low < 10 or 15 < low <= 20:
    #    print(low)
    low += 1
    if not 10 <= low <= 15:
        print(low)
    else:
        continue
