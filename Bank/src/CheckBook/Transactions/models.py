from django.db import models

# Create your models here.

class Account(models.Model):
    First_Name = models.CharField(max_length=50, null=False, blank=True)
    Last_Name = models.CharField(max_length=50, null=False, blank=True)
    Starting_Balance = models.DecimalField(max_digits=10000, decimal_places=2, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Last_Name + ' ' + self.First_Name


Types = {
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal')
}


class Transaction(models.Model):
    Date_of_Transaction = models.DateField()
    Type = models.CharField(max_length=60, choices=Types)
    Amount = models.DecimalField(max_digits=1000, decimal_places=2, null=False, blank=True)
    Description = models.TextField(max_length=200, default='')
    Account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()