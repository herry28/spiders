import requests
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('zouhai','ZOUhai28')

    def test_get_user(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'zouhai')
        self.assertEqual(result['email','1061006551@qq.com'])


if __name__ == '__main__':
    unittest.main()
