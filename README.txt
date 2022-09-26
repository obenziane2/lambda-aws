{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\fswiss\fcharset0 Helvetica;\f2\fnil\fcharset0 HelveticaNeue;
}
{\colortbl;\red255\green255\blue255;\red18\green19\blue24;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c8627\c9804\c12157;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs24 \cf0 Introduction:\

\f1\b0 \
This readme describes the steps to create a ALB private load balancer using python 3.7, Boto3 on AWS Lambda\
\

\f0\b Requirements:
\f1\b0 \
\
* Python 3.7\
* Boto3\
* AWS Account\
\

\f0\b Steps:
\f1\b0 \
\
1. Open the file \'93 jcpennney-alb.py\'94  and replace the variables corresponding to your AWS account\
\
subnet_id_list    = ["subnet-1axxxx", "subnet-1bxxxx", "subnet-1cxxxx"]\
security_group_id = 'sg-xxxxxxxxxxxxxx'\
vpc_id            = "vpc-xxxxxxxxxxxxx"\
\
2. Create a lambda function from AWS console using the file: \'93jcpennny-alb.py\'94\
3. Once Lambda function is created, point the handler to \'93
\f2\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 lambda_function.lambda_handler\cb1 \'94
\f1\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0  \
4. The python script should create a load balancer, target group and an http 80 listener\
\
\
\

\f0\b Notes:
\f1\b0 \
* we can go beyond this basic setup like including https, health check, etc\'85. I\'92ve tried to keep this simple as much as I can for now.\
\
Thank you! Please let me know if you have any questions or comments}