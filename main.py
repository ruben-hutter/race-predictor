import time


def ask_distance() -> float | None:
    """Ask the user for the distance they would like to predict their pace for"""
    print("Enter the distance you would like to predict your pace for:")
    print("1. 5k")
    print("2. 10k")
    print("3. Half Marathon")
    print("4. Marathon")
    print("5. Custom Distance")

    distance = input("Enter the number of your selection: ")

    try:
        distance = int(distance)
        match distance:
            case 1:
                return 5
            case 2:
                return 10
            case 3:
                return 21.1
            case 4:
                return 42.2
            case 5:
                return float(input("Enter the distance in km: "))
            case _:
                print("Invalid selection")
                return None
    except ValueError:
        print("Invalid selection. Please enter a number")
        return None


def ask_time(distance: float) -> time.struct_time | None:
    """Ask the user for the time they would like to predict their pace for"""
    t = input(f"Enter your predicted time for {distance}k (HH:MM:SS) or (MM:SS): ")

    t_parts = t.split(":")
    if len(t_parts) == 1:
        t = f"00:00:{t_parts[0]}"
    elif len(t_parts) == 2:
        t = f"00:{t_parts[0]}:{t_parts[1]}"
    else:
        t = ":".join(t_parts)

    try:
        return time.strptime(t, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS or MM:SS")
        return None


def calculate_pace(distance: float, t: time.struct_time) -> tuple[str, str]:
    """Calculate the pace in min:sec per km and mile"""
    total_seconds = t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec
    total_minutes = total_seconds / 60

    min_per_km = total_minutes / distance
    min_per_mile = total_minutes / (distance * 0.621371)

    def format_pace(pace: float) -> str:
        minutes = int(pace)
        seconds = int((pace - minutes) * 60)
        return f"{minutes}:{seconds:02d}"

    return format_pace(min_per_km), format_pace(min_per_mile)


def output_pace(pace: tuple[str, str]):
    """Output the calculated pace"""
    min_per_km, min_per_mile = pace
    print(f"Pace: {min_per_km} min/km")
    print(f"Pace: {min_per_mile} min/mile")


def main():
    distance = ask_distance()
    if distance is None:
        return

    predicted_time = ask_time(distance)
    if predicted_time is None:
        return

    output_pace(calculate_pace(distance, predicted_time))


if __name__ == "__main__":
    main()
