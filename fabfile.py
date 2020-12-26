import os

from fabric import Connection, task

CONNECTION_PROPERTIES = {
    "host": os.environ.get('SERVER_IP'),
    "user": os.environ.get('SERVER_USER'),
}


@task
def remote(ctx):
    with Connection(**CONNECTION_PROPERTIES) as c:
        c.local("rm -rf /src/perdana-indonesia-app/env")
        c.run("pwd")
        c.run("sh /src/scripts/deploy.sh")
