from squirrel.models import Squirrel

from django.core.management.base import BaseCommand, CommandError
from django.db import models

import csv

class Command(BaseCommand):
  help = 'Update the database of the day every morning'

  # 接收参数
  def add_arguments(self, parser):
      parser.add_argument('path', type=str, help='文件路径')

  def handle(self, *args, **options):
      path = options['path']  # 拿到参数的值
      out = open(path, 'a', newline='') #准备并打开 要存入数据的文件对象

      ob = Squirrel.objects.all() #获取squirrel表的全部数据对象
      lis = ob.values_list() #获取所有数据对象的值列表
      fields = Squirrel.getattrlist() #获取属性名列表

      csv_write = csv.writer(out, dialect='excel') #以Excel为模板
      csv_write.writerow(fields) #将字段名写入文件
      for i in lis:
          csv_write.writerow(i)


