#!/usr/bin/python3
""" This Fabric script generates a .tgz archive """


from fabric.api import run, local, sudo
from fabric.contrib import files
import os
import time


def do_pack():
    """ Compress web static files into .tgz
    Return:
        upon success, returns archive path
        upon fail, returns None
    """
    local("mkdir -p versions")

    timestamp = time.strftime("%Y%m%d%H%M%S")

    path = "versions/web_static_{}.tgz".format(timestamp)

    archive = local("tar -cvzf {} web_static".format(path))

    if archive.succeeded:
        size = os.path.getsize(path)
        print("web_static packed: {} -> {}Bytes".format(path, size))
        return path
    return None
