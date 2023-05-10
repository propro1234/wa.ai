from apscheduler.schedulers.blocking import BlockingScheduler
from microft import chat

sched = BlockingScheduler()

sched = add_job(chat, 'interval', seconds=0)

sched.start()