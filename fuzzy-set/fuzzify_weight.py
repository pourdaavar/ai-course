def fuzzy_weight_light(x):
    if x <= 50:
        return 1
    elif 50 < x <= 70:
        return (70 - x) / (70 - 50)
    else:
        return 0


def fuzzy_weight_average(x):
    if 50 < x <= 70:
        return (x - 50) / (70 - 50)
    elif 70 < x <= 90:
        return (90 - x) / (90 - 70)
    else:
        return 0


def fuzzy_weight_heavy(x):
    if x <= 70:
        return 0
    elif 70 < x <= 90:
        return (x - 70) / (90 - 70)
    else:
        return 1
