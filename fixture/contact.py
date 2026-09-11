from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT,"add new").click()
        self.fill_contact_form(contact)
        # submit  contact creation
        wd.find_element(By.XPATH,'//input[@name="submit"]').click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home_phone)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("work", contact.work_phone)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("email2", contact.email2)
        self.change_contact_field_value("email3", contact.email3)
        self.change_contact_field_value("homepage", contact.homepage)
        self.select_contact_dropdown_value("bday",contact.bday)
        self.select_contact_dropdown_value("bmonth",contact.bmonth)
        self.change_contact_field_value("byear", contact.byear)
        self.select_contact_dropdown_value("aday", contact.bday)
        self.select_contact_dropdown_value("amonth", contact.bmonth)
        self.change_contact_field_value("ayear", contact.byear)


    def select_contact_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def select_first_icon_edit_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,"//img[@alt='Edit']").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_icon_edit_contact()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # update contact form
        wd.find_element(By.NAME,"update").click()
        self.return_to_home_page()

    def del_first_contact_from_card_edit(self):
        wd = self.app.wd
        self.select_first_icon_edit_contact()
        # delete contact
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()

    def del_first_contact_from_list(self):
        wd = self.app.wd
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()



