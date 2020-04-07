#!/usr/bin/python3
""" This Fabric script generates a .tgz archive """


from fabric.api import run, local
from fabric.contrib import files
from os.path import getsize
import time


def do_pack():
    """ Compress web static files into .tgz
    Return:
        upon success, returns archive path
        upon fail, returns None
    """
    timestamp = time.strftime("%Y%m%d%H%M%S")

    folder = run("mkdir -p versions")

    path = "versions/web_static_{}.tgz".format(timestamp)

    archive = local("tar -cvzf {} web_static".format(path))

    if archive.succeeded:
        size = getsize(path)
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    return None
