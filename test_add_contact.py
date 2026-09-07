# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ivan", middlename="Ivanovish", lastname="Ivanov", title="ada",
                                        company="New",
                                        nickname="Brave", address="address address address",
                                        home_phone="+7 11111", mobile_phone="+7 2222", work_phone="+7 33333",
                                        email1="email1@ya.ru",
                                        email2="email2@ya.ru", email3="email3@ya.ru",
                                        homepage="https://dzen.ru/", bday="27", bmonth="December", byear="2000",
                                        aday="25",
                                        amonth="December", ayear="2021"))
    app.logout()
