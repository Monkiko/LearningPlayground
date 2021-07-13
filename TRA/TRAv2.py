#!/usr/bin/env python
#
#
# Script to randomly assign Ticket Reviewees to Reviewers (QueueQillerz only)
# This is to have certain Reviewers assigned only 1 Reviewee
#
#
# Author: Ian Rivera-Leandry
# Creation Date: 06-19-2019
# Last Revised On: 09-11-2019
#
#

from random import shuffle
import itertools
import requests
import sys

#
#
# Making lists of L1s and Senior Techs for Reviewee List

def Reviewees_setup():
    global Reviewees
    L1 = ['Caleb Cortez', 'Edward Lane', 'Kim Oswalt', 'Larry Veloz']
    ST = ['Marcus Bermudez', 'Ian Rivera',
    'Chelsey Aldridge', 'Clay Claiborne', 'Brandon Taylor', 'Omar Ferrer']
    shuffle(L1)
    shuffle(ST)
    Reviewees = L1[:] + ST[:]

#
#
# Making Reviewer lists

def Reviewers_setup():
    global Reviewers
    SReviewers = ['Marcus Bermudez', 'Ian Rivera',
    'Chelsey Aldridge', 'Clay Claiborne', 'Brandon Taylor', 'Omar Ferrer']
    MReviewers = ['Chelsey Aldridge', 'Ian Rivera', 'Marcus Bermudez', 'Omar Ferrer']
    shuffle(SReviewers)
    shuffle(MReviewers)
    Reviewers = SReviewers[:] + MReviewers[:] + MReviewers[:]

#
#
# Verify that no one is assigned to themselves

def SelfAssignedCheck():
    global Reviewees
    global Reviewers
    for c1, c2 in zip(Reviewees,itertools.cycle(Reviewers)):
        if c1 == c2:
            sys.exit("A Reviewer was assigned to themself. Please run again")

#
#
# Dole out the Ticket Review Assignments and write the output to a file

def ReviewAssignments():
    global Reviewees
    global Reviewers
    file=open("TicketReviewAssignments.txt","w")
    file.write("Ticket Review Assignments this month: ")
    file.write("\n")
    file.write("\n")
    file.write("Reviewees                 Reviewers")
    file.write("\n")
    file.write("---------                 ---------")
    file.write("\n")
    padding = 25
    for c1, c2 in zip(Reviewees,itertools.cycle(Reviewers)):
        print >> file, "%s %s" % (c1.ljust(padding), c2)
        Reviewees.remove(c1)
    file.close()

#
#
# Send email with Ticket Review Assignments

def MailAssignments():
    file=open("TicketReviewAssignments.txt","r")
    return requests.post(
        "https://api.mailgun.net/v3/irl-tinkerlab.net/messages",
        auth=("api", "key-83d206c1b7d736ed433938fe4f3b4d8b"),
        files=[("attachment", open("TicketReviewAssignments.txt"))],
        data={"from": "Ian Rivera-Leandry <mailgun@irl-tinkerlab.net>",
            "to": ["Ian.Rivera-Leandry@rackspace.com"],
            "subject": "Ticket Review Assignments",
            "text": file.read()})
    file.close()

#
#
# Run the functions to create the lists

Reviewees_setup()
Reviewers_setup()
SelfAssignedCheck()
ReviewAssignments()

#
#
# Send email

MailAssignments()
