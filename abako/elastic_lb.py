# -*- coding: utf-8 -*-

import pprint
import boto3


def elb_instance():
    e = boto3.client('elb')
    return e


def list_elbs():
    """Return Elastic Load Balancers."""
    elb = elb_instance()
    instances = elb.describe_load_balancers()
    return instances


if __name__=="__main__":
    elbs = list_elbs()
    pprint.pprint(elbs)
