import os

def get_current_user():
    return os.getlogin()

if __name__ == "__main__":
    user = get_current_user()
    print(f"Current user: {user}")