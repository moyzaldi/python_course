from model.group import Group

def test_modify_group_name(app):
    if app.group.count()== 0:
        app.group.create(Group(name="sadsad", header="sdaasd", footer="dsadsadsa")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(name="Second"))


def test_modify_group_header(app):
    if app.group.count()== 0:
        app.group.create(Group(name="sadsad", header="sdaasd", footer="dsadsadsa")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(header="Second"))


def test_modify_group_footer(app):
    if app.group.count()== 0:
        app.group.create(Group(name="sadsad", header="sdaasd", footer="dsadsadsa")) # сначала создаем группу, чтобы тест точно прошел
    app.group.modify_first_group(Group(footer="Second"))
