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

def calculate_team_effort_hours():
    """Calculates team effort-hour capacity based on sprint days and member details."""
    try:
        sprint_days = int(input("Enter number of sprint days: "))
        num_team_members = int(input("Enter number of team members: "))

        pto_days, ceremony_hours, hours_per_day_range = [], [], []
        for i in range(num_team_members):
            print(f"Team member {i+1}:")
            pto_days.append(int(input("Enter number of PTO days: ")))
            ceremony_hours.append(int(input("Enter number of ceremony hours: ")))
            hours_per_day_range.append(tuple(map(int, input("Enter available hours/day range (min, max): ").split(','))))

        available_effort_hours_per_person = []
        for i in range(num_team_members):
            min_hours, max_hours = hours_per_day_range[i]
            available_hours = sprint_days * (max_hours + min_hours) / 2 - pto_days[i] * (max_hours + min_hours) / 2 - ceremony_hours[i]
            available_effort_hours_per_person.append(available_hours)

        total_available_effort_hours = sum(available_effort_hours_per_person)
        print(f"Available Effort-Hours/Person: {available_effort_hours_per_person}")
        print(f"Available Effort-Hours for Team: {total_available_effort_hours}")
    except ValueError:
        print("Invalid input. Please enter integers for numerical values and ranges separated by a comma for hours/day.")

def main():
    """Provides the user interface and handles option selection."""
    while True:
        print("\nHome Menu:")
        print("1. Calculate Sprint Team's Velocity")
        print("2. Calculate Team Effort-Hour Capacity")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            calculate_sprint_velocity()
        elif choice == '2':
            calculate_team_effort_hours()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
