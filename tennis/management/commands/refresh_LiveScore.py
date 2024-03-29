# Currently Unused

# For automating LiveScore Requests

# Adapted from https://pypi.org/project/django-apscheduler/

from ...LiveScore_Requests import list_by_date

import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from datetime import datetime, timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)


def refresh_live_scores():
    # now = datetime.now()
    # this is in GMT
    now = timezone.now()
    day = now.strftime("%Y%m%d")
    hour = now.strftime("%H")

    print("Now: ", now)
    print("Executed refresh_live_scores command at ", day)
    print("Hour: ", hour)

    # 5 calls every 12 hours,
    # 6 more single day calls every 3 hours
    # 16 total API calls per day
    
    # if hour == "00" or hour == "12":
    #     # loop to call previous 1 days through next 3 days
    #   call_list = [now - timedelta(days=x) for x in range(-3, 2)]
    #   for date in call_list:
    #       formattedDate = date.strftime("%Y%m%d")
    #       print(formattedDate)
    #       # LiveScore_Request
    #       list_by_date(formattedDate)
    # else:
    #     print(day)
    #     # LiveScore_Request
    #     list_by_date(day)

    call_list = [now - timedelta(days=x) for x in range(-3, 2)]
    for date in call_list:
        formattedDate = date.strftime("%Y%m%d")
        print(formattedDate)
        # LiveScore_Request
        list_by_date(formattedDate)

    print("End of scheduled API call")    
        
 
    



# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way. 
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      refresh_live_scores,
      trigger=CronTrigger(hour="*/3"),  # Every 3 hours
      # trigger=CronTrigger(second="*/10"),  # Every 10 seconds
      # trigger=CronTrigger(minute="*/2"),  # Every 2 minutes
      id="refresh_live_scores",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'refresh_live_scores'.")

    scheduler.add_job(
      delete_old_job_executions,
      trigger=CronTrigger(
        day_of_week="mon", hour="00", minute="00"
      ),  # Midnight on Monday, before start of the next work week.
      id="delete_old_job_executions",
      max_instances=1,
      replace_existing=True,
    )
    logger.info(
      "Added weekly job: 'delete_old_job_executions'."
    )

    try:
      logger.info("Starting scheduler...")
      scheduler.start()
    except KeyboardInterrupt:
      logger.info("Stopping scheduler...")
      scheduler.shutdown()
      logger.info("Scheduler shut down successfully!")