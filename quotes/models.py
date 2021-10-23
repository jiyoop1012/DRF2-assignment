from django.db import models

class Quote(models.Model):
    quote_author = models.CharField(max_length=60)
    quote_body   = models.CharField(max_length=1000)
    context      = models.TextField()
    source       = models.CharField(max_length=1000)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_body
