import random



def getProbability(n_points, radius):
    # For simplicity, we are assuming the circle has the center at (0,0)

    # Counter
    points_in_the_circle = 0

    for i in range(n_points):
        # Generate a random point (x,y)
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        # Get the distance through circle equation
        point_distance = (x ** 2 + y ** 2) ** 0.5

        # Check if the point is inside the circle
        if point_distance <= radius:
            points_in_the_circle += 1

    # Calculate probability
    probability = points_in_the_circle / n_points

    print("Probability: ", probability)

def main():
    getProbability(100, 0.5)
    getProbability(1000, 1)
    getProbability(10000, 10)
    

if __name__ == "__main__":
    main()