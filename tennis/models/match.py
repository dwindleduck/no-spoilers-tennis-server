from django.db import models
# from django.contrib.auth import get_user_model

class Match(models.Model):

    date_time = models.DateTimeField()

    league = models.CharField(max_length=100)
    competition = models.CharField(max_length=100)

    T1name = models.CharField(max_length=100)
    T2name = models.CharField(max_length=100)

    #T1 Overall Set Score
    T1SetScore = models.CharField(max_length=100)
    #T2 Overall Set Score
    T2SetScore = models.CharField(max_length=100)
    #T1 Set 1
    T1Set1 = models.CharField(max_length=100)
        ### add in tiebreak scores
    #T2 Set 1
    T2Set1 = models.CharField(max_length=100)
    #T1 Set 2
    T1Set2 = models.CharField(max_length=100)
    #T2 Set 2
    T2Set2 = models.CharField(max_length=100)
    #T1 Set 3
    T1Set3 = models.CharField(max_length=100)
    #T2 Set 3
    T2Set3 = models.CharField(max_length=100)
    #T1 Set 4
    T1Set4 = models.CharField(max_length=100)
    #T2 Set 4
    T2Set4 = models.CharField(max_length=100)
    #T1 Set 5
    T1Set5 = models.CharField(max_length=100)
    #T2 Set 5
    T2Set5 = models.CharField(max_length=100)


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
            'T1name': self.T1name,
            'T2name': self.T2name,
            'T1SetScore': self.T1SetScore,
            'T2SetScore': self.T2SetScore,
            'T1Set1': self.T1Set1,
            'T2Set1': self.T2Set1,
            'T1Set2': self.T1Set2,
            'T2Set2': self.T2Set2,
            'T1Set3': self.T1Set3,
            'T2Set3': self.T2Set3,
            'T1Set4': self.T1Set4,
            'T2Set4': self.T2Set4,
            'T1Set5': self.T1Set5,
            'T2Set5': self.T2Set5,
            'winner': self.winner,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            
        }