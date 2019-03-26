import boto3
import boto3
import datetime

import os

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    print("\n\nAWS snapshot backups starting at %s" % datetime.datetime.now())
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for instance in instances:
        instance_name = filter(lambda tag: tag['Key'] == 'Name', instance.tags)[0]['Value']

        for volume in ec2.volumes.filter(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance.id]}]):
            description = 'scheduled-%s.%s-%s' % (instance_name, volume.volume_id, 
                datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
                
            if volume.create_snapshot(VolumeId=volume.volume_id, Description=description):
                print("Snapshot created with description [%s]" % description)

        for snapshot in volume.snapshots.all():
            snapshot.create_tags(DryRun=False,Tags=[{'Key': 'Name','Value': description}])
            retention_days = int(os.environ['retention_days'])
            if snapshot.description.startswith('scheduled-') and ( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days):
                print("\t\tDeleting snapshot [%s - %s]" % ( snapshot.snapshot_id, snapshot.description ))
                snapshot.delete()

    print("\n\nAWS snapshot backups completed at %s" % datetime.datetime.now())
    return True
