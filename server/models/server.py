"""
.. module:: models.server
   :synopsis: Database models relating to servers

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from mongoengine import Document
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField

from models.audit import AuditableMixin
from models.auth import User
from models.auth import UserGroup


class Server(Document, AuditableMixin):
    name = StringField(required=True)
    hostname = StringField(required=True)
    user_list = ListField(ReferenceField(User))
    group_list = ListField(ReferenceField(UserGroup))

    def get_users(self):
        """
        Gets all of the users that have access to the machine.
        This includes users added directly and through groups.
        """
        users = set()

        # Getting users added directly to the server
        for user in self.user_list:
            users.add(user)

        # Getting users that are in groups on the server
        for group in self.group_list:
            for user in group.user_list:
                users.add(user)

        return users

    def get_usernames(self):
        """
        Gets all of the usernames for the users on the server.
        """
        users = self.get_users()
        return [user.username for user in users]


class ServerGroup(Document, AuditableMixin):
    name = StringField(required=True)
    server_list = ListField(ReferenceField(Server))

    def get_servers(self):
        return set(self.server_list)



