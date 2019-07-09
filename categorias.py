url = 'localhost'
db = 'prueba'
username = 'demo'
password = 'demo'


from odoo_rpc_client import Client

# assume that odoo server is listening localhost on standard 8069 port and
# have database 'my_db'.
#client = Client('192.168.20.113', 'postgres', 'admin', 'admin', '8071')
client = Client(url, db, username, password)

'''
    Categorias
'''
print('CATEGORIAS')
categorias = client['product.category']
categorias_list = categorias.search_records([])
for cat in categorias_list:
    print('Las categorias son: ', cat.name)
    if cat.parent_id:
        print('Padre: ', cat.parent_id.name)