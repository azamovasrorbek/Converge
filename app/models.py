from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __cl__(self):
        return f"{self.name}: {self.text[:20]}"