import string

def check_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters, preferably 12 or more.")

    # Check lowercase
    has_lower = False
    for ch in password:
        if ch >= 'a' and ch <= 'z':
            has_lower = True
            break

    if has_lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check uppercase
    has_upper = False
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
            break

    if has_upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check digits
    has_digit = False
    for ch in password:
        if ch >= '0' and ch <= '9':
            has_digit = True
            break

    if has_digit:
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    special = False

    for ch in password:
        if ch in string.punctuation:
            special = True
            break

    if special:
        score += 1
    else:
        suggestions.append("Add special characters such as @, #, $, %, !.")

    # Check repeated characters
    repeated = False

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            repeated = True
            break

    if repeated:
        score -= 1
        suggestions.append("Avoid repeated characters like 'aaa' or '111'.")

    # Strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    elif score <= 5:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return strength, suggestions


# Main program
password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\n--- Password Strength Analyzer ---")
print("Password Strength:", strength)

if len(suggestions) == 0:
    print("Your password meets all the basic security requirements.")
else:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)