import boto3
import datetime
import openpyxl

import os

ec2 = boto3.resource('ec2')

def aws_create_ec2_tags():
    print("\n\nAWS EC2 Create Tags starting at %s" % datetime.datetime.now())
	
	# excel file open
    wb = openpyxl.load_workbook('ec2_tags.xlsx')
    ws = wb.active
    #ws = wb.get_sheet_by_name("AP-SLT DEV")
	
    for r in ws.rows:
        print("r0  %s" % r[0].row)
        if 1 == r[0].row:
    	    continue
        instanceid = ''
        strSystem = ''
        strStage = ''
        strService = ''
        strCompany = ''
        strCountry = ''
		
        instanceid = r[13].value
		
        if r[7].value != None:
            strSystem = r[7].value
        
        if r[8].value != None:
            strStage = r[8].value
        
        if r[9].value != None:
            strService = r[9].value
        	
        if r[10].value != None:
            strCompany = r[10].value
        
        if r[11].value != None:
            strCountry = r[11].value
        
        print("strSystem :: %s" % strSystem)
        print("strService :: %s" % strService)
        
        try:
            instance = ec2.Instance(instanceid)
            instance.create_tags(
                DryRun=False,
                Tags=[
                    {
					    'Key': 'System',
					    'Value': strSystem
				    },
				    {
					    'Key': 'STAGE',
					    'Value': strStage
				    },
				    {
                        'Key': 'Service',
					    'Value': strService
				    },
				    {
					    'Key': 'Company',
					    'Value': strCompany
				    },
				    {
					    'Key': 'Country',
                        'Value': strCountry
				    },
			    ]
		    )
        except :
            print("opps instace id %s is error" % instanceid)
#        print("print tag %s" % tag)
    
    wb.close
    print("\n\nAWS EC2 Create Tags End at %s" % datetime.datetime.now())
    return True
	
if __name__ == '__main__':
	aws_create_ec2_tags()