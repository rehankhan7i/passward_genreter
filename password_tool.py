import random
import re
import string

# ye sadharand rendom se jyada majbut hai
secure_random = random.SystemRandom()

COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "admin", "letmein", "iloveyou"]
def check_strength(password):
    """Score (0-6) aur feedback list return karta hai."""
    score = 0
    feedback = []
    # yha pe password ki lenth 
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Kam se kam 8 characters rakho.")
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("12+ characters aur behtar hain.")

    # yha pe Character types
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Lowercase letter (a-z) add karo.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Uppercase letter (A-Z) add karo.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Number (0-9) add karo.")
    if re.search(r"[^\w\s]|_", password):
        score += 1
    else:
        feedback.append("Special character (!@#$%) add karo.")

    # ye code me  block me  comman words or jo nii kerna uske bareme btaye ga
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("Yeh bahut common password hai, bilkul use mat karo!")
    if re.search(r"(.)\1{2,}", password):
        score = max(score - 1, 0)
        feedback.append("Ek hi character 3 baar repeat mat karo (aaa, 111).")

    return score, feedback


def rating(score):
    if score <= 2:
        return "WEAK"
    if score <= 4:
        return "MEDIUM"
    return "STRONG"
def generate_password(length=12):
    length = max(length, 8)
    # Har type ka kam se kam ek character guarantee
    chars = [
        secure_random.choice(string.ascii_lowercase),
        secure_random.choice(string.ascii_uppercase),
        secure_random.choice(string.digits),
        secure_random.choice(string.punctuation),
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while len(chars) < length:
        chars.append(secure_random.choice(all_chars))
    secure_random.shuffle(chars)
    return "".join(chars)

def check_menu():
    pwd = input("Password daalo: ")
    if not pwd:
        print("Password khaali hai!")
        return
    score, feedback = check_strength(pwd)
    print(f"\nScore: {score}/6  ->  {rating(score)}")
    for tip in feedback:
        print(" -", tip)

def generate_menu():
    try:
        length = int(input("Password length (min 8, default 12): ") or 12)
    except ValueError:
        print("Number daalo! Default 12 use ho raha hai.")
        length = 12
    pwd = generate_password(length)
    score, _ = check_strength(pwd)
    print(f"\nGenerated password: {pwd}")
    print(f"Strength: {rating(score)} ({score}/6)")

def main():
    while True:
        print("\n=== Password Tool ===")
        print("1. Password strength check karo")
        print("2. Strong password generate karo")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            check_menu()
        elif choice == "2":
            generate_menu()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Galat choice, 1/2/3 daalo.")
if __name__ == "__main__":
    main()
