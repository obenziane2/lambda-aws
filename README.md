# Introduction:

This readme describes the steps to create a ALB private load balancer using python 3.7, Boto3 on AWS Lambda

# Requirements:

* Python 3.7
* Boto3
* AWS Account

#Steps:

1. Open the file “ jcpennney-alb.py”  and replace the variables corresponding to your AWS account

subnet_id_list    = ["subnet-1axxxx", "subnet-1bxxxx", "subnet-1cxxxx"]
security_group_id = 'sg-xxxxxxxxxxxxxx'
vpc_id            = "vpc-xxxxxxxxxxxxx"

2. Create a lambda function from AWS console using the file: “jcpennny-alb.py”
3. Once Lambda function is created, point the handler to “lambda_function.lambda_handler” 
4. The python script should create a load balancer, target group and an http 80 listener



#Notes:
* we can go beyond this basic setup like including https, health check, etc…. I’ve tried to keep this simple as much as I can for now.

Thank you! Please let me know if you have any questions or comments