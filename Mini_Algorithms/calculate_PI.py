import random




def main():
    # For simplicity, we are assuming the circle has the center at (0,0)
    radius = 0.5

    num_points = 100000000000

    # Counter
    points_in_circle = 0

    for i in range(num_points):
        # Generate a random point (x,y)
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        # Get the distance through circle equation
        point_distance = (x ** 2 + y ** 2) ** 0.5

        # Check if the point is inside the circle
        if point_distance <= radius:
            points_in_circle += 1

    # Calculate probability
    pi_value = points_in_circle / num_points * 4

    print("π: ", pi_value)

if __name__ == "__main__":
    # a) We can approximate π constant
    # b) It took 100,000,000,000 iterations to approximate to four decimals places
    main()