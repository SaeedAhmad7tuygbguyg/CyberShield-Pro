import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8: score += 1
    else: feedback.append("Make it at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): score += 1
    else: feedback.append("Use both Uppercase and Lowercase letters.")
    
    if re.search(r"\d", password): score += 1
    else: feedback.append("Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    else: feedback.append("Include a special character (e.g., @, #, $).")
    
    return {"score": score, "feedback": feedback}

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range(16))