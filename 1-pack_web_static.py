#!/usr/bin/python3
""" script that generates a .tgz archive from the web_static folder"""
from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """ generates a .tgz archive"""
    if not path.exists("versions"):
        local('mkdir -p versions')

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "web_static_{}".format(time)

    archive = local("tar -cvzf versions/{}.tgz web_static".format(file))

    if archive.succeeded:
        return "versions/{}.tgz".format(file)
    else:
        return None
