from subprocess import call
import argparse
import time

parser = argparse.ArgumentParser()
help_ = "Sleep time"
parser.add_argument("-s", "--sleep", help=help_, default=24*60*60, type=int)
args = parser.parse_args()

while(True):
    call("git pull origin master",shell=True)
    call("python twitter_post.py",shell=True)
    time.sleep(args.sleep)