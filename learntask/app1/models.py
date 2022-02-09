from django.db import models





class Teams(models.Model):
    team_name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.team_name

    class Merta:
        ordering=['name']


class Users(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    team_id = models.IntegerField()
    is_active=models.ForeignKey(Teams,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Merta:
        ordering=['name']