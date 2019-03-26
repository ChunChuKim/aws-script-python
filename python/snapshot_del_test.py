import boto3
import datetime
import os
import time

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot('id')

def aws_snapshots_delete():
	print("\n\nAWS snapshot delete starting at %s" % datetime.datetime.now())
	cnt=0
	snapshots = client.describe_snapshots(
		Filters=[
			{
				'Name': 'status',
				'Values': [
					'completed',
				]
			},		
		],
		OwnerIds=[
			'635464704865',
		]
	)
	for snapshot_src in snapshots.get("Snapshots"):
		#print("snapshot :: %s" % snapshot)
		
		cnt = cnt+ 1
		retention_days=14
		print("=================================================")
		print("snapshot cnt :: %s" % cnt)
		snapshot = ec2.Snapshot(snapshot_src.get("SnapshotId"))
		print("snapshot :: %s" % snapshot)
		print(datetime.datetime.now().replace(tzinfo=None))
		print(snapshot.start_time.replace(tzinfo=None))
		print(( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days))
		print(datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None))
		print(datetime.timedelta(days=retention_days))
		print("=================================================")
		if ( cnt % 100 == 0) : time.sleep(5)
	
if __name__ == '__main__':
	aws_snapshots_delete()