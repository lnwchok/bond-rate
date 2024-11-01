import click


@click.command()
@click.option(
    "--age", prompt="Your age", type=int, help="The age of the person to be insured."
)
@click.option(
    "--value",
    prompt="Value of the item to be insured",
    type=float,
    help="The value of the item to be insured.",
)
def calculate_insurance_rate(age, value):
    """Simple program that calculates insurance rate based on age and value of the item."""
    base_rate = 0.05  # Base rate is 5% of the item value

    # Adjust rate based on age
    if age < 25:
        age_factor = 1.5  # Higher risk for younger individuals
    elif age < 60:
        age_factor = 1.0  # Standard rate
    else:
        age_factor = 1.2  # Slightly higher risk for older individuals

    # Calculate final insurance rate
    insurance_rate = base_rate * age_factor * value

    click.echo(
        f"The insurance rate for a {age}-year-old with an item valued at ${value:.2f} is ${insurance_rate:.2f}."
    )


if __name__ == "__main__":
    calculate_insurance_rate()
