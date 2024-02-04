from djoser import email

"""
Paths to HTML files for managing user's credentials through email.
"""

class PasswordResetEmail(email.PasswordResetEmail):
    """ Resets the user's password """
    template_name = "email/password_reset.html"


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    """ Confirmation of change password action by the user. """
    template_name = "email/password_changed_confirmation.html"


class UsernameChangedConfirmationEmail(email.UsernameChangedConfirmationEmail):
    """ Confirmation of change username action by the user. """
    template_name = "email/username_changed_confirmation.html"


class UsernameResetEmail(email.UsernameResetEmail):
    """ Resets user's username """
    template_name = "email/username_reset.html"
