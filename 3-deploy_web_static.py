#!/usr/bin/python3
""" This module uses fabric to
    deploy files to a server
"""


from fabric.api import env, run, put
import os
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


env.hosts = ['35.196.163.39', '35.185.33.80']


def deploy():
    """ This function deploys a web to a server
    """
    archive_path = do_pack()
    if archive_path is False:
        return false

    deploy_return = do_deploy(archive_path)
    return deploy_return
