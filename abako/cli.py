# -*- coding: utf-8 -*-

import click

import dynamodb
import rdsdb
import ec
import ecr_registry
import elastic_lb


@click.group()
def raw_report():
    pass


@raw_report.command()
def dynamo():
    """Show DynamoDB tables."""
    tables = dynamodb.show_tables()
    click.echo(tables)


@raw_report.command()
def rds():
    """Show RDS instances."""
    instances = rdsdb.get_instances()
    click.echo(instances)


@raw_report.command()
def ec2():
    """Show EC2 instances."""
    ec2_instances = ec.get_instances()
    click.echo(ec2_instances)


@raw_report.command()
def ecr():
    """Show ECR (Docker) repositories."""
    repos = ecr_registry.get_repositories()
    click.echo(repos)


@raw_report.command()
def elb():
    """Show ELB - Elastic Load Balancers."""
    balancers = elastic_lb.list_elbs()
    click.echo(balancers)


raw_report = click.CommandCollection(sources=[raw_report])


if __name__=="__min__":
    raw_report()

