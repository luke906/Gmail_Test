from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler


##########################################################################################
class APS(object):
    # =====================================================================================
    def __init__(self):
        self._interval_jobs = {}
        self._cron_jobs = {}
        self._scheduler = None

    # =====================================================================================
    def add_interval_job(self, job, **kwargs):
        self._interval_jobs[job.__name__] = (job, kwargs)
        return len(self._interval_jobs)

    # =====================================================================================
    def add_cron_job(self, job, **kwargs):
        self._cron_jobs[job.__name__] = (job, kwargs)
        return len(self._cron_jobs)

    # =====================================================================================
    def start_scheduler(self):
        if len(self._interval_jobs) + len(self._cron_jobs) <= 0:
            return False
        self._scheduler = Scheduler()
        for job, kwargs in self._interval_jobs.values():
            self._scheduler.add_job(job, 'interval', id=job.__name__, **kwargs)
        for job, kwargs in self._cron_jobs.values():
            self._scheduler.add_job(job, 'cron', id=job.__name__, **kwargs)
        self._scheduler.start()
        return True

    # =====================================================================================
    def stop_scheduler(self):
        if self._scheduler is not None:
            print("shut down")
            self._scheduler.shutdown()


##########################################################################################
class mySchedule(APS):
    # =====================================================================================
    def __init__(self):
        APS.__init__(self)

    # =====================================================================================
    def my_interval(self):
        print('[%s] my_interval' % datetime.now())

    # =====================================================================================
    def my_cron(self):
        print('[%s] my_cron' % datetime.now())

    # =====================================================================================
    def add_schedule(self):
        self.add_interval_job(self.my_interval, seconds=3)
        self.add_cron_job(self.my_cron, second='*/10')


##########################################################################################
if __name__ == '__main__':
    mys = mySchedule()
    mys.add_schedule()
    mys.start_scheduler()
    for i in range(5):
        sleep(1)
        print('[%s] in main sleep after start scheduler' % i)
    mys.stop_scheduler()

    print("end")