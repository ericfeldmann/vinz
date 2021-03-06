"""
.. module:: rest.user_group
   :synopsis: REST Resource definitions relating to user_groups
"""
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import user_group as user_group_api


user_group_fields = {
    #'uri': fields.Url(endpoint='user_group'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'user_list': fields.List(fields.String)
}

user_group_parser = reqparse.RequestParser()
user_group_parser.add_argument("name", type=str, location='json')



class UserGroupResource(Resource):
    """
    REST endpoint to serve up details of a specific User Group from the database.
    """

    @marshal_with(user_group_fields)
    def get(self, user_group_id):
        return user_group_api.get_user_group(user_group_id)

    def put(self, user_group_id):
        #TODO update information for a specific user
        return

    def delete(self, user_group_id):
        user_group_api.delete_user(user_group_id)
        return '', HTTP_STATUS.DELETED


class UserGroupResourceList(Resource):
    """
    REST endpoint to serve up a list of User Group resources from the database.
    """
    @marshal_with(user_group_fields)
    def get(self):
  #check if the user is admin   checkAdmin(user_id)
        return user_group_api.get_user_groups()

    def post(self):
        args = user_group_parser.parse_args()
        user_group = user_group_api.create_user_group(**args)
        return marshal(user_group , user_group_fields), HTTP_STATUS.CREATED

