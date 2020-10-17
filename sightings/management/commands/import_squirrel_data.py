import csv
import datetime


from django.core.management.base import BaseCommand, CommandError
from django.db import models
from sightings.models import sightings

class Command(BaseCommand):
  help = 'Update the database of the day every morning'
  # 接收参数
  def add_arguments(self, parser):
      parser.add_argument('path', type=str, help='文件路径')

  def handle(self, *args, **options):
      path = options['path']  # 拿到参数的值
      print(path)
      with open(path) as fp:
          data = list(csv.DictReader(fp))
  def testboolean(str_):
              if str_ == 'true':
                  return 1
              else:
                  return 0
		              for i in data:
              detester = i['Date']
              date = datetime.datetime.strptime(detester,'%m%d%Y')
              #print(date)
              squirrel = sightings()
              squirrel.Latitude = i["Y"]
              squirrel.Longitude = i["X"]
              squirrel.Unique_Squirrel_ID = i["Unique Squirrel ID"]
              squirrel.Shift = i['Shift']
              squirrel.Date = date
              squirrel.Age = i['Age']
              squirrel.Primary_Fur_Color = i['Primary Fur Color']
              squirrel.Location = i['Location']
              squirrel.Specific_Location = i['Specific Location']
              squirrel.Running = testboolean(i['Running'])
              #print(i['Running'])
              #print(squirrel.Running)
              squirrel.Chasing = testboolean(i['Chasing'])
              squirrel.Climbing = testboolean(i['Climbing'])
              squirrel.Eating = testboolean(i['Eating'])
              squirrel.Foraging = testboolean(i['Foraging'])
              squirrel.Other_Activities = i['Other Activities']
              squirrel.Kuks = testboolean(i['Kuks'])
              squirrel.Quaas = testboolean(i['Quaas'])
              squirrel.Moans = testboolean(i['Moans'])
              squirrel.Tail_flags = testboolean(i['Tail flags'])
              squirrel.Tail_twitches = testboolean(i['Tail twitches'])
              squirrel.Approaches = testboolean(i['Approaches'])
              squirrel.Indifferent = testboolean(i['Indifferent'])
              squirrel.Runs_from = testboolean(i['Runs from'])
              squirrel.save() #保存到数据库
