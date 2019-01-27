from subreddit_pulse.subreddit_monitor import SubredditMonitor
import time
import click


@click.command()
@click.option('--subreddits',
              default='askreddit',
              help="Subreddits to monitor. Use '+' to join multiple.")
@click.option('--search_terms',
              default='keywords.dat',
              help="File containing search terms for monitoring subreddits.")
def watch_subreddit(subreddits, search_terms):
    """Subreddit Pulse: Monitors Subreddits for Specific Terms

    When given a list of specific terms, this program monitors specific
    subreddits for those terms. If the term is found in the title or body
    of a new submission, information about the submission is recorded into
    a logfile (stored in logfiles/).
    """
    logfile = _create_logfile()
    monitor = SubredditMonitor()
    monitor.logfile = logfile
    monitor.keyword_file = search_terms
    monitor.subreddit_monitor(subreddits)


def _create_logfile():
    """Creates a new logfile.

    This log file is used to log submissions that meet
    certain criteria. A new log file is generated each
    time the program is executed. The logfile name is
    of the form YearMonthDay-HourMinuteSecond.csv
    """
    time_string = time.strftime("%Y%m%d-%H%M%S")
    with open(f"logfiles/{time_string}.csv", 'w') as f:
        f.write("Title,ID,URL,Date_Created\n")
    print("Log file created")
    return f"logfiles/{time_string}.csv"


if __name__ == "__main__":
    watch_subreddit()
