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
    Productos
'''
print('PRODUCTOS')
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
product_list = productos.search_records([('active', '=', 'True')])
for p in product_list:
    print('id: ', p.id, 'name: ', p.name, 'price: ', p.list_price, 'active: ', p.active, 'categoria: ', p.categ_id, ' existencias: ',p.qty_available)



'''
    Producto
'''
print('PRODUCTO')
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
product_list = productos.search_records([('id', '=', 25)])
for p in product_list:
    print('id: ', p.id, 'name: ', p.name, 'price: ', p.list_price, 'active: ', p.active, 'categoria: ', p.categ_id, 'existencias: ',p.qty_available)


producto = product_list[0]
