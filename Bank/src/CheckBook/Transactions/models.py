from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    initial_deposit = models.DecimalField(max_digits=10000, decimal_places=2, blank=True, null=False)

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


Types = {
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal')
}


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=60, choices=Types, default='')
    amount = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=False)
    description = models.TextField(max_length=200, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()