import boto3
import datetime
import os
import time
import json
from pprint import pprint

ec2client = boto3.client('ec2')
rdsclient = boto3.client('rds')
elbclient = boto3.client('elbv2')
iamclient = boto3.client('iam')
ec2 = boto3.resource('ec2')
iam = boto3.resource('iam')

snapshot = ec2.Snapshot('id')

def aws_iam_list():

	idx=0
	a = []
	b = []
	a.append("UserArn")
	a.append("UserId")
	a.append("GroupName")
	a.append("PasswordLastUsed")
	a.append("JobStatus")
	a.append("JobCreationDate")
	a.append("ServiceName")
	a.append("LastAuthenticated")
	a.append("ServiceNamespace")
	a.append("LastAuthenticatedEntity")
	a.append("TotalAuthenticatedEntities")
	b.append(a)
	
	print("\n\nAWS iam user list search starting at %s" % datetime.datetime.now())
	
	userlist = iamclient.list_users(MaxItems=500)
	
	for iamusers in userlist.get("Users"):
		
		userarn=str(iamusers['Arn'])
		#print(userarn)
		jobid = iamclient.generate_service_last_accessed_details(Arn=userarn)['JobId']
		#print(" iam username : %s" % iamusers['UserName'])
		#print("user :: %s" % iamusers)
		#print(" jobid  : %s" % jobid)
		accesseddetail=iamclient.get_service_last_accessed_details(JobId=jobid)
		
		
		try:
			ad = accesseddetail['ServicesLastAccessed']
			adYN = True
		except:
			adYN = False
		#print(adYN)
		#print(accesseddetail)
		
		a = []
		a.append(userarn)
		a.append(iamusers['UserName'])
		#print(iamclient.list_groups_for_user(UserName=iamusers['UserName'])['Groups'])
		for groups in iamclient.list_groups_for_user(UserName=iamusers['UserName'])['Groups']:
			#print(groups['GroupName'])
			a.append(groups['GroupName'])

		if adYN:
			for lastaccessed in ad:
				
				#a.append(iamclient.list_groups_for_user(UserName=iamusers['UserName'])['Groups']['GroupName'])
				try:
					a.append(iamusers['PasswordLastUsed'])
				except:
					a.append("")
				a.append(accesseddetail['JobStatus'])
				a.append(accesseddetail['JobCreationDate'])
				try:
					a.append(lastaccessed['ServiceName'])
				except:
					a.append("")
					
				try:
					a.append(lastaccessed['LastAuthenticated'])
				except:
					a.append("")
				try:
					a.append(lastaccessed['ServiceNamespace'])
				except:
					a.append("")
				try:
					a.append(lastaccessed['LastAuthenticatedEntity'])
				except:
					a.append("")
				try:
					a.append(lastaccessed['TotalAuthenticatedEntities'])
				except:
					a.append("")
		else:
			try:
				a.append(iamusers['PasswordLastUsed'])
			except:
				a.append("")
			a.append(accesseddetail['JobStatus'])
			a.append(accesseddetail['JobCreationDate'])
			a.append("")
			a.append("")
			a.append("")
			a.append("")
			a.append("")
		
		b.append(a)
		#print(accesseddetail)
		#print("idx : %i" % idx)
		idx = idx + 1
		
		
	f = open("iamUserList.csv", 'w')
	for iamUserList in b:
		ln=""
		#print(sgs)
		idx = 0
		for iu in iamUserList:
			if(idx > 0):
				ln=ln+","
			#print(sg)
			ln = ln + str(iu)
			idx = idx +1
		print(ln)
		f.write(ln+"\n")
			
	f.close()

		
	
if __name__ == '__main__':
	aws_iam_list()