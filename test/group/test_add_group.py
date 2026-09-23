from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="sadsad", header="sdaasd", footer="dsadsadsa"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
