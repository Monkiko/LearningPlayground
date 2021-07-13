#!/bin/bash
#
#
# Script to keep running TRAv2.py script until it succeeds
#
#
# Author: Ian Rivera-Leandry
# Creation Date: 08-14-2019
# Last Revised On: 08-14-2019
#
#
until /usr/bin/python /home/ian8775/github_projects/TRA/TRAv2.py
do
  echo "Let's try this again..."
done
