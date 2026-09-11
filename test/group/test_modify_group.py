from model.group import Group

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(name="Second"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(header="Second"))
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(footer="Second"))
    app.session.logout()