import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")


import django

django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, 'date', run_date='2020-13-07 10:49:17')

scheduler.start()
