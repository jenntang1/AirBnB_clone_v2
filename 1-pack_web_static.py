#!/usr/bin/python3
""" This Fabric script generates a .tgz archive """


from fabric.api import *
from fabric.contrib import files
from os import stat


def do_pack():
    """ Compress web static files into .tgz
    Return:
        upon success, returns archive path
        upon fail, returns None
    """
    timestamp = "+%Y%m%d%H%M%S"
    tgzname = "web_static_{}.tgz".format(timestamp)

    versions = run("mkdir -p versions")

    archive = local("tar -cvzf versions/{} web_static".format(path))

    if archive.succeeded:
        size = path.getsize(tgzname)
        print("web_static packed: versions/{} -> {}Bytes".format(
                                                                 tgzname,
                                                                 size))
        return tgzname
    return None
