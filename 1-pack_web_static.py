#!/usr/bin/python3
""" This Fabric script generates a .tgz archive """


from fabric.api import run, local
from fabric.contrib import files
from os.path import getsize


def do_pack():
    """ Compress web static files into .tgz
    Return:
        upon success, returns archive path
        upon fail, returns None
    """
    timestamp = "+%Y%m%d%H%M%S"
    path = "versions/web_static_{}.tgz".format(timestamp)

    folder = run("mkdir -p versions")

    archive = local("tar -cvzf {} web_static".format(path))

    if archive.succeeded:
        size = getsize(path)
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    return None
