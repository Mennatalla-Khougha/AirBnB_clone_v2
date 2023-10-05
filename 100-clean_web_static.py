#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import run, local, task

env.hosts = ["100.25.111.125", "34.207.190.218"]
env.user = "ubuntu"


@task
def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
