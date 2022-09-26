#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import boto3
import botocore


logger = logging.getLogger(__name__)
if logger.name == '__main__':
    console = logging.StreamHandler()
    logger.addHandler(console)
logger.setLevel(logging.INFO)


session = boto3.session.Session(region_name='us-east-1')
alb_client = session.client('elbv2')

# AWS  set of 3 availablity zones
subnet_id_list    = ["subnet-1axxxx", "subnet-1bxxxx", "subnet-1cxxxx"]
security_group_id = 'sg-xxxxxxxxxxxxxx'
vpc_id            = "vpc-xxxxxxxxxxxxx"


def alb_create_target_group(target_group_name, vpc_id):
    response = alb_client.create_target_group(Name=target_group_name, Protocol='HTTP', Port=80, VpcId=vpc_id)
    return response


def create_alb(alb_name):
    """
    Given a subnets/availabilty zones, create a an internal ALB in us-east-1 in 3 zones.
    """
    try:
        response = alb_client.create_load_balancer(
            Name= alb_name,
            Subnets = subnet_id_list,
            SecurityGroups=[
                security_group_id,
            ],
            Scheme='internal',
            Type='application',
            IpAddressType='ipv4',
        )
        return response 
    except Exception as e:
        logger.error(e)
        notify_on_error(str(e))

def alb_describe(target_group_arn, loadbalancer_arn):

    response = alb_client.describe_load_balancers()
    
    response = alb_client.create_target_group(Name=target_group_name, Protocol='HTTP', Port=80, VpcId=vpc_id)
    return response

def alb_create_listener(target_group_arn, loadbalancer_arn):

    response = alb_client.create_listener(
        DefaultActions=[
            {
                'TargetGroupArn': target_group_arn,
                'Type': 'forward',
            },
        ],
        LoadBalancerArn=loadbalancer_arn,
        Port=80,
        Protocol='HTTP',
    )
    
    return response

def lambda_handler(event, context):
    #create target group
    target_group = alb_create_target_group('jcpenney-target-group', vpc_id)
    target_group_arn = target_group['TargetGroups'][0]['TargetGroupArn']

    #create alb
    alb_create = create_alb('JCPenneyLoadBalancer')
    loadbalancer_arns = alb_create['LoadBalancers'][0]['LoadBalancerArn']

    # create listener
    alb_listener = alb_create_listener(target_group_arn, loadbalancer_arns)


