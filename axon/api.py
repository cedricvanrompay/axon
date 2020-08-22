""" Synapse admin API functions

See https://github.com/matrix-org/synapse/tree/master/docs/admin_api for
documentaiton.
"""

import axon


class Client(axon.BaseClient):
    """ API client implementation
    """
        
    def get_user(self, userid):
        """ Get information about a given user
        """
        return self.query(
            "get",  "/_synapse/admin/v2/users/" + userid
        )

    def put_user(self, userid, **kwargs):
        """ Create or update information about a given user
        """
        return self.query(
            "put", "/_synapse/admin/v2/users/" + userid,
            body=kwargs
        )

    def delete_user(self, userid, erase=False):
        """ Delete a given user
        """
        return self.query(
            "post", "/_synapse/admin/v1/deactivate/" + userid,
            body=dict(erase=erase)
        )

    def get_user_sessions(self, userid):
        """ Get a given user sessions
        """
        return self.query(
            "get", "/_synapse/admin/v1/whois/" + userid
        )

    def get_room(self, roomid):
        """ Get details about a room
        """
        return self.query(
            "get", "/_synapse/admin/v1/rooms/" + roomid
        )

    def delete_room(self, roomid, **kwargs):
        """ Delete a room
        """
        return self.query(
            "post", "/_synapse/admin/v1/rooms/" + roomid + "/delete",
            body=kwargs
        )

    def get_room_members(self, roomid):
        """ Get a list of room members
        """
        return self.query(
            "get", "/_synapse/admin/v1/rooms/" + roomid + "/members"
        )

    def list_rooms(self, reverse, **kwargs):
        """ List rooms after filtering
        """
        kwargs["dir"] = "b" if reverse else "f"
        return self.query(
            "get", "/_synapse/admin/v1/rooms",
            qs=kwargs
        )
