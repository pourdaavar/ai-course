import numpy as np

# Define the input variables (height and weight)
height = float(input("Enter height (in cm): "))
weight = float(input("Enter weight (in kg): "))

# Fuzzification


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


# Fuzzify the inputs
height_short = fuzzy_height_short(height)
height_average = fuzzy_height_average(height)
height_tall = fuzzy_height_tall(height)

weight_light = fuzzy_weight_light(weight)
weight_average = fuzzy_weight_average(weight)
weight_heavy = fuzzy_weight_heavy(weight)

# Decision Making (Using MIN operator for "and" operation)
fit_level = {
    'Not Fit': min(height_short, weight_heavy),
    'Fit': min(height_average, weight_average),
    'Very Fit': min(height_tall, weight_light)
}
