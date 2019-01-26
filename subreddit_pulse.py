from subreddit_pulse.subreddit_monitor import SubredditMonitor
import time


def watch_subreddit():
    """Main entry point"""
    logfile = _create_logfile()
    monitor = SubredditMonitor()
    monitor.logfile = logfile
    monitor.subreddit_title_monitor('askreddit')


def _create_logfile():
    """Creates a new logfile.

    This log file is used to log submissions that meet
    certain criteria. A new log file is generated each
    time the program is executed. The logfile name is
    of the form YearMonthDay-HourMinuteSecond.csv
    """
    time_string = time.strftime("%Y%m%d-%H%M%S")
    with open(f"{time_string}.csv", 'w') as f:
        f.write("Title,ID,URL,Date_Created,Body\n")
    print("Log file created")
    return f"{time_string}.csv"


if __name__ == "__main__":
    watch_subreddit()
