from django.db import models
from django.core.validators import RegexValidator

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name="Client first_name", max_length=65,
                                  blank=False)
    last_name = models.CharField(verbose_name="Client last_name", max_length=65,
                                 blank=False)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$",message='Invalid Phone Number')
    phone_number = models.CharField(validators=[phoneNumberRegex], verbose_name="Client phone_number", max_length=65,
                                    blank=False)

    doc = models.DateField(verbose_name="Client DOC",
                          blank=False)

    def __str__(self):
        return self.first_name

    class Meta:
        pass