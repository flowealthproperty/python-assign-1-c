def calculate_paint_and_labour(square_feet, price_per_gallon, labour_rate):
    """
    Calculate the number of gallons of paint required, cost of paint, hours of labour,
    cost of labour, and total cost of the paint job.
    """
    gallons_of_paint = square_feet / 112
    cost_of_paint = gallons_of_paint * price_per_gallon
    hours_of_labour = square_feet / 112 * 8  # Assuming 8 hours to paint 112 square feet
    cost_of_labour = hours_of_labour * labour_rate
    total_cost = cost_of_paint + cost_of_labour

    return gallons_of_paint, cost_of_paint, hours_of_labour, cost_of_labour, total_cost

def main():
    try:
        square_feet = float(input("Enter the number of square feet of wall space to be painted: "))
        price_per_gallon = float(input("Enter the price of the paint per gallon: $"))
        labour_rate = float(input("Enter the labour rate per hour: $"))

        gallons_of_paint, cost_of_paint, hours_of_labour, cost_of_labour, total_cost = calculate_paint_and_labour(square_feet, price_per_gallon, labour_rate)

        print("\nEstimate for the paint job:")
        print(f"Number of gallons of paint required: {gallons_of_paint:.2f}")
        print(f"Cost of the paint: ${cost_of_paint:.2f}")
        print(f"Hours of labour required: {hours_of_labour:.2f}")
        print(f"Cost of the labour: ${cost_of_labour:.2f}")
        print(f"Total cost of the paint job: ${total_cost:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values for square feet, price per gallon, and labour rate.")

if __name__ == "__main__":
    main()
