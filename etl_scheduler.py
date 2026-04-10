# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# import pytz
#
# from join_tables_etl import run_etl
#
# # Timezone
# IST = pytz.timezone("Asia/Kolkata")
#
# scheduler = BlockingScheduler(timezone=IST)
#
# # Schedule job at 2 PM IST daily
# scheduler.add_job(
#     run_etl,
#     # trigger=CronTrigger(hour=19, minute=0)
#     trigger=CronTrigger(minute="*/1")
# )
#
# # print("Scheduler started... Waiting for 7 PM IST job.")
# print("Scheduler started... runs every minute")
#
#
# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     print("Scheduler stopped.")

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from join_tables_etl import run_etl

IST = pytz.timezone("Asia/Kolkata")

scheduler = BackgroundScheduler(timezone=IST)

scheduler.add_job(
    run_etl,
    trigger=CronTrigger(minute="*/1")  # testing
)

def start_scheduler():
    if not scheduler.running:
        print("Scheduler started... runs every minute")
        scheduler.start()
    else:
        print("Scheduler already running")