def calculate_sprint_velocity():
    """Calculates average sprint velocity based on previous sprints' point completion."""
    try:
        previous_points_input = input("Enter previous sprints' point completion separated by space: ")
        previous_points = list(map(int, previous_points_input.split()))
        
        if previous_points:
            average_velocity = sum(previous_points) / len(previous_points)
            print(f"Average sprint velocity: {average_velocity:.2f} points")
        else:
            print("No points entered. Please enter the completion points of previous sprints.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces for previous sprint points.")
