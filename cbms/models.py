from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER_CHOICE = [
    ('1', '女性'),
    ('2', '男性'),
]


class Costomer(models.Model):
    name = models.CharField('名前', max_length=20)
    gender = models.CharField('性別', choices=GENDER_CHOICE, max_length=2)
    age = models.IntegerField('年齢')

    def __str__(self):
        return str(self.name) + '(' + str(self.age) + ')'

class Genre(models.Model):
    subject = models.CharField('科目', max_length=30)
    base_fee = models.IntegerField('基本料金')
    charge_fee = models.IntegerField('従量料金')

    def __str__(self):
        return str(self.subject)

class History(models.Model):
    costomer = models.ForeignKey(Costomer, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    time = models.IntegerField('受講時間', validators=[MinValueValidator(1), MaxValueValidator(12)])
    date = models.DateField('受講日')


    def __str__(self):
        return 'History:id=' + str(self.id) + ', ' + '受講時間=' + str(self.time) + ', ' + '受講日:' +  str(self.date) + ', ' + '請求金額=' + str(self.billing)
