# subreddit-pulse

## Overview


This program monitors new submissions in specific subreddits. It can log all new posts, or it can monitor for specific keywords, making it easy to parse information about topics of interest. If one of the provided keywords is encountered, information about the submission (namely, title, date, url, id, and body) is logged for later viewing. The program continuously monitors the subreddits until the program is terminated (Ctrl+C).

As an example, consider a case in which you're interested in finding new recipes for tacos. In such a case, subreddit-pulse could monitor cooking-related subreddits for the keywords 'taco' and 'tacos', and it will log each new submission that includes these keywords. Later, a review of the generated log file will show all new submissions that discuss tacos, ensuring that no new recipes are missed.

## Installation 


This program was written using Python 3.6.7. To use, clone this repository, and then create a virtual environment:\
`python3 -m venv venv`\
Activate the virtual environment:\
`source venv/bin/activate` (for Linux/OS X)\
Install the required dependencies:\
`pip install -r requirements.txt`


## Configuration


After installation, the config.ini file needs to be setup. This file provides the necessary information for accessing Reddit. An example of how the config.ini file should be setup is located in `examples/`. The completed config.ini file should be placed in `subreddit_pulse/`. 


Next, for keyword-based logging, the keywords of interest need to be added. By default, the program looks for a file called keywords.dat in the root directory. This file should contain keywords of interest, each on its own line. An example keywords.dat file is located in `examples/`.


## Usage

### Log all new posts

To log all new posts:\
`python subreddit_pulse.py all --subreddits subreddit_name --log name_of_log_file`\
By default, if a log file is not specified, one will automatically be created with the format "YearMonthDay-HourMinuteSecond.csv". If no subreddits are specified, the program will prompt for the name(s) of subreddit(s) to monitor. Multiple subreddits can be specified if their names are separated by a '+' sign, e.g., "subreddit1+subreddit2+subreddit3".

### Log posts that contain specific keywords

To log posts that contain specific keywords:\
`python subreddit_pulse.py keywords --subreddits subreddit_name --log name_of_log_file --search_terms name_of_keywords_file`\

By default, if a log file is not specified, one will automatically be created with the format "YearMonthDay-HourMinuteSecond.csv". If a keywords file is not specified, the program will default to `keywords.dat`. If no subreddits are specified, the program will prompt for the name(s) of subreddit(s) to monitor. Multiple subreddits  can be specified if their names are separated by a '+' sign, e.g., "subreddit1+subreddit2+subreddit3".

