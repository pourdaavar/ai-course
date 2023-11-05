def fuzzy_bmi_light(BMI, x):
    if x <= BMI[0][0]:
        return 1
    elif BMI[0][0] < x <= BMI[0][1]:
        return (BMI[0][1] - x) / (BMI[0][1] - BMI[0][0])
    else:
        return 0


def fuzzy_bmi_normal(BMI, x):
    if BMI[0][1] < x <= BMI[1][0]:
        return (x - BMI[0][1]) / (BMI[1][0] - BMI[0][1])
    elif BMI[1][0] < x <= BMI[1][1]:
        return (BMI[1][1] - x) / (BMI[1][1] - BMI[1][0])
    else:
        return 0


def fuzzy_bmi_heavy(BMI, x):
    if x <= BMI[1][1]:
        return 0
    elif BMI[1][1] < x <= BMI[2][0]:
        return (x - BMI[1][1]) / (BMI[2][0] - BMI[1][1])
    elif BMI[2][0] < x <= BMI[2][1]:
        return (BMI[2][1] - x) / (BMI[2][1] - BMI[2][0])
    else:
        return 1


def fuzzy_bmi_obese(BMI, x):
    if x <= BMI[2][1]:
        return 0
    elif BMI[2][1] < x <= BMI[3][0]:
        return (x - BMI[2][1]) / (BMI[3][0] - BMI[2][1])
    elif BMI[3][0] < x <= BMI[3][1]:
        return (BMI[3][1] - x) / (BMI[3][1] - BMI[3][0])
    else:
        return 1
