employees = [
    ("John", 50000, 4.5),
    ("Alice", 60000, 4.7),
    ("Bob", 45000, 4.2),
    ("Emma", 55000, 4.6),
    ("James", 48000, 4.4)
]

sales_weight = 0.6
satisfaction_weight = 0.4

# Calculate weighted score and sort employees
top_performers = sorted(employees, key=lambda e: (e[1] * sales_weight) + (e[2] * satisfaction_weight), reverse=True)

# Display sorted employees based on performance
print("Top-performing employees:")
for employee in top_performers:
    print(f"Name: {employee[0]}, Score: {(employee[1] * sales_weight) + (employee[2] * satisfaction_weight):.2f}")

#scenario 2:
import math

# Calculate square roots of even numbers from 1 to 10
even_square_roots = [(x, (lambda n: math.sqrt(n))(x)) for x in range(1, 11) if x % 2 == 0]

# Display the results
print("Square roots of even numbers:")
for num, sqrt_val in even_square_roots:
    print(f"Number: {num}, Square Root: {sqrt_val:.2f}")
