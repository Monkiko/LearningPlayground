#!/usr/bin/env python
#
#
# Script to randomly assign Ticket Reviewees to Reviewers (QueueQillerz only)
#
#
# Author: Ian Rivera-Leandry
# Creation Date: 06-05-2019
# Last Revised On: 06-19-2019
#
#

import commands
from random import shuffle
import itertools
import requests, json, time, os

def L1_setup():
#
#
# Making a list of L1s
    global L1
    global L2
    L1 = ['Caleb Cortez', 'Edward Lane', 'Kim Oswalt', 'Larry Veloz']

#
#
# Making a list of L2s

    L2 = ['Zach Hall', 'Nicholas Flynt', 'Marcus Bermudez', 'Ian Rivera',
    'Chelsey Aldridge', 'Clay Claiborne', 'Brandon Taylor']

#
#
# Assign the L1s to L2s
def L1_Assignment():
    global L1
    global L2
    shuffle(L1)
    shuffle(L2)
    print "L1 Ticket Review Assignments this month: "
    print ("\n")
    print "L1                   L2"
    print "--                   --"
    padding = 20
    for c1, c2 in zip(L1,itertools.cycle(L2)):
        print "%s %s" % (c1.ljust(padding), c2)
        L1.remove(c1)

#
#
# Making a list of Senior Techs

def Review_Setup():
    global Reviewees
    global Reviewers
    Reviewees = ['Omar Ferrer', 'William Tenniswood', 'Zach Hall', 'Nicholas Flynt',
    'Marcus Bermudez', 'Ian Rivera', 'Chelsey Aldridge', 'Clay Claiborne',
    'Brandon Taylor']

    Reviewers = ['Omar Ferrer', 'William Tenniswood', 'Zach Hall', 'Nicholas Flynt',
    'Marcus Bermudez', 'Ian Rivera', 'Chelsey Aldridge', 'Clay Claiborne',
    'Brandon Taylor']

#
#
# Verify that no one is assigned to themselves

def SeniorCheck():
    global Reviewees
    global Reviewers
    shuffle(Reviewees)
    padding = 20
    for c1, c2 in zip(Reviewees,itertools.cycle(Reviewers)):
        if c1 == c2:
            return SeniorCheck()

#
#
# Assign the Senior Techs
def SeniorAssignments():
    global Reviewees
    global Reviewers
    print ("\n")
    print ("\n")
    print "Senior Tech Ticket Review Assignments this month: "
    print ("\n")
    print "Reviewees            Reviewers"
    print "---------            ---------"
    padding = 20
    for c1, c2 in zip(Reviewees,itertools.cycle(Reviewers)):
        print "%s %s" % (c1.ljust(padding), c2)
        Reviewees.remove(c1)

L1_setup()
L1_Assignment()
Review_Setup()
SeniorCheck()
SeniorAssignments()