# ABAKO
A simple tool for checking your active AWS resources.


## Installation for development and testing
Create Python virtualenv
```bash
$ virtualenv venv-abako
$ source venv-abako/bin/activate
```
Install abako for local development
```bash
$ pip install --editable .
```

## Using Abako
Show current options:
```bash
$ abako --help
usage: abako [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dynamo  show DynamoDB tables.
  ec2     show EC2 instances.
  ecr     show ECR repositories.
  elb     show Elastic Load Balancers.
  rds     show RDS instances.
```

Show DynamoDB tables:
```bash
$ abako dynamo
```

Show provisoned EC2 instances:
```bash
$ abako ec2
```

Show RDS databases:
```bash
$ abako rds
```

Show ECR (Docker) repositories:
```bash
$ abako ecr
```

Show Elastic Load Balancers:
```bash
$ abako elb
```

## Makefile
Create wheel and sdist:
```bash
$ make sdist
```

Cleanup environment
```bash
$ make clean
```

Run tests:
```bash
$ make test
```
