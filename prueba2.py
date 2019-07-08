
import odoolib

connection = odoolib.get_connection(hostname="localhost", database="prueba", \
    login="demo", password="demo")
user_model = connection.get_model("res.users")
ids = user_model.search([("login", "=", "demo")])
user_info = user_model.read(ids[0], ["name"])
print(user_info["name"])
# will print "Administrator"