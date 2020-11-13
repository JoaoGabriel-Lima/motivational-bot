from apscheduler.schedulers.blocking import BlockingScheduler
from frog2 import send_time


sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
import frog2
sched.add_job(send_time, 'cron', second=00)

sched.start()