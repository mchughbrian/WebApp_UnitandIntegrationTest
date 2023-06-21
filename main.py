class User:
    def __init__(self, username, password):
        """Initialize a User object with a username and password.

        Args:
        username (str): The user's username.
        password (str): The user's password.
        """
        self.username = username
        self.password = password

    def register(self):
        """Register the user in the database.

        This function doesn't have an implementation here,
        but in a full application it might interact with a database
        to create a new user entry.
        """
        pass

    def change_password(self, new_password):
        """Change the user's password.

        This function updates the user's password. In a real application,
        it would also need to ensure the change is reflected in the database.

        Args:
        new_password (str): The user's new password.
        """
        self.password = new_password


class Authentication:
    def __init__(self):
        """Initialize an Authentication object with no logged-in user."""
        self.logged_in_user = None

    def login(self, username, password):
        """Authenticate the user and log them in if the credentials are correct.

        This function doesn't have an implementation here,
        but in a full application it might check the credentials against a database,
        and if they match, set the logged_in_user to the corresponding user.

        Args:
        username (str): The username to log in with.
        password (str): The password to log in with.
        """
        pass

    def logout(self):
        """Log out the currently logged-in user.

        This sets the logged_in_user to None, indicating that no user is logged in.
        """
        self.logged_in_user = None
