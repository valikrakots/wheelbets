import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")


import django

django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob)

scheduler.start()
