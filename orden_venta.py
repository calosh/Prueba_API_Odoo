url = 'localhost'
db = 'prueba'
username = 'demo'
password = 'demo'


from odoo_rpc_client import Client

# assume that odoo server is listening localhost on standard 8069 port and
# have database 'my_db'.
#client = Client('192.168.20.113', 'postgres', 'admin', 'admin', '8071')
client = Client(url, db, username, password)

sale_order = client['sale.order']
ordenes_compra = sale_order.search_records([])
print('Ordenes de compra: ', ordenes_compra)
for orden in ordenes_compra:
    print(orden)

print('Crear ordenes de compra: ')
orden_compra = sale_order.create_record({'partner_id': 25})

sale_order_line = client['sale.order.line']


print('PRODUCTO')
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
product_list = productos.search_records([('id', '=', 35)])
for p in product_list:
    print('id: ', p.id, 'name: ', p.name, 'price: ', p.list_price, 'active: ', p.active, 'categoria: ', p.categ_id)


producto = product_list[0]


detalle_pedido_orden = sale_order_line.create_record({'product_id':producto.id, 'name':producto.name, 'price_unit': producto.list_price, 'quantity':5, 'order_id':orden_compra.id, 'account_id':290, 'discount':50})

#account_invoice_line.create_record({'product_id':producto2.id, 'name':producto2.name, 'price_unit': producto2.list_price, 'quantity':3, 'invoice_id':factura_obj.id, 'account_id':290})
