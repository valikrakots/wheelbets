import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")


import django

django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, 'date', run_date=datetime(2020, 07, 14, 8, 35, 17))

scheduler.start()
