from django.db import models
# from django.contrib.auth import get_user_model

class Match(models.Model):

    date_time = models.DateTimeField()

    league = models.CharField(max_length=100)
    competition = models.CharField(max_length=100)

    team1name = models.CharField(max_length=100)
    team2name = models.CharField(max_length=100)

    team1score = models.CharField(max_length=100)
    #break scores into sets.....
    team2score = models.CharField(max_length=100)

    winner = models.CharField(max_length=100, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This must return a string
        return f"{self.team1name}' v {self.team2name} at {self.date_time}"
    def as_dict(self):
        return {
            'id': self.id,
            'date_time': self.date_time,
            'league': self.league,
            'competition': self.competition,
            'team1name': self.team1name,
            'team2name': self.team1name,
            'team1score': self.team1score,
            'team2score': self.team2score,
            'winner': self.winner,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            
        }