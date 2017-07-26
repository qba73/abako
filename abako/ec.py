# -*- coding: utf-8 -*-

import pprint
import boto3


def ec():
    ec2 = boto3.client('ec2')
    return ec2


def get_instances():
    ec_obj = ec()
    ec2_instances = ec_obj.describe_instances()
    return ec2_instances


def main():
    e = ec()
    ins = get_instances(e)
    pprint.pprint(ins)


if __name__=="__main__":
    main()
