import boto3
import datetime

import os

client = boto3.client('ec2')

def lambda_handler():
	print("\n\nAWS snapshot delete starting at %s" % datetime.datetime.now())
	snapshots = client.describe_snapshots(MaxResults=5)
	#print("snapshots [%s]" % snapshots)
	for snapshot in snapshots:
		print("\t\tDeleting snapshot [%s - %s]" % ( snapshot.snapshot_id, snapshot.description ))
	print("\n\nAWS snapshot delete completed at %s" % datetime.datetime.now())
	return True

if __name__ == '__main__':
	lambda_handler()
