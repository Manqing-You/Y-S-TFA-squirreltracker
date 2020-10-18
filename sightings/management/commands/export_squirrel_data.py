from sightings.models import sightings

from django.core.management.base import BaseCommand, CommandError
from django.db import models

import csv

class Command(BaseCommand):
  help = 'Export the database'

  # 接收参数
  def add_arguments(self, parser):
      parser.add_argument('path', type=str, help='file path')

  def handle(self, *args, **options):
      path = options['path']
      out = open(path, 'a', newline='')

      ob = sightings.objects.all()
      lis = ob.values_list()
      fields = sightings.getattrlist()

      csv_write = csv.writer(out, dialect='excel')
      csv_write.writerow(fields)
      for i in lis:
          csv_write.writerow(i)


