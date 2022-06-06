import math
import uuid
from threading import local
from types import SimpleNamespace

import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from event.models import Event
from game.models import Game
from localization.models import Localization
from measure.models import Measure
from team.models import Team
from user.models import User
from prize.models import Prize


class Command(BaseCommand):

    def handle(self, *args,**options):

        olympics = pd.read_csv('athlete_events.csv')

        transaction.set_autocommit(False)

        users = set()
        measurements = set()
        teams = set()
        games = set()
        localizations = set()
        events = set()
        prizes = set()

        for index, row in olympics.iterrows():
            print(row['ID'])

            # user = User.objects.filter(id=row['ID']).first()
            user_data ={
                'id':int(row['ID']),
                'name':row['Name'],
                'sex':row['Sex']
            }
            user = User(**user_data)
       
            measure_data = {
                'heigth':row['Height'] if not math.isnan(row['Height']) else None,
                'wheight':row['Weight'] if not math.isnan(row['Weight']) else None,
                'age':row['Age']
            }

            measure = Measure(**measure_data, user = user)
            measurements.add(measure)

            team_data = {
                'name':row['Team'],
                'ndc':row['NOC']
            }

            team_filter = (t for t in teams if t.name == team_data['name'])
            team = next(team_filter, Team(**team_data))
            teams.add(team)

            user.team = team

            users.add(user)
            
            game_data = {
                'name':row['Games'],
                'year':row['Year'],
                'season':row['Season']
            }


            game = Game(**game_data)
            games.add(game)

            game = next(g for g in games if g.name == game.name and g.year == game.year)

            game.teams_list.append(team)
            
            localization = Localization()
            localization.city=row['City']
            localizations.add(localization)

            localization = next(l for l in localizations if l.city == localization.city)

            event_data ={
                'name':row['Event'],
                'sport':row['Sport']
            }
            
            event = Event(**event_data, localization = localization, game = game)
            events.add(event)

            # event = next(e for e in events if e.name == event.name and e.game.uuid == event.game.uuid)

            event.users_list.append(user)


            if row['Medal'] != 'NA':
                prize = Prize()
                prize.medal = row['Medal']
                prize.user = user
                prize.event = event
                prizes.add(prize)

            
        
        Team.objects.bulk_create(teams)
        User.objects.bulk_create(users)

        Game.objects.bulk_create(games)
        for g in games:
            g.teams.add(*g.teams_list)
        
        Measure.objects.bulk_create(measurements)
        Localization.objects.bulk_create(localizations)

        Event.objects.bulk_create(events)
        for e in events:
            e.users.add(*e.users_list)

        Prize.objects.bulk_create(prizes)


        transaction.commit()
            
