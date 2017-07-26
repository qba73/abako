# -*- coding: utf-8 -*-

import pprint
import boto3


def dynamo():
    cl = boto3.client('dynamodb')
    return cl


def get_tables(db):
    tables = db.list_tables()
    return tables


def show_tables():
    db = dynamo()
    tables = get_tables(db)
    return tables


if __name__=="__main__":
    dynamo_tables = show_tables()
    pprint.pprint(dynamo_tables)

