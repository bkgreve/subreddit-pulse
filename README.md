# subreddit-pulse

## Overview


This program monitors new submissions in specific subreddits for specific keywords, making it easy to parse information about topics of interest. If one of the provided keywords is encountered, information about the submission (namely, title, date, url, and id) is logged for later viewing. The program continuously monitors the subreddits until the program is terminated.

As an example, consider a case in which you're interested in finding new recipes for tacos. In such a case, subreddit-pulse could monitor cooking-related subreddits for the keywords 'taco' and 'tacos', and it will log each new submission that includes these keywords. Later, a review of the generated log file will show all new submisisons that discuss tacos, ensuring that no new recipes are missed.

## Installation 


This program was written in Python 3. Clone this repository, and then create a virtual environment:\
`python3 -m venv venv`\
Activate the virtual environment:\
`source venv/bin/activate` (for Linux/OS X)\
Install the required dependencies:\
`pip install -r requirements.txt`


## Configuration


After installation, the config.ini file needs to be setup. This file provides the necessary information for accessing Reddit. An example of how the config.ini file should be setup is located in `examples/`. The completed config.ini file should be placed in `subreddit_pulse/`. 


Next, the keywords of interest need to be added. By default, the program looks for a file called keywords.dat in the root directory. This file should contain keywords of interest, each on its own line. An example keywords.dat file is located in `examples/`.


## Usage


After setting up config.ini and keywords.dat, the program can be launched as follows:
`python subreddit_pulse.py --subreddits 'subreddit-name'`, where _subreddit-name_ is the subreddit to search. Multiple subreddits can be specified if their names are separated by a '+' sign, e.g., "subreddit1+subreddit2+subreddit3".


Once launched, the program will monitor a continuous stream of new submissions from the subreddit(s). If one of the keywords is encountered in the title or the body of the submission, then the submission title, date created, URL, and ID are appended to a log file (located in `logfiles/`). A new logfile is written each time the program is launched (with the name format "YearMonthDay-HourMinuteSecond.csv"). 

