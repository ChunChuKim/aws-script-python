import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='dspprd')
ec2_client = session.client('ec2')
#ec2_client = boto3.client('ec2')

try:
    response = ec2_client.describe_security_groups(GroupIds=[
        'sg-0ac55c1beae230784',
        'sg-6b153c00',
    ])
    for sg in response['SecurityGroups']:
        print(sg.find('181231'))
        #if.fin
        print('::::::::::::::::::')
    #print(response['SecurityGroups'])
except ClientError as e:
    print(e)