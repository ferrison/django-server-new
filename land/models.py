from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    imei = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username

    def get(self):
        ret = {}
        ret['fname'] = self.user_info.first_name
        ret['sname'] = self.user_info.last_name
        return ret


class fuck(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class nom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class user_info(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nom = models.ForeignKey(nom, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class pp(models.Model):
    name = models.CharField(max_length=50)
    nom = models.ForeignKey(nom, on_delete=models.CASCADE)
    fuck = models.ForeignKey(fuck, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class mark(models.Model):
    mark = models.IntegerField(default=0)
    user_info = models.ForeignKey(user_info, on_delete=models.CASCADE)
    pp = models.ForeignKey(pp, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mark)


class time(models.Model):
    nom = models.OneToOneField(nom,on_delete=models.CASCADE,primary_key=True)
    start=models.DateTimeField()
    end=models.DateTimeField()

    def __str__(self):
        return str(self.nom)
