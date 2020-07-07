import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")


from apscheduler.schedulers.background import BackgroundScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()
