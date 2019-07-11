url = 'localhost'
db = 'prueba'
username = 'demo'
password = 'demo'


from odoo_rpc_client import Client

# assume that odoo server is listening localhost on standard 8069 port and
# have database 'my_db'.
#client = Client('192.168.20.113', 'postgres', 'admin', 'admin', '8071')
client = Client(url, db, username, password)


print('Revisando descuentos: (product.pricelist)')
product_pricelist = client['product.pricelist']
lista_descuentos = product_pricelist.search_records([])

for d in lista_descuentos:
    print('id: ',d.id, ' name: ',d.name)

print('Lineas de descuentos: (product.pricelist.item)')
product_pricelist_item = client['product.pricelist.item']
lista_item_descuentos = product_pricelist_item.search_records([])

descuentos_producto = {}
for l in lista_item_descuentos:
    print(l.name, 'porcentaje: ', l.percent_price, ' categorias: ', l.categ_id)
    if l.categ_id:
        descuentos_producto.update({l.categ_id.id : {'id':l.categ_id.id, 'porcentaje': l.percent_price}})

print("Los descuentos: ",descuentos_producto)
'''
    Productos
'''
productos = client['product.template']  # or You may use 'db.get_obj('sale.order')' if You like
#product_list = productos.search_records([('categ_id', '=', 11)]) #caso sub categoria
product_list = productos.search_records([]) #caso categoria
for producto in product_list:
    if descuentos_producto.get(producto.categ_id.id):
        print('Descuento: ', descuentos_producto.get(producto.categ_id.id)['porcentaje'])
        print('id: ', producto.id, 'name: ', producto.name, 'price: ', producto.list_price, 'active: ', producto.active, 'categoria: ', producto.categ_id, 'existencias: ',producto.qty_available)

