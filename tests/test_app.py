import os
import unittest

from assertpy import assert_that
import requests

import behave_restful.app as br_app

class TestBehaveRestfulApp(unittest.TestCase):

    def setUp(self):
        self.test_dir = '/a/path'
        self.context = ContextDouble()
        self.app = br_app.BehaveRestfulApp()
        self.app.initialize_context(self.context, self.test_dir)


    def test_context_is_initialized_with_test_dir(self):
        assert_that(self.context.test_dir).is_equal_to(self.test_dir)


    def test_context_is_initialized_with_current_working_dir(self):
        assert_that(self.context.working_dir, os.getcwd())


    def test_context_default_session_is_initialized_with_requests_module(self):
        assert_that(self.context.default_session).is_same_as(requests)


    def test_sets_the_session_to_the_default_session(self):
        assert_that(self.context.session).is_same_as(self.context.default_session)



class ContextDouble(object):
    def __init__(self):
        self.config = self
        self.userdata = {}



if __name__=="__main__":
    unittest.main()