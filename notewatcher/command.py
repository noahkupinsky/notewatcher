from cominfer.command_inferrer import CommandInferrer
import os

def main():
    description = 'Command line tool for syncing note files to GitHub repos'
    directory = os.path.dirname(os.path.realpath(__file__))
    CommandInferrer(description, directory).infer()