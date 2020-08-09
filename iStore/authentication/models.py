"""
This module provides user profile  model.
"""

from django.db import models


# Create your models here.
class UserProfile(models.Model):
    """
    A user's profile.
        Attributes:
        FirstName (str): User's name
        LastName (str): User's surname
        BirthDate (date): User's birthday date
        RegistrationDate (datetime): User's registration date
    """
    FirstName = models.CharField(blank=True, max_length=30)
    LastName = models.CharField(blank=True, max_length=20)
    BirthDate = models.DateField(null=True)
    RegistrationDate = models.DateField(null=True)

    def __repr__(self):
        """
            :return: All information about user which is added.
        """
        return f"<User {self.FirstName}/{self.LastName}/{self.BirthDate}/{self.RegistrationDate}>"
