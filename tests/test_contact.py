#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from unittest import TestCase, TestSuite
from dingtalk.dingtalk import DingTalk


class TestContact(TestCase):

    department_id = None
    role_id = None

    @classmethod
    def setUpClass(cls):
        cls.appkey = "dingtjjs1pr7nlgmtoxc"
        cls.appsecret = "8a6Ltc8_w-BNpqVOXg3dUH_1PHxxgmWnuf6Gt1ZcQqaMR3fYDDD6rs3Jnmzxr9uy"
        cls.dingtalk = DingTalk("", cls.appkey, cls.appsecret)

    def test_create_department(self):
        if not TestContact.department_id:
            res = self.dingtalk.department.create("Test")
            self.assertIsInstance(res, int, res)
            TestContact.department_id = res

    def test_get_departments(self):
        res = self.dingtalk.department.get()
        self.assertGreaterEqual(len(res), 0, res)
        for dept in res:
            if dept['name'].lower() == 'test':
                TestContact.department_id = dept['dept_id']

    def test_update_department(self):
        res = self.dingtalk.department.update(self.department_id, name="TEST")
        self.assertTrue(res)

    def test_get_department_info(self):
        res = self.dingtalk.department.get_info(self.department_id)
        self.assertIsInstance(res, dict)

    def test_get_department_children(self):
        res = self.dingtalk.department.get_children(self.department_id)
        self.assertIsInstance(res, list)

    def test_get_user_departments(self):
        res = self.dingtalk.department.get_user_departments(100)
        self.assertIsInstance(res, list)

    def test_get_parents(self):
        res = self.dingtalk.department.get_parents(self.department_id)
        self.assertIsInstance(res, list)

    def test_delete_department(self):
        res = self.dingtalk.department.delete(self.department_id)
        self.assertTrue(res)

    def test_create_role(self):
        res = self.dingtalk.role.create("TestRole")
        self.assertIsInstance(res, int)
        TestContact.role_id = res

    def test_create_role_group(self):
        res = self.dingtalk.role.create_group("TestRoleGroup")
        self.assertIsInstance(res, int)

    def test_update_role(self):
        res = self.dingtalk.role.update_role(TestContact.role_id, "TESTRole")
        self.assertTrue(res)

    def test_add_roles_to_users(self):
        res = self.dingtalk.role.add_roles_to_users()
        self.assertTrue(res)

    def test_delete_role(self):
        res = self.dingtalk.role.delete(TestContact.role_id)
        self.assertTrue(res)


if __name__ == "__main__":
    suit = TestSuite()
    suit.addTest(TestContact("test_get_departments"))
    suit.addTest(TestContact("test_create_department"))
    suit.addTest(TestContact("test_update_department"))
    suit.addTest(TestContact("test_get_department_children"))
    suit.addTest(TestContact("test_get_parents"))
    suit.addTest(TestContact("test_delete_department"))
    suit.addTest(TestContact("test_create_role_group"))
    unittest.TextTestRunner(verbosity=3).run(suit)
