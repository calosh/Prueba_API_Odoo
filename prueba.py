url = 'localhost'
db = 'prueba'
username = 'demo'
password = 'demo'


from odoo_rpc_client import Client

# assume that odoo server is listening localhost on standard 8069 port and
# have database 'my_db'.
#client = Client('192.168.20.113', 'postgres', 'admin', 'admin', '8071')
client = Client(url, db, username, password)

# get current user
client.user
print(client.user.name)
'''
    Categorias
'''
print('CATEGORIAS')
categorias = client['product.category']
categorias_list = categorias.search_records([])
for cat in categorias_list:
    print('Las categorias son: ', cat)

'''
    Productos
'''
print('PRODUCTOS')
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
product_list = productos.search_records([('active', '=', 'True')])
for p in product_list:
    print('id: ', p.id, 'name: ', p.name, 'price: ', p.list_price, 'active: ', p.active, 'categoria: ', p.categ_id)



'''
    Producto
'''
print('PRODUCTO')
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
product_list = productos.search_records([('id', '=', 25)])
for p in product_list:
    print('id: ', p.id, 'name: ', p.name, 'price: ', p.list_price, 'active: ', p.active, 'categoria: ', p.categ_id)


'''
    Facturas
'''
print('FACTURAS')
facturas = client['account.invoice']
facturas_list = facturas.search_records([])
for f in facturas_list:
    print(f)


'''
    Crear usuario
print('Crear usuario')
partner_obj = client['res.partner']
carlos = partner_obj.create_record({'name':'Carlos'})
print(carlos.name)
'''




print('Crear factura')
factura_obj = facturas.create_record({'partner_id': 25, 'invoice_line_ids':[(0, 0, {'product_id':31, 'quantity':2})]})
print(factura_obj.partner_id)

#lines = factura_obj.get('invoice_line_ids')
#print('si linea: ', lines)
#lines.create_record({'product_id': 31, 'invoice_id':factura_obj.id})
#print('product_id: ', lines.product_id)

'''
# Get the new line and add the tax

lines = oerp.get('account.invoice.line')

new_line = lines.browse(line_id)

new_line.invoice_line_tax_id = tax_ids_array

oerp.write_record(new_line)
'''







