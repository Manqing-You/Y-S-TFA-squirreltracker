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
