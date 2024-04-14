import os
from cominfer import CommandInferrer
from comutils import FunctionSchedulerUser


def main():
    description = 'Command line tool for syncing files to GitHub repos'
    directory = os.path.dirname(os.path.realpath(__file__))
    CommandInferrer(description, directory).infer()


def configure(view_dir="", username="", interval=""):
    user = FunctionSchedulerUser('notewatcher')
    user.configure(view_dir=view_dir, username=username)
    if interval:
        user.schedule_function('notewatcher', 'update', interval)
