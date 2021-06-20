#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


class Department(Core):

    def get(self, dept_id=None, lang=None):
        """
        get department list

        params:
        dept_id: int id of department, get all departments if dept_id is None
        lang: language of contacts

        :return :list of departments
        """
        # [{'auto_add_user': True, 'create_dept_group': True, 'dept_id': 147953855, 'name': '财务部', 'parent_id': 1}]
        url = f"{URL}/topapi/v2/department/listsub"
        res = self._post(url, data={
            "dept_id": dept_id,
            "language": lang
        })
        return res['result']

    def create(self, name, parent_id=1, **kwargs):
        """
        create a department.

        :param name:  department name
        :param parent_id: parent department id, default 1 root department.
        :param hide_dept: whether hide the department
        :param dept_permits: who can view the department, limit 200 departments.
        :param user_permits: who can view the department, limit 200 persons.
        :param outer_dept: restrict members of this department from viewing the address book.
        :param outer_dept_only_self: whether members of this department can only see the address book of their department and subordinate departments
        :param outer_permit_users: specify the userid list of address book users that the members of this department can view, the total cannot exceed 200
        :param outer_permit_depts: specify a list of department IDs in the address book that members of this department can view, the total number cannot exceed 200
        :param create_dept_group: whether to create an enterprise group associated with this department
        :param order: for the sort value in the parent department, the lower order value is sorted first
        :source_identifier: department identification field, developers can use this field to uniquely identify a department and map it with the department in the external address book of DingDing

        :return dept_id: deparment id of new created department.
        """
        url = f"{URL}/topapi/v2/department/create"
        data = {'name': name, 'parent_id': parent_id}
        data.update(kwargs)
        res = self._post(url, data=data)
        return res['result']['dept_id']

    def update(self, dept_id, **kwargs):
        """
        udpate department.

        :param dept_id: the department id which to update.
        :param name:  department name
        :param language:  language of department.
        :param parent_id: parent department id, default 1 root department.
        :param hide_dept: whether hide the department
        :param dept_permits: who can view the department, limit 200 departments.
        :param user_permits: who can view the department, limit 200 persons.
        :param outer_dept: restrict members of this department from viewing the address book.
        :param outer_dept_only_self: whether members of this department can only see the address book of their department and subordinate departments
        :param outer_permit_users: specify the userid list of address book users that the members of this department can view, the total cannot exceed 200
        :param outer_permit_depts: specify a list of department IDs in the address book that members of this department can view, the total number cannot exceed 200
        :param create_dept_group: whether to create an enterprise group associated with this department
        :param order: for the sort value in the parent department, the lower order value is sorted first
        :param source_identifier: department identification field, developers can use this field to uniquely identify a department and map it with the department in the external address book of DingDing
        :param auto_add_user: whether auto add user into group when user been added to department.
        :param dept_manager_userid_list: update manager list of department
        :param group_contain_sub_dept: whether has child department.
        :param group_contain_outer_dept: whether has outside department
        :param group_contain_hidden_dept: whether has hide department.
        :param org_dept_owner: the host of group.

        :return True or False
        """
        url = f"{URL}/topapi/v2/department/update"
        data = {'dept_id': dept_id}
        data.update(kwargs)
        res = self._post(url, data=data)
        return True

    def delete(self, dept_id):
        """
        delete department

        :param dept_id: department id which is going to be deleted.
        :return True
        """
        url = f"{URL}/topapi/v2/department/delete"
        data = {'dept_id': dept_id}
        self._post(url, data=data)
        return True

    def get_info(self, dept_id, lang=None):
        """
        get detail infos of department.

        :param dept_id: department id
        :param lang: language of department.
        """
        url = f"{URL}/topapi/v2/department/get"
        data = {'dept_id': dept_id, 'language': lang}
        res = self._post(url, data=data)
        return res['result']

    def get_children(self, dept_id):
        """
        get childen of the department.

         :param dept_id: department id
         :return departments: id list of children deparments
        """
        url = f"{URL}/topapi/v2/department/listsubid"
        data = {'dept_id': dept_id}
        res = self._post(url, data)
        return res['result']['dept_id_list']

    def get_user_departments(self, userid):
        """
        get all departments of given user.

        :param userid: user id 
        :return parent_list: user's departments.
        """
        url = f"{URL}/topapi/v2/department/listparentbyuser"
        data = {'userid': userid}
        res = self._post(url, data)
        return res['result']['parent_list']

    def get_parents(self, dept_id):
        """
        get parents of one department.

        :param dept_id: id of department
        :param parent_id_list: id list of parent departments
        """
        url = f"{URL}/topapi/v2/department/listparentbydept"
        data = {'dept_id': dept_id}
        res = self._post(url, data)
        return res['result']['parent_id_list']


class Role(Core):

    def create(self, name, groupid):
        """
        create role

        :param name: role name
        :param groupid: group id
        """
        url = f"{URL}/role/add_role"
        data = {'roleName': name, 'groupId': groupid}
        res = self._post(url, data)
        return res['roleId']

    def create_group(self, name):
        """
        create role group

        :param name: group name
        :return groupId: group id
        """
        url = f"{URL}/role/add_role_group"
        data = {'name': name}
        res = self._post(url, data)
        return res['groupId']

    def update_role(self, roleid, rolename):
        """
        update role

        :param roleid: role id
        :param rolename: rolename
        :return True
        """
        url = f"{URL}/role/update_role"
        data = {'roleid': roleid, 'rolename': rolename}
        res = self._post(url, data)
        return True

    def add_roles_to_users(self, roles, users):
        """
        add roles to users.

        :param roles: roles
        :param users: users
        :return True
        """
        url = "f{URL}/role/addrolesforemps"
        data = {'roleIds': roles, 'userIds': users}
        res = self._post(url, data)
        return True

    def delete(self, role_id):
        """
        delete role

        :param role_id: id of role which is going to be deleted.
        :return True
        """
        url = f"{URL}/topapi/role/deleterole"
        data = f"{'role_id':role_id}"
        res = self._post(url, data)
        return True

    def delete_users_roles(self, roleids, userids):
        """
        delete users' roles

        :param roleIds: roles
        :param userids: users
        """
        url = f"{URL}/topapi/role/removerolesforemps"
        data = f"{'roleIds':roleids,'userIds':userids}"
        res = self._post(url, data)
        return True

    def get_by_groupid(self, group_id):
        """
        get role groups list.

        :param group_id: id of group.
        :return role_group: role group detail
        """

        url = f"{URL}/topapi/role/getrolegroup"
        data = f"{'group_id':group_id}"
        res = self._post(url, data)
        return res['role_group']
