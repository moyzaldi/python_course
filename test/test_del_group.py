from model.group import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sadsad", header="sdaasd", footer="dsadsadsa")) # сначала создаем группу, чтобы тест точно прошел
    app.group.delete_first_group()
    app.session.logout()





