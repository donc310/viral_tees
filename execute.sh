#!/bin/sh

source ../bin/activate
python run_luigi.py TrendsTaskWrapper --scheduler-port 8089
