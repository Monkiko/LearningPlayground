#!/bin/bash
#
#
#DC Change
#A script to quickly change the active DC for our ssh tools
#
#
#
#This first portion is gathering the sso username to be used later and
#the current DC and desired DC to switch the ssh configuration files.
clear
read -p "SSO Username: " username
echo "Which DC are you currently configured for?"
echo "1) dfw1"
echo "2) iad3"
echo "3) ord1"
read -p "Enter the number for the DC you are currently using: " ODC
if [ $ODC -eq 1 ]; then
    ODC=dfw1
elif [ $ODC -eq 2 ]; then
    ODC=iad3
elif [ $ODC -eq 3 ]; then
    ODC=ord1
else
    echo "Invalid Entry. Please try again."
fi
#
#
echo "You have indicated that you are set up for the $ODC datacenter"
#
#
#
echo "Which DC are you switching to?"
echo "1) dfw1"
echo "2) iad3"
echo "3) ord1"
read -p "Enter the number for the DC you are switching to: " NDC
if [ $NDC -eq 1 ]; then
    NDC=dfw1
elif [ $NDC -eq 2 ]; then
    NDC=iad3
elif [ $NDC -eq 3 ]; then
    NDC=ord1
else
    echo "Invalid Entry. Please try again."
fi
echo "You have indicated that you wish to use the $NDC datacenter"
#
#
#
RDP=$HOME/.config/rdpwin/rdpwin.conf

sed -i 's/cbast.'$ODC'.corp.rackspace.net/cbast.'$NDC'.corp.rackspace.net/g' $HOME/.ssh/config
if [ -f $RDP ] ; then
    sed -i 's/cbast.'$ODC'.corp.rackspace.net/cbast.'$NDC'.corp.rackspace.net/' $HOME/.config/rdpwin/rdpwin.conf
fi
#
#
#
if [ $NDC = "dfw1" ]; then
    DC=dfw
elif [ $NDC = "iad3" ]; then
    DC=iad
elif [ $NDC = "ord1" ]; then
    DC=ord
fi
#
#
#
#This portion is leveraging authnet.sh to automatically log in to the new DC's support gateway, make sure ssh-agent is running
#add the ssh-key, and then log into the cbast
authnet.sh -d $DC -lv
eval $(ssh-agent)
ssh-add $HOME/.ssh/id_rsa
ssh $username@cbast.$NDC.corp.rackspace.net
