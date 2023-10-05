#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import env, run, put, task, local, runs_once
from os.path import exists
from datetime import datetime

env.hosts = ["100.25.111.125", "34.207.190.218"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """ generates a .tgz archive"""
    if not exists("versions"):
        local('mkdir -p versions')

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "web_static_{}".format(time)

    archive = local("tar -cvzf versions/{}.tgz web_static".format(file))

    if archive.succeeded:
        return "versions/{}.tgz".format(file)
    else:
        return None


@task
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = archive_path.split("/")[1]
        file = archive.split(".")[0]
        release = "/data/web_static/releases/"
        folder = "/data/web_static/releases/{}".format(file)
        run("mkdir -p {}".format(folder))
        run(" tar -xzf /tmp/{} -C {}".format(archive, folder))
        run("rm /tmp/{}".format(archive))
        run("mv {}{}/web_static/* {}{}/".format(release, file, release, file))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    except Exception:
        return False


@task
def deploy():
    """creates and distributes an archive"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)


@task
def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs -d "\n" rm -rf'.format(path, number))
