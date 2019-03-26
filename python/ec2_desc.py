import boto3

ec2 = boto3.client('ec2')

instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ]
)    
idx=0
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        idx = idx + 1
        print("index : " , idx, end=", ")
        print("instance id : %s" % instance['InstanceId'], end=", ")
        
        #print("Tags :: %s"% instance['Tags'])
        for tag in instance['Tags']:
            if "Name" in tag['Key']:
                print("instance name %s " % tag['Value'])
        

#print "Changing tags for %d instances" % len(ids)

#ec2.create_tags(
#    Resources=ids,
#    Tags=[
#        {
#            'Key': 'XsuiteIgnore',
#            'Value': ''
#        }
#    ]
#)        