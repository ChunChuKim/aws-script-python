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

	a = []
	a.append("SecurityGroupId")
	a.append("SecurityGroupName")
	a.append("Protocol")
	a.append("FromPort")
	a.append("ToPort")
	a.append("Source")
	a.append("Description")
	a.append("UserId")
	b.append(a)
	securitygroups = ec2client.describe_security_groups()
	for securitygroup in securitygroups.get("SecurityGroups"):
		
		#print(securitygroup)
		security_group_id = securitygroup['GroupId']
		security_group_name = securitygroup['GroupName']
#		a.append(security_group_id)
#		a.append(security_group_name)
		for ipPermissions in securitygroup.get("IpPermissions"):
			#print(security_group_id)
			#print(ipPermissions)
#			a.append(ipPermissions['FromPort'])
#			a.append(ipPermissions['IpProtocol'])
			if(len(ipPermissions['IpRanges'])>0):
				
				for ipRanges in ipPermissions['IpRanges']:
					a = []
					a.append(security_group_id)
					a.append(security_group_name)
					if("-1" in ipPermissions['IpProtocol']):
						a.append("All")
						a.append("All")
						a.append("All")
					else:
						a.append(ipPermissions['IpProtocol'])
						a.append(ipPermissions['FromPort'])
						a.append(ipPermissions['ToPort'])
					
					a.append(ipRanges['CidrIp'])
					try:
						a.append(ipRanges['Description'])
					except:
						a.append("")
					a.append("")
					b.append(a)
						
			if(len(ipPermissions['UserIdGroupPairs'])>0):
				
				for useridgrouppairs in ipPermissions['UserIdGroupPairs']:
					a = []
					a.append(security_group_id)
					a.append(security_group_name)
					if("-1" in ipPermissions['IpProtocol']):
						a.append("All")
						a.append("All")
						a.append("All")
					else:
						a.append(ipPermissions['IpProtocol'])
						a.append(ipPermissions['FromPort'])
						a.append(ipPermissions['ToPort'])
					a.append(useridgrouppairs['GroupId'])
					try:
						a.append(useridgrouppairs['Description'])
					except:
						a.append("")
						
					try:
						a.append(useridgrouppairs['UserId'])
					except:
						a.append("")
						
					b.append(a)

					
					
			
		#print(a)
	#print(b)

#	f = open("SecurityGroups.csv", 'w')
#	for sgs in b:
#		ln=""
		#print(sgs)
#		idx = 0
#		for sg in sgs:
#			if(idx > 0):
#				ln=ln+","
			#print(sg)
#			ln = ln + str(sg)
#			idx = idx +1
#		print(ln)
#		f.write(ln+"\n")
			
#	f.close()
		
		
		
	
if __name__ == '__main__':
	aws_nonuse_security_groups()