import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    ec2.stop_instances(
        InstanceIds=['i-01c889a188c45fc63']
    )

    return {
        'statusCode': 200,
        'body': 'EC2 stop request sent successfully'
    }