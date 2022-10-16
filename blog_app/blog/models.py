from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse


teams = (
    ("Arizona Cardinals", "Arizona Cardinals"),
    ("Atlanta Falcons", "Atlanta Falcons"),
    ("Baltimore Ravens", "Baltimore Ravens"),
    ("Buffalo Bills", "Buffalo Bills"),
    ("Carolina Panthers", "Carolina Panthers"),
    ("Chicago Bears", "Chicago Bears"),
    ("Cincinnati Bengals", "Cincinnati Bengals"),
    ("Cleveland Browns", "Cleveland Browns"),
    ("Dallas Cowboys", "Dallas Cowboys"),
    ("Denver Broncos", "Denver Broncos"),
    ("Detroit Lions", "Detroit Lions"),
    ("Green Bay Packers", "Green Bay Packers"),
    ("Houston Texans", "Houston Texans"),
    ("Indianapolis Colts", "Indianapolis Colts"),
    ("Jacksonville Jaguars", "Jacksonville Jaguars"),
    ("Kansas City Chiefs", "Kansas City Chiefs"),
    ("Las Vegas Raiders", "Las Vegas Raiders"),
    ("Los Angeles Chargers", "Los Angeles Chargers"),
    ("Los Angeles Rams", "Los Angeles Rams"),
    ("Miami Dolphins", "Miami Dolphins"),
    ("Minnesota Vikings", "Minnesota Vikings"),
    ("New England Patriots", "New England Patriots"),
    ("New Orleans Saints", "New Orleans Saints"),
    ("New York Giants", "New York Giants"),
    ("New York Giants", "New York Jets"),
    ("Philadelphia Eagles", "Philadelphia Eagles"),
    ("Pittsburgh Steelers", "Pittsburgh Steelers"),
    ("San Francisco 49ers", "San Francisco 49ers"),
    ("Seattle Seahawks", "Seattle Seahawks"),
    ("Tampa Bay Buccaneers", "Tampa Bay Buccaneers"),
    ("Tennessee Titans", "Tennessee Titans"),
    ("Washington Commanders", "Washington Commanders"),
)


class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    week = models.IntegerField(default=1)
    team = models.CharField(max_length=50, choices=teams, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
