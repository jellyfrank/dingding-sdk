#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


class Role(Core):

    def create(self, name, groupid=None):
        """
        create role

        :param name: role name
        :param groupid: group id
        """
        url = f"{URL}/role/add_role"
        data = {'roleName': name, 'groupId': groupid}
        res = self._post(url, data)
        return res['roleId']
