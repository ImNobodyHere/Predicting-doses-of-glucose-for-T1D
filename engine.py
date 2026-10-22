# This project will contain three 4 concepts:
# ICR : How many grams of carbs one unit of insulin covers.
# ISF : How many mg/dL one unit drops your glucose.
# IOB : Insulin from earlier doses that is still working, which is what prevent stacking.
# The duration of insulin action usually around 4 to 6 hours, because IOB is just “how much of each past dose has not acted yet.”

#Theres two types of injections:
#       The basal: which is the insulin injection that doesn't matter the meal.
#       The bolus: is the correction dose for meals that caused hyperglycemia

# Usually these terms are identified as Basal = Lantus pen insulin which is basically a one time day injection that works slow over day
# And Bolus is a fast acting insulin like Novorapid / Humalog etc which is for pre meals or after meals and even correction doses

# The user will provide the amount of carbs of his meal 
# We predict that every 12-15g of carbs => 1 insulin (The values varies on each person)


def get_icr_range():
    return (12,15)

def meal_dose_range(carbs_g):
    icr_low, icr_max = get_icr_range()
    min_result = carbs_g / icr_low
    max_result = carbs_g / icr_max
    return min_result, max_result

class InvalidCarbsError(ValueError):
    pass



# icr_weakest_unit, icr_strongest_unit = meal_dose_range(60)
# print(f'Minimum injection: {icr_strongest_unit} || Maximum injection: {icr_weakest_unit}')




