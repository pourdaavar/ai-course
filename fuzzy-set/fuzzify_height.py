def fuzzy_height_short(x):
    if x <= 140:
        return 1
    elif 140 < x <= 160:
        return (160 - x) / (160 - 140)
    else:
        return 0


def fuzzy_height_average(x):
    if 140 < x <= 160:
        return (x - 140) / (160 - 140)
    elif 160 < x <= 180:
        return (180 - x) / (180 - 160)
    else:
        return 0


def fuzzy_height_tall(x):
    if x <= 160:
        return 0
    elif 160 < x <= 180:
        return (x - 160) / (180 - 160)
    else:
        return 1
