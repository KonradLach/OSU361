#Konrad Lach
#OSU 361 Project

def calculate_531_max(weight):
    max_weight = weight * 0.9

    return max_weight

def calculate_one_rep_max(weight):
    one_rep_max = weight * (1 + 0.0333 * 5)
    return one_rep_max

def myround(x, base=5):
    return base * round(x/base)

def calculate_program():
    print("Enter your 1 rep max for each exercise:")
    bench_press = float(input("Bench Press (in lbs): "))
    dead_lift = float(input("Deadlift (in lbs): "))
    shoulder_press = float(input("Shoulder Press (in lbs): "))
    squat = float(input("Squat (in lbs): "))

    bench_weight = calculate_531_max(bench_press)
    deadlift_weight = calculate_531_max(dead_lift)
    shoulder_press_weight = calculate_531_max(shoulder_press)
    squat_weight = calculate_531_max(squat)

    print("\nYour 5/3/1 lifting program:")
    print("Week 1:")
    print(f"Bench Press:\n {myround(bench_weight*.65)} lbs x 5 reps\n {myround(bench_weight*.75)} lbs x 5 reps \n {myround(bench_weight*.85)} lbs x 5+ reps")
    print(f"Deadlift:\n {myround(deadlift_weight*.65)} lbs x 5 reps\n {myround(deadlift_weight*.75)} lbs x 5 reps \n {myround(deadlift_weight*.85)} lbs x 5+ reps")
    print(f"Shoulder Press:\n {myround(shoulder_press_weight*.65)} lbs x 5 reps\n {myround(shoulder_press_weight*.75)} lbs x 5 reps \n {myround(shoulder_press_weight*.85)} lbs x 5+ reps")
    print(f"Squat:\n {myround(squat_weight*.65)} lbs x 5 reps\n {myround(squat_weight*.75)} lbs x 5 reps \n {myround(squat_weight*.85)} lbs x 5+ reps")

    print("\nWeek 2:")
    print(f"Bench Press:\n {myround(bench_weight*.70)} lbs x 3 reps\n {myround(bench_weight*.80)} lbs x 3 reps \n {myround(bench_weight*.90)} lbs x 3+ reps")
    print(f"Deadlift:\n {myround(deadlift_weight*.70)} lbs x 3 reps\n {myround(deadlift_weight*.80)} lbs x 3 reps \n {myround(deadlift_weight*.90)} lbs x 3+ reps")
    print(f"Shoulder Press:\n {myround(shoulder_press_weight*.70)} lbs x 3 reps\n {myround(shoulder_press_weight*.80)} lbs x 3 reps \n {myround(shoulder_press_weight*.90)} lbs x 3+ reps")
    print(f"Squat:\n {myround(squat_weight*.70)} lbs x 3 reps\n {myround(squat_weight*.80)} lbs x 3 reps \n {myround(squat_weight*.90)} lbs x 3+ reps")

    print("\nWeek 3:")
    print(f"Bench Press:\n {myround(bench_weight*.75)} lbs x 5 reps\n {myround(bench_weight*.85)} lbs x 3 reps \n {myround(bench_weight*.95)} lbs x 1+ reps")
    print(f"Deadlift:\n {myround(deadlift_weight*.75)} lbs x 5 reps\n {myround(deadlift_weight*.85)} lbs x 3 reps \n {myround(deadlift_weight*.95)} lbs x 1+ reps")
    print(f"Shoulder Press:\n {myround(shoulder_press_weight*.75)} lbs x 5 reps\n {myround(shoulder_press_weight*.85)} lbs x 3 reps \n {myround(shoulder_press_weight*.95)} lbs x 1+ reps")
    print(f"Squat:\n {myround(squat_weight*.75)} lbs x 5 reps\n {myround(squat_weight*.85)} lbs x 3 reps \n {myround(squat_weight*.95)} lbs x 1+ reps")

def calculate_maxes():
    print("Enter your lifting weight for 5 reps:")
    bench_press = float(input("Bench Press (in lbs): "))
    dead_lift = float(input("Deadlift (in lbs): "))
    shoulder_press = float(input("Shoulder Press (in lbs): "))
    squat = float(input("Squat (in lbs): "))

    one_rep_max_bench = calculate_one_rep_max(bench_press)
    one_rep_max_deadlift = calculate_one_rep_max(dead_lift)
    one_rep_max_shoulder = calculate_one_rep_max(shoulder_press)
    one_rep_max_squat = calculate_one_rep_max(squat)

    print("\nYour calculated one rep maxes:")
    print(f"Bench Press: {one_rep_max_bench:.2f} lbs")
    print(f"Deadlift: {one_rep_max_deadlift:.2f} lbs")
    print(f"Shoulder Press: {one_rep_max_shoulder:.2f} lbs")
    print(f"Squat: {one_rep_max_squat:.2f} lbs")

def main():
    print("Welcome to the 5/3/1 Calculator!")
    print("If you know your 1 rep max for each lift, press 1.")
    print("If you want to calculate your 1 rep maxes, press 2.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        calculate_program()
    elif choice == "2":
        calculate_maxes()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()