from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=128, unique=True, default="Chat")
    users_online = ArrayField(
        models.CharField(max_length=16, blank=True, null=True),
        default=list,
        null=True,
        blank=True
    )

    """ Retrieve the total count of online people """
    def get_online_count(self):
        return self.users_online.count()

    """ Getting all the users online """
    def get_online_users(self):
        return list(self.users_online)

    
    def already_exists(self, username: str) -> bool:
        return username in self.users_online

    
    def user_joined(self, username: str) -> None:
        """
            Function that adds a new username to the users online list
            :param username: The string containing the current user who has joined the Room
            :return None:
        """
        if not self.already_exists(username):
            self.users_online.append(username)
            self.save()

    
    def user_left(self, username: str) -> None:
        """
            Function that removes a given username from the users online list
            :param username: The string containing the current user who left the Room
            :return None:
        """
        if self.already_exists(username):
            self.users_online.remove(username)
            self.save()


class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'

    
