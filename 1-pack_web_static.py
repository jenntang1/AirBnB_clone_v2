#!/usr/bin/python3
""" This Fabric script generates a .tgz archive """


from fabric.api import *
from fabric.contrib import files


path = "tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static"


def do_pack():
    """ Compress web static files into .tgz
    Return:
        upon success, returns archive path
        upon fail, returns None
    """
    archive = sudo("mkdir -p versions; tar -cvzf \
                   versions/web_static_$(date \
                   +%Y%m%d%H%M%S).tgz web_static")

    if archive.succeeded:
        return path
    return None
