from django.db import models


size_choice = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)
friendliness_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

trainability_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)
sheddingamount_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

exerciseneeds_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=size_choice)
    friendliness = models.CharField(max_length=10, choices=friendliness_choice)
    trainability = models.CharField(max_length=10, choices=trainability_choice)
    sheddingamount = models.CharField(max_length=10, choices=sheddingamount_choice)
    exerciseneeds = models.CharField(max_length=10, choices=exerciseneeds_choice)

