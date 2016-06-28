from django.db import models

class Account(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text

class Category(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text

    class Meta:
        verbose_name_plural = "categories"

class Person(models.Model):
    name_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name_text

class Transact(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        result = "Account: " + self.account.name_text
        if (self.category is not None):
            result += " | Category: " + self.category.name_text
        if (self.person is not None):
            result += " | Person: " + self.person.name_text
        return result
