import numpy as np
from fuzzify_height import *
from fuzzify_weight import *
from fuzzify_bmi import *
from t_norm import *

# Define the input variables (height and weight)
# height = float(input("Enter height (in cm): "))
# weight = float(input("Enter weight (in kg): "))
height = 164  # cm
weight = 75  # kg

# Fuzzify the inputs
height_short = fuzzy_height_short(height)
height_average = fuzzy_height_average(height)
height_tall = fuzzy_height_tall(height)

weight_light = fuzzy_weight_light(weight)
weight_average = fuzzy_weight_average(weight)
weight_heavy = fuzzy_weight_heavy(weight)

# Decision Making (Using MIN operator for "and" operation)
fit_level = {
    "Level 1": t_norm(height_short, weight_light),
    "Level 2": t_norm(height_average, weight_light),
    "Level 3": t_norm(height_tall, weight_light),
    "Level 4": t_norm(height_short, weight_average),
    "Level 5": t_norm(height_average, weight_average),
    "Level 6": t_norm(height_tall, weight_average),
    "Level 7": t_norm(height_short, weight_heavy),
    "Level 8": t_norm(height_average, weight_heavy),
    "Level 9": t_norm(height_tall, weight_heavy),
}

BMI_Range = [[10, 18], [18, 25], [25, 35], [35, 180]]

bmi_light = fuzzy_bmi_light(BMI_Range, weight_light)
bmi_average = fuzzy_bmi_normal(BMI_Range, weight_average)
bmi_heavy = fuzzy_bmi_heavy(BMI_Range, weight_heavy)
bmi_obese = fuzzy_bmi_obese(BMI_Range, weight_heavy)

# defuzify with Center of sums


def defuzzify_center_of_sums(fuzzy_set):
    numerator = 0
    denominator = 0

    for key, value in fuzzy_set.items():
        numerator += key * value
        denominator += value

    if denominator != 0:
        return numerator / denominator
    else:
        return None

# https://cse.iitkgp.ac.in/~dsamanta/courses/archive/sca/Archives/Chapter%205%20Defuzzification%20Methods.pdf
