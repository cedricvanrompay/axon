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
    client = api.Client()
    user = client.get_user(userid)
    user.update(client.get_user_sessions(userid))
    user.update(client.get_user_rooms(userid))
    print(json.dumps(user))


@user.command()
@click.argument("userid")
@click.option("--displayname")
def update(userid, **kwargs):
    """ Update a given user
    """
    print(json.dumps(api.Client().put_user(userid, **kwargs)))


@user.command()
@click.argument("userid")
@click.option("--erase/--no-erase", default=False)
def delete(userid, erase=False):
    """ Update a given user
    """
    print(json.dumps(api.Client().delete_user(userid, erase)))


@cli.group()
def room():
    """ Manage rooms
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


@cli.group()
def media():
    """ Manage media
    """


@media.command()
@click.option("--days", default=7, type=int)
def purge(days):
    """ Purge medias older than a number of days
    """
    print(json.dumps(api.Client().purge_remote_media(
        days=days
    )))


if __name__ == "__main__":
    cli()
