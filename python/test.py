import boto3
import datetime
import time

import os

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot('id')

def aws_snapshots_delete():
	print("\n\nAWS snapshot delete starting at %s" % datetime.datetime.now())
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
	cnt=0
	for snapshot_src in snapshots.get("Snapshots"):
		#print("snapshot :: %s" % snapshot)
		
		cnt =cnt+ 1
		if ( cnt % 80 == 0) : time.sleep(10)
			
		retention_days = 14
		snapshot = ec2.Snapshot(snapshot_src.get("SnapshotId"))
		print("snapshot :: %s" % snapshot)
		print(( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days))
		print(datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None))
		print(datetime.timedelta(days=retention_days))
		print(cnt)
		if ( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days):
			print("\tDeleting snapshot [%s - %s]" % ( snapshot_src.get("SnapshotId"), snapshot_src.get("Description")))
			try:
				snapshot.delete()
				print("snapshot_id ::: %s" % snapshot_src.get("SnapshotId"))
			except Exception as e:
				print("Oops!  error :: %s" % e )
		print("---------------------------------------------------------")
		
	
if __name__ == '__main__':
	aws_snapshots_delete()