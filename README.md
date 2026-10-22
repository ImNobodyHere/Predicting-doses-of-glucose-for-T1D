# Predicting-doses-of-glucose-for-T1D
Educational simulator that estimates Min/Max insulin dose ranges from carbs and glucose for T1D. Demo only, not medical advice.

This project is a decision-support simulator that shows how carbohydrate intake, current glucose, and active insulin combine into a bolus estimate. For Type 1 Diabetes it implements the standard Insulin-to-Carbohydrate Ratio, Insulin Sensitivity Factor.

Instead of returning a single number, it returns a Min/Max range: a conservative dose that avoids hypoglycemia and a higher dose that covers the glucose spike. Every result shows the formula steps behind it, and hard safety limits (maximum bolus cap, low-glucose block, input sanity checks) are applied before and after each calculation. A synthetic data module stress-tests the logic against thousands of generated cases.

Disclaimer: This is an educational and portfolio project using demo parameters. It is not a medical device and must never be used to decide real insulin doses. Always follow your healthcare provider’s guidance.
