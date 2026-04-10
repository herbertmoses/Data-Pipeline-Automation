import threading
import time
from etl_scheduler import start_scheduler
from folder_watcher import start_watcher


def run_scheduler():
    print("Starting ETL Scheduler...")
    start_scheduler()


def run_watcher():
    print("🚀 Watcher started...")
    start_watcher()


if __name__ == "__main__":
    # Start watcher first
    t2 = threading.Thread(target=run_watcher)
    t2.start()

    time.sleep(3)

    # Start scheduler
    t1 = threading.Thread(target=run_scheduler)
    t1.start()

    print("Both services started...")

    t1.join()
    t2.join()