import praw
import configparser
import datetime as dt


class SubredditMonitor(object):
    """Returns a stream of new submissions for given subreddit."""

    def __init__(self):
        self.logfile = "logfile.csv"

    def subreddit_title_monitor(self, subreddits):
        """Monitors the title of submission.

        This function monitors the titles of new submissions for given
        subreddits. If a keyword from a list is present in the title,
        perform action on that submission.

        Args:
        subreddits (str): subreddits to monitor; multiple subreddits
        can be included in string when separated by '+' sign, e.g.,
        subreddit1+subreddit2+subreddit3.
        """
        keywords = ["do", "the"]
        reddit = self._reddit_access()
        for submission in reddit.subreddit(subreddits).stream.submissions():
            if any(word in submission.title for word in keywords):
                print("Logging submission")
                self._log_submissions(submission)
            else:
                print("Submission does not satisfy criteria")

    def _reddit_access(self):
        """Returns reddit object for accessing subreddits."""

        config = configparser.ConfigParser()
        config.read('config.ini')

        client_id = config['DEFAULT']['CLIENT_ID']
        client_secret = config['DEFAULT']['CLIENT_SECRET']
        user_agent = config['DEFAULT']['USER_AGENT']
        username = config['DEFAULT']['USERNAME']
        password = config['DEFAULT']['PASSWORD']

        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent,
                             username=username,
                             password=password)

        return reddit

    def _log_submissions(self, submission):
        """Generates log file of posts that meet criteria"""
        title = submission.title
        sub_id = submission.id
        url = submission.url
        date_created = dt.datetime.fromtimestamp(submission.created)
        body = submission.selftext
        log_string = f"{title},{sub_id},{url},{date_created},{body}\n"
        with open(self.logfile, 'a') as f:
            f.write(log_string)
