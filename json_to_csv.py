import csv
import json
import time
import os
from collections import OrderedDict

#root dir of the customer data
root_dir = "/var/run/tenant"
file_list = []
for subdir, dirs, files in os.walk(root_dir):
	for each in files:
		file_list.append( os.path.join(subdir, each))

#initialize the csv file
f = csv.writer(open("customer_metric_data.csv", "wb+"))

#Write the header line in csv file
f.writerow(["Timestamp", "TenantID", "Metric", "Value"])

#I want to read the files in folder by order, ie, read tenant-id 1234 before 1398, etc
#if the order is not matter, then we can remove the sorted part
for each in sorted(file_list):
	if "json" in each:
		x = open(each)
		data = json.load(x, object_pairs_hook=OrderedDict) # by using OrderedDict, the data order of the json file is reserved 

		for metric, value  in data.items():
			f.writerow(["{:.0f}".format(time.time()), each.split("/")[-2], metric, value])
	
