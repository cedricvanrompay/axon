""" CLI commands
"""

import click
import json

from axon import api


@click.group()
def cli():
    """ Axon is a Matrix Synapse management tool
    """


@cli.group()
def user():
    """ Manager users
    """


@user.command()
@click.argument("userid")
def get(userid):
    """ Query a given user
    """
    print(json.dumps(api.Client().get_user(userid)))


@user.command()
@click.argument("userid")
def sessions(userid):
    """ Query a given user sessions
    """
    print(json.dumps(api.Client().get_user_sessions(userid)))


@user.command()
@click.argument("userid")
@click.option("--displayname")
def update(userid, **kwargs):
    """ Update a given user
    """
    print(json.dumps(api.Client().put_user(userid, **kwargs)))


@user.command()
@click.argument("userid")
@click.option("--erase", type=bool)
def delete(userid, erase=False):
    """ Update a given user
    """
    print(json.dumps(api.Client().delete_user(userid, erase)))


@cli.group()
def room():
    """ Manager rooms
    """


@room.command()
@click.argument("roomid")
def get(roomid):
    """ Get details about a room
    """
    client = api.Client()
    room = client.get_room(roomid)
    room.update(client.get_room_members(roomid))
    print(json.dumps(room))


@room.command()
@click.argument("roomid")
@click.option("--new-room-user-id")
@click.option("--room-name")
@click.option("--message")
@click.option("--block/--no-block", default=False)
@click.option("--purge/--no-purge", default=False)
def delete(roomid, **kwargs):
    """ Delete a given room
    """
    print(json.dumps(api.Client().delete_room(roomid, **kwargs)))


@room.command()
@click.option("--sort")
@click.option("--from", default=0)
@click.option("--limit", default=100)
@click.option("--search")
@click.option("--reverse/--forward", default=False)
def list(reverse, search, **kwargs):
    """ Filter and list rooms
    """
    print(json.dumps(api.Client().list_rooms(
        reverse=reverse,
        search_term=search,
        **kwargs
    )))


if __name__ == "__main__":
    cli()
