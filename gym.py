import calendar
import datetime
import random


app = "FitTrack"


def read_number(prompt, minimum, maximum):
    """Ask for a number until it is inside the allowed range."""
    while True:
        answer = input(prompt).strip()

        if not answer.replace(".", "", 1).isnumeric():
            print("Please enter a number, such as 68.5.")
            continue

        number = float(answer)
        if minimum <= number <= maximum:
            return number
        print(f"Enter a value between {minimum} and {maximum}.")


def calculate_bmi(weight, height):
    """Work out BMI from kilograms and centimetres."""
    height = height / 100
    return weight / (height * height)


def get_suggestions(bmi, age, goal, has_medical_history, medical_history):
    """Print a few general suggestions for the person."""
    print("\nBMI for your selected goal:", round(bmi, 1))

    if age < 18:
        print("1. Talk with a parent or guardian and a health professional about your growth.")
        print("2. Choose enjoyable movement, such as walking, games, or a sport.")
        print("3. Eat regular meals with a mix of foods; avoid restrictive diets.")
    elif bmi < 18.5:
        print("1. Ask a health professional for personal advice before changing your diet.")
        print("2. Aim for regular meals with grains, protein foods, fruit, and vegetables.")
        print("3. Try gentle strength exercises with rest days between sessions.")
    elif bmi < 25:
        print("1. Keep meals varied, with vegetables, fruit, whole grains, and protein.")
        print("2. Mix activities you enjoy, such as brisk walks and light strength work.")
        print("3. Build a routine you can keep up, and make room for rest.")
    elif bmi < 30:
        print("1. Choose filling meals with vegetables, beans, whole grains, and protein.")
        print("2. Start with regular walks and add gentle strength training if comfortable.")
        print("3. Small, steady habits are more useful than crash diets or punishing workouts.")
    else:
        print("1. A doctor or registered dietitian can help set a safe, personal plan.")
        print("2. If movement feels comfortable, begin with short, low-impact walks.")
        print("3. Build meals around varied whole foods; skip extreme diets and quick fixes.")

    print("\nEquipment and exercises for your goal")
    if goal == "gain":
        print("Equipment: dumbbells, a bench, and a barbell if available.")
        print("Exercises: squats, bench press, shoulder press, and rows.")
    elif goal == "lose":
        print("Equipment: walking shoes, a skipping rope, and an exercise mat.")
        print("Exercises: brisk walking, cycling, step-ups, and bodyweight exercises.")
    elif goal == "abs":
        print("Equipment: an exercise mat, a pull-up bar, and a cable machine.")
        print("Exercises: planks, crunches, leg raises, and mountain climbers.")
    else:
        print("Equipment: light dumbbells, resistance bands, and an exercise mat.")
        print("Exercises: lunges, push-ups, rows, planks, and easy cardio.")

    if has_medical_history:
        print("\nMedical history provided:", medical_history)
        print("Precaution: speak with a doctor or physiotherapist before exercising.")
        print("Avoid heavy lifting, maximum-effort exercises, and any movement that causes pain.")
        print("Do not do high-impact exercises until a health professional says they are safe.")


def profile():
    """Ask for the details needed to make a profile."""
    print("\nLet's set up your profile.")

    while True:
        name = input("What should we call you? ").strip()
        if name:
            break
        print("Please enter a name so we can make your profile.")

    while True:
        age_text = input("How old are you? ").strip()
        if not age_text.isdigit():
            print("Enter your age as a whole number.")
            continue

        age = int(age_text)
        if 1 <= age <= 120:
            break
        print("Please enter an age from 1 to 120.")

    weight = read_number("Your weight in kilograms: ", 10, 500)
    height = read_number("Your height in centimetres: ", 50, 250)

    print("\nChoose your main goal:")
    print("1. Gain weight and build strength")
    print("2. Lose weight and improve fitness")
    print("3. Maintain my current weight")
    print("4. Work on my abs")

    while True:
        goal_choice = input("Enter 1, 2, 3, or 4: ").strip()
        if goal_choice == "1":
            goal = "gain"
            break
        if goal_choice == "2":
            goal = "lose"
            break
        if goal_choice == "3":
            goal = "maintain"
            break
        if goal_choice == "4":
            goal = "abs"
            break
        print("Please choose one of the four options.")

    while True:
        history_answer = input("Do you have any medical history? (yes/no): ").strip().lower()
        if history_answer == "yes":
            medical_history = input("Please describe it briefly: ").strip()
            if medical_history:
                has_medical_history = True
                break
            print("Please type a short description.")
        elif history_answer == "no":
            has_medical_history = False
            medical_history = "None reported"
            break
        else:
            print("Please answer yes or no.")

    return {
        "name": name,
        "age": age,
        "weight_kg": weight,
        "height_cm": height,
        "goal": goal,
        "has_medical_history": has_medical_history,
        "medical_history": medical_history,
        "created": datetime.date.today(),
    }



print(f"\t\t\tWelcome to {app}")
print("A simple starting point for your fitness routine")
welcome_number = random.randint(1, 3)
if welcome_number == 1:
    print("Let's get started.")
elif welcome_number == 2:
    print("A few simple details will help us begin.")
else:
    print("Small steps can build a useful routine.")

while True:
    user_profile = profile()

    bmi = calculate_bmi(user_profile["weight_kg"], user_profile["height_cm"])
    """Show the profile and the advice from the program."""
    print("\nYour Liftbite profile")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print("Weight:", user_profile["weight_kg"], "kg")
    print("Height:", user_profile["height_cm"], "cm")
    print("Goal:", user_profile["goal"])
    print("Medical history:", user_profile["medical_history"])
    day = calendar.day_name[user_profile["created"].weekday()]
    print(f"Profile created: {day}, {user_profile['created']}")
    print("\nBMI:", round(bmi, 1))
    if user_profile["age"] < 18:
        print("BMI note: the adult categories are not meant for people under 18.")
        category = "Not used for people under 18"
    else:
        if bmi < 18.5:
            category = "Below the usual adult range"
        elif bmi < 25:
            category = "Within the usual adult range"
        elif bmi < 30:
            category = "Above the usual adult range"
        else:
            category = "Well above the usual adult range"
        print(f"General category: {category}")

    print("\nA few ideas to get started")
    get_suggestions(
        bmi,
        user_profile["age"],
        user_profile["goal"],
        user_profile["has_medical_history"],
        user_profile["medical_history"],
    )

    print("\nA quick note")
    print("BMI is a rough screening measure, not a diagnosis or a full picture")
    print("of health. It does not account for muscle, body composition, or every")
    print("person's circumstances. Check with a health professional for advice")
    print("about your own health, especially before changing food or exercise.")

    print(f"\nThanks for stopping by {app}, {user_profile['name']}!")

    receipt_time = datetime.datetime.now()
    print("\nReceipt")
    print("Name:", user_profile["name"])
    print("Date:", user_profile["created"])
    print("Time:", receipt_time.strftime("%H:%M:%S"))
    print("Weight:", user_profile["weight_kg"], "kg")
    print("Height:", user_profile["height_cm"], "cm")
    print("Goal:", user_profile["goal"])
    print("Medical history:", user_profile["medical_history"])
    print("BMI:", round(bmi, 1))
    print("Category:", category)
    print("Thank you for using", app)

    again = input("\nDo you want another session? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break