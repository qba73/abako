# -*- coding: utf-8 -*-

import pprint
import boto3


def rdsclient():
    client = boto3.client('rds')
    return client


def get_instances():
    client = rdsclient()
    instances = client.describe_db_instances()
    return instances


def main():
    instances = get_instances()
    pprint.pprint(instances)


if __name__=="__main__":
    main()
