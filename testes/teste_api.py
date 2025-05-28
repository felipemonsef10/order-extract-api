import requests
import json

link = r'http://localhost:5000/pedidos?folder={}'

pasta_monitorada = str(input('Nome da pasta: '))

requisicao = requests.get(link.format(pasta_monitorada))
response = requisicao.json()


for pedido in response['pedidos']:
    nmr_pedido = pedido['order_id']

    with open(fr'jsons\{nmr_pedido}.json', 'w+', encoding='utf-8') as json_pedido:
        json.dump(pedido, json_pedido, ensure_ascii=False)