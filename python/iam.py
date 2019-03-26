import boto3

iam = boto3.resource('iam')
group = iam.Group('infraCLI')

print(group.attached_policies.all())

for group_policy_iterator in group.attached_policies.all():
	print(group_policy_iterator)
	group_policy_iterator.detach_group(
		GroupName='infraCLI',
	)