def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    return (principal * rate * time) / 100

# Example usage
p = 1000  # principal
r = 5     # annual interest rate
t = 2     # time in years

interest = calculate_simple_interest(p, r, t)
print(f"Simple Interest: {interest}")
