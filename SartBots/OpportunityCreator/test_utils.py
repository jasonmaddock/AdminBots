import pytest
from utils import sfdc_login
from env import email


class TestSfdcLogin:
    def test_prod(self):
        instance = "prod"
        driver = sfdc_login(instance, email)
        assert driver.title == "Lightning Experience"
        driver.quit()

    def test_uat(self):
        instance = "uat"
        driver = sfdc_login(instance, email)
        assert driver.title == "Lightning Experience"
        driver.quit()

    def test_qa(self):
        instance = "qa"
        driver = sfdc_login(instance, email)
        assert driver.title == "Lightning Experience"
        driver.quit()
