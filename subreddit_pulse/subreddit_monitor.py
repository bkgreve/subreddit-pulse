import praw
import configparser
import datetime as dt


class SubredditMonitor(object):
    """Monitors new submissions for given subreddit."""

    def __init__(self):
        self.logfile = "logfile.csv"
        self.keyword_file = "keywords.dat"

    def subreddit_monitor_keywords(self, subreddits):
        """Monitors new submissions for keywords.

        This function monitors the title/body of new submissions for given
        subreddits. If a keyword in the list search_terms is present in
        the title or in the body, that submission is logged.

        Args:
        subreddits (str): subreddits to monitor; multiple subreddits
        can be included in string when separated by '+' sign, e.g.,
        subreddit1+subreddit2+subreddit3.
        """
        reddit = self._reddit_access()
        search_terms = self._get_keywords()
        for submission in reddit.subreddit(subreddits).stream.submissions():
            if any(word in submission.title for word in search_terms):
                print("Logging submission")
                self._log_submissions(submission)
            elif any(word in submission.selftext for word in search_terms):
                print("Logging submission")
                self._log_submissions(submission)
            else:
                print("Passing. Submission does not satisfy criteria.")

    def subreddit_monitor_all(self, subreddits):
        """Logs all new submissions for given subreddits.

        Args:
        subreddits (str): subreddits to monitor; multiple subreddits
        can be included in string when separated by '+' sign, e.g.,
        subreddit1+subreddit2+subreddit3.
        """
        reddit = self._reddit_access()
        for submission in reddit.subreddit(subreddits).stream.submissions():
            print("Logging submission.")
            self._log_submissions(submission)

    def _reddit_access(self):
        """Returns reddit object for accessing subreddits."""

        config = configparser.ConfigParser()
        config.read('config.ini')

        client_id = config['DEFAULT']['CLIENT_ID']
        client_secret = config['DEFAULT']['CLIENT_SECRET']
        user_agent = config['DEFAULT']['USER_AGENT']
        username = config['DEFAULT']['USERNAME']
        password = config['DEFAULT']['PASSWORD']

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password)

        return reddit

    def _log_submissions(self, submission):
        """Generates log file of submissions that meet criteria"""
        title = submission.title
        sub_id = submission.id
        url = submission.url
        body = submission.selftext
        date_created = dt.datetime.fromtimestamp(submission.created)
        log_string = f"{title},{sub_id},{url},{date_created},{body}\n"
        with open(self.logfile, 'a') as f:
            f.write(log_string)

    def _get_keywords(self):
        """Loads keywords from file and returns them as list of strings."""
        search_terms = []
        with open(self.keyword_file, 'r') as f:
            for line in f:
                line = line.partition('#')[0]
                line = line.rstrip()
                if len(line) > 0:
                    search_terms.append(line)
        return search_terms
