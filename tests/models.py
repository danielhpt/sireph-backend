from django.db import models


class Test(models.Model):
    type = models.CharField(max_length=15)


class TestAction(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    action = models.CharField(max_length=20, blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True, blank=True, null=True)


class TestOccurrence(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )
    occurrence_id = models.IntegerField(blank=True, null=True)
