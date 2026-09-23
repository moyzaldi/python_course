from model.group import Group

def test_modify_group_name(app):
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(name="Second"))


def test_modify_group_header(app):
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(header="Second"))


def test_modify_group_footer(app):
    app.group.create(Group(name="First", header="First", footer="First")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(footer="Second"))
