import boto3
import datetime

import os

ec2 = boto3.resource('ec2')

def lambda_handler():
    print("\n\nAWS EC2 Create Tag starting at %s" % datetime.datetime.now())
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
        print(instance.id, instance.instance_type)
        ec2.create_tags(Resources=instance.id,Tags=[{'Key':'XsuiteIgnore','Value':''}])
    print("\n\nAWS EC2 Create Tag completed at %s" % datetime.datetime.now())
    return True

if __name__ == '__main__':
	lambda_handler()
