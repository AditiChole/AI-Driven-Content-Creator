from firebase_auth import auth

def signup_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user["idToken"])
        return True, "Account created. Please verify your email."
    except Exception as e:
        error = str(e)
        if "EMAIL_EXISTS" in error:
            return False, "Email already exists"
        return False, "Signup failed"

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        info = auth.get_account_info(user["idToken"])
        if not info["users"][0]["emailVerified"]:
            return False, "Please verify your email"
        return True, "Login successful"
    except Exception as e:
        error = str(e)
        if "INVALID_PASSWORD" in error:
            return False, "Incorrect password"
        if "EMAIL_NOT_FOUND" in error:
            return False, "Email not found"
        return False, "Login failed"

# ------------------- NEW: Update Password -------------------
def update_password(email, current_password, new_password):
    """
    Re-authenticate user first, then update password.
    """
    try:
        # Sign in to re-authenticate
        user = auth.sign_in_with_email_and_password(email, current_password)
        auth.update_password(user['idToken'], new_password)
        return True, "Password updated successfully"
    except Exception as e:
        error = str(e)
        if "INVALID_PASSWORD" in error:
            return False, "Current password is incorrect"
        return False, "Password update failed"

