from subreddit_pulse.subreddit_monitor import SubredditMonitor
import time
import click


@click.group()
def cli():
    """Subreddit Pulse.

    Watches specific subreddits and logs new submissions. Can log
    all new submissions or can log only submissions that contain
    user-provided keywords.

    For help on specific commands, include --help after the command.
    """
    pass


@cli.command('keywords')
@click.option(
    '--subreddits',
    prompt='Subreddits to monitor.',
    help="Subreddits to monitor. Use '+' to join multiple.")
@click.option(
    '--search_terms',
    default='keywords.dat',
    help="File containing search terms for monitoring subreddits.")
@click.option('--log', help="Name for log file. Default is <date>.csv")
def watch_subreddit_keywords(subreddits, search_terms, log):
    """Logs posts that contain specific keywords.

    Given a list of specific terms, monitors specified
    subreddits for those terms. If the keyword is found in the title
    or body of the post, then the post is logged in a log file (located
    in logfiles/. Multiple subreddits can be specified by separating the
    subreddit names with '+', e.g., 'askreddit+learnpython'.
    """
    logfile = _create_logfile(log)
    monitor = SubredditMonitor()
    monitor.logfile = logfile
    monitor.keyword_file = search_terms
    monitor.subreddit_monitor(subreddits)


@cli.command('all')
@click.option(
    '--subreddits',
    prompt='Subreddits to monitor.',
    help="Subreddits to monitor. Use '+' to join multiple.")
@click.option('--log', help="Name for log file. Default is <date>.csv")
def watch_subreddit_all(subreddits):
    """Logs all posts from specific subreddits.

    For specified subreddits, logs all posts to log file for later
    analysis. Multiple subreddits can be specified by separating the
    subreddit names with '+', e.g., 'askreddit+gifs+learnpython'. The
    log file is stored in logfiles/.
    """
    pass


def _create_logfile(log):
    """Creates a new logfile.

    This log file is used to log submissions that meet
    certain criteria. A new log file is generated each
    time the program is executed. The default logfile name is
    of the form YearMonthDay-HourMinuteSecond.csv
    """
    if not log:
        time_string = time.strftime("%Y%m%d-%H%M%S")
        with open(f"logfiles/{time_string}.csv", 'w') as f:
            f.write("Title,ID,URL,Date_Created,Body\n")
            print(f"Log file ({time_string.csv}) created")
        return f"logfiles/{time_string}.csv"
    elif log:
        with open(f"logfiles/{log}", 'w') as f:
            f.write("Title,ID,URL,Date_Created,Body\n")
            print(f"Log file ({log}) created.")
        return f"logfiles/{log}"


if __name__ == "__main__":
    cli()
