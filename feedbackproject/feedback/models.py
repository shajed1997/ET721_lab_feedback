from django.db import models


# Model for an item
class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for feedback
class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.item.name} - {self.rating}"
