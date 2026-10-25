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
import math
import exceptions as e

def get_icr_range():
    return (12, 15)

def validate_carbs(value):
    if isinstance(value, bool):
        raise e.InvalidCarbsError("The value of carb must be a number.")
    if not isinstance(value, (int, float)):
        raise e.InvalidCarbsError("The value of carb must be a number.")
    if not math.isfinite(value):
        raise e.InvalidCarbsError("The value of carb is invalid!")
    if value <= 0:
        raise e.InvalidCarbsError("The value of carb must be positive.")
    if value > e.HARD_LIMIT:
        raise e.InvalidCarbsError("The value of carb must not be above 300.")

    needs_confirmation = value > e.SOFT_LIMIT
    return value, needs_confirmation

def meal_dose_range(carbs_g):
    icr_low, icr_high = get_icr_range()
    dose_min = carbs_g / icr_high
    dose_max = carbs_g / icr_low
    return dose_min, dose_max

if __name__ == "__main__":
    try:
        raw = input("Insert your carbohydrate value: ")
        carbs_g, needs_confirmation = validate_carbs(float(raw))

        if needs_confirmation:
            answer = input(f"You entered {carbs_g} g, is that correct? (y/n): ")
            if answer.lower() != "y":
                raise SystemExit("Cancelled.")

        dose_min, dose_max = meal_dose_range(carbs_g)
        print(f"Minimum injection: {dose_min:.1f} units || Maximum injection: {dose_max:.1f} units")

    except (ValueError, e.InvalidCarbsError) as err:
        print(err)




# icr_weakest_unit, icr_strongest_unit = meal_dose_range(60)
# print(f'Minimum injection: {icr_strongest_unit} || Maximum injection: {icr_weakest_unit}')




