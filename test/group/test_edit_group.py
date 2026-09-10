from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.edit_first_group(Group(name="Second", header="Second", footer="Second"))
    app.session.logout()