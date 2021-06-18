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

    def create(self, name, parent_id=1, hide_dept=False, dept_permits=None, user_permits=None, outer_dept=None,
               outer_dept_only_self=None, outer_permit_users=None, outer_permit_depts=None, create_dept_group=None, order=None, source_identifier=None):
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
        data = {'name': name}
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
