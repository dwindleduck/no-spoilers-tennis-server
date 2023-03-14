from django.db import models
from django.contrib.auth import get_user_model

class WatchedMatchCard(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    match = models.ForeignKey(
        "Match",
        on_delete=models.CASCADE
    )
    spoil_results = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
