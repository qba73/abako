# -*- coding: utf-8 -*-

import pprint
import boto3


def ecr_instance():
    e = boto3.client('ecr')
    return e


def get_repositories():
    instance = ecr_instance()
    repos = instance.describe_repositories()
    return repos


if __name__=="__main__":
    img = get_repositories()
    pprint.pprint(img)
