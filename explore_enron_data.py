#!/usr/bin/python
from __future__ import division
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
from numpy import loadtxt

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#number of datasets
print "Number of data points in Dataset is %d" %len(enron_data)

#number of features
print "Number of features is %d" % len(enron_data.values()[1])

#counting the number of poi in E+F dataset
count = 0
for key in enron_data:
    val = enron_data[key]['poi']
    if val==1:
        count = count+1
print "Number of POI in E+F Dataset %d" %count

#counting number of poi in manually generated text file
lines = [line.rstrip('\n') for line in open('../final_project/poi_names_HM.txt')]
print "Total POIs in Compiled List %d" % len(lines)

#total value of the stock belonging to James Prentice
print "Prentice James's Total Stock Value: %d" % enron_data["PRENTICE JAMES"]["total_stock_value"]

#How many email messages do we have from Wesley Colwell to persons of interest?
print "Email messages from Wesley Colwell to persons of interest: %d" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#the value of stock options exercised by Jeffrey Skilling
print "Value of stock options exercised by Jeffrey Skilling: %d" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#WHo took home the most money?
subdict = dict((k, enron_data[k]["total_payments"]) for k in ("SKILLING JEFFREY K", "LAY KENNETH L"))
print "Person who took the most money: %s" % max(subdict, key=subdict.get)
print "Value in USD of most money taken home: %d" % max(subdict.values())


#How many folks in the dataset have a quantified salary?
count_sal = 0
for key in enron_data:
    val = enron_data[key]['salary']
    if val!='NaN':
        count_sal = count_sal+1
print "Number of people with quantified salary: %d" %count_sal


#How many folks in the dataset have a Known email address?
count_email = 0
for key in enron_data:
    val = enron_data[key]['email_address']
    if val!='NaN':
        count_email = count_email+1
print "Number of people with quantified salary: %d" %count_email


#How many people in the E+F dataset have NaN for their total payments? what percentage of the people in he dataset is this?
count_tot_payments = 0
for key in enron_data:
    val = enron_data[key]['total_payments']
    if val=='NaN':
        count_tot_payments = count_tot_payments+1
print "Number of people with missing total payment data: %d" % count_tot_payments
#print " Percentage of missing total payment data: %f" %
total_count = len(enron_data)
percent=(count_tot_payments)/total_count*100
print "Missing total payment data as percent: %f" % round(percent,2)


# How many POIs have NaN for their total_payments? what percentage of the POI's as a whole is this?
count_poi = 0
for key in enron_data:
    val1 = enron_data[key]['total_payments']
    val2 = enron_data[key]['poi']
    if val1=='NaN' and val2=='True':
        count_poi = count_poi+1
print "Number of POI with missing total payment data: %d" % count_poi
#print " Percentage of missing total payment data: %f" %
total_count = len(enron_data)
percent=(count_poi)/total_count*100
print "Missing total payment data for POI as percent: %f" % round(percent,2)


