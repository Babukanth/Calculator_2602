def grade_calculator(name, m1, m2, m3):
    # Calculate total and percentage
    total = m1 + m2 + m3
    percentage = (total / 300) * 100

    # Determine grade
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    # Prepare output
    print(name)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}")

grade_calculator("Raj", 80, 70, 90)
grade_calculator("Babu", 85, 90, 95)
grade_calculator("Aananthi", 99, 99, 99)
