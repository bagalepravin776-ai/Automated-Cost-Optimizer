# Automated AWS Cost Optimizer

## Project Overview

This project automatically reduces AWS costs by stopping idle Amazon EC2 instances.

## AWS Services Used

* AWS Lambda
* Amazon CloudWatch
* Amazon EC2
* Amazon SNS

## Architecture
<img width="1536" height="1024" alt="01_Architecture png" src="https://github.com/user-attachments/assets/a9b958c5-0f19-4ea9-82bf-ec63bef61038" />

CloudWatch monitors EC2 CPU utilization.

If CPU utilization falls below 5%:

1. CloudWatch Alarm enters ALARM state.
2. Lambda function is triggered.
3. Lambda stops the EC2 instance.
4. AWS costs are reduced automatically.

## Project Workflow

EC2 Instance → CloudWatch Alarm → Lambda Function → Stop EC2

## Screenshots

### EC2 Running

<img width="692" height="519" alt="02_ec2-running" src="https://github.com/user-attachments/assets/3e505908-4e96-419f-9005-60e21f5b2b75" />


### CloudWatch Alarm Configuration

<img width="1336" height="524" alt="03_cloudwatch-alarm-config" src="https://github.com/user-attachments/assets/92ae5c96-8fcb-4883-adef-0f7b86cdb52a" />


### Lambda Function Code

<img width="860" height="300" alt="04_lambda-code" src="https://github.com/user-attachments/assets/6b3ffd61-bee3-4c31-8848-9f0f50320d47" />


### Lambda Test Success

<img width="919" height="353" alt="05_lambda-test-success" src="https://github.com/user-attachments/assets/9ee9ffc0-1255-4592-bf8c-c8e53a835730" />


### Alarm with Lambda Action

<img width="1261" height="422" alt="06_alarm-lambda-action" src="https://github.com/user-attachments/assets/39fdc032-1574-4a52-8d31-277ab3a6f529" />


### EC2 Stopped

<img width="718" height="351" alt="07_ec2-stopped" src="https://github.com/user-attachments/assets/dd37e8dc-4e1f-4a59-b613-a6ffbf52f8e4" />


## Outcome

Successfully automated EC2 cost optimization using AWS Lambda and CloudWatch.
