import boto3
import datetime

import os

ec2 = boto3.resource('ec2')

def lambda_handler():
    print("\n\nAWS snapshot backups starting at %s" % datetime.datetime.now())
    instances = ec2.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name', 
                'Values': ['running']
            }
        ]
    )
    
    print("instances [%s]" % instances)
    for instance in instances:
        #instance_name = filter(lambda tag: tag['Key'] == 'Name', instance.tags)[0]['Value']
        #print("instance_name [%s]" % instance_name)
        #idx+=1
        #print("instance number [%s]" % idx)
        
        for volume in ec2.volumes.all():
		#for volume in ec2.volumes.filter(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance.id]}]):
        #    description = 'scheduled-%s.%s-%s' % (instance_name, volume.volume_id, 
        #        datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
            
            #response = volume.create_snapshot(Description=description, VolumeId=volume.volume_id)    
            
            #if response:
                #print("Snapshot created with description [%s]" % description)
                #ec2.create_tags( Resources=[response.snapshot_id],
                #Tags=[
                #    {'Key': 'Name', 'Value': description}
                #])
                #snapshot = ec2.Snapshot(response.snapshot_id)
                #snapshot.create_tags(Tags=[{'Key': 'Name','Value': description}])

            for snapshot in volume.snapshots.all():
                retention_days = 100
                #print(datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None))
                #print("retention_days %s" % datetime.timedelta(days=retention_days))
                #print(snapshot.description.startswith('scheduled-'))
                #print(( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days))
                #print("---------------------------------------------------------")
                if ( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days):
                    print("\t\tDeleting snapshot [%s - %s]" % ( snapshot.snapshot_id, snapshot.description ))
                    try:
                        snapshot.delete()
                    except:
                        print("Oops!  error :: " )
        
    print("\n\nAWS snapshot backups completed at %s" % datetime.datetime.now())
    return True

if __name__ == '__main__':
	lambda_handler()
