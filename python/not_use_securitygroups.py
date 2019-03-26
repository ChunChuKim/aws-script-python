import boto3
import datetime
import os
import time
import json
from pprint import pprint

ec2client = boto3.client('ec2')
rdsclient = boto3.client('rds')
elbclient = boto3.client('elbv2')
ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot('id')

def aws_nonuse_security_groups():

	idx=0
	a = []
	b = []
	c = []
	print("\n\nAWS Security Group search starting at %s" % datetime.datetime.now())
	#response = client.describe_instances(
	#	Filters=[
#			{
#				'Name': 'network-interface.group-id',
#				'Values': [
#					'sg-0b088361',
#				]
#			},
#		]
#	)
#	print(response)
#	print(len(response))

	rdslist = rdsclient.describe_db_instances()
	#print(rdslist)
	#print(len(rdslist['DBInstances']))
	for rds in rdslist['DBInstances'] :		
		for vpcsecuritygroups in rds.get('VpcSecurityGroups'):
			security_group_id = vpcsecuritygroups.get('VpcSecurityGroupId')
			c.append(security_group_id)
		
		
	elbs = elbclient.describe_load_balancers()
	#print(elbs)
	#print(len(elbs['LoadBalancers']))
	for elb in elbs['LoadBalancers'] :
		security_group_id = elb.get('SecurityGroups')
		if(security_group_id != None):
			for security_group_ids in security_group_id :
				b.append(security_group_ids)
	
	securitygroups = ec2client.describe_security_groups()
	for securitygroup in securitygroups.get("SecurityGroups"):
		security_group_id = securitygroup['GroupId']
		#print("\n\nSecurity Group ID %s" % security_group_id)
		#EC2 Security Group search
		response = ec2client.describe_instances(Filters=[{'Name': 'network-interface.group-id','Values': [security_group_id]}])
		#print(len(response['Reservations']))
		
		if(len(response['Reservations']) == 0):
			a.append(security_group_id)
		
		
		#idx = idx + 1
			#LB ecurity Group search
			#if(len() ==0):			
			#print(security_group_id)
	#print(a)
	#print(b)
	#print(c)
	s1 = set(a)
	s2 = set(b)
	s3 = set(c)
	s4 = s1 - s2 - s3
	for i in list(s4):
		print(i)
		
	
if __name__ == '__main__':
	aws_nonuse_security_groups()