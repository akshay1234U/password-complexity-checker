import re


def assess_password_strength(password):
  
    score = 0
    feedback = []
    
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
   
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    
    if score == 5:
        strength = "Strong"
        feedback.append("Great! Your password is strong.")
    elif score >= 3:
        strength = "Moderate"
        feedback.append("Your password is moderate. Consider making it stronger.")
    else:
        strength = "Weak"
        feedback.append("Your password is weak. You need to improve it.")
    
   
    return strength, feedback


def display_feedback(password):
    strength, feedback = assess_password_strength(password)
    print(f"Password strength: {strength}")
    for note in feedback:
        print(f"- {note}")


if __name__ == "__main__":
    password = input("Enter your password: ")
    display_feedback(password)
