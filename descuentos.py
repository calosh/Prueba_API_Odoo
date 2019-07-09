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
lista_item_descuentos = product_pricelist_item.search_records([('pricelist_id','=',5)])
for l in lista_item_descuentos:
    print(l.name, 'porcentaje: ', l.percent_price, ' categorias: ', l.categ_id)
