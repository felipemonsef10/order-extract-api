import os
import re
import pdfplumber
from collections import OrderedDict
import json


def verify_folder(folder_path):
    if len(os.listdir(folder_path)) > 0:
        lista_pdfs = [pdf for pdf in os.listdir(folder_path) if '.pdf' in pdf]
        return lista_pdfs
    else:
        return False
    

def extract_text_from_pdf(pdf_file):
    extracted_texts = []

    with pdfplumber.open(pdf_file) as pdf:
        for index, pagina in enumerate(pdf.pages, start=1):
            # print(pagina)

            text = pagina.extract_text()
            
            if index % 2 == 1:
                extracted_texts.append(text)

    return extracted_texts


def standardize_text(text):
    pattern_order_id = re.compile(r'N°\s\d{1}.\d{3}.\d{3}')
    pattern_cod_fornecedor = re.compile(r'\d+')
    pattern_quantidade = re.compile(r'\d+,\d{3}')
    pattern_valor_unitario = re.compile(r'(\d+,\d{2})\s')

    json_pedido = {
        'order_id': '',
        'items': []
    }

    numero_pedido = re.findall(pattern_order_id, text)
    json_pedido['order_id'] = numero_pedido[0]

    try:
        header_index = text.index('Cód. Fornecedor Item de Estoque Emb. Quantidade Vlr. Unit. Desconto Vlr. Liq. IPI % IPI $ Frete Imp.Ret. IR.Gnre Vlr. Total')
        end_table_index = text.index('Observações')
        text_items = text[header_index:end_table_index - 1]
        # print('Página Ímpar')
    except Exception as erro:
        return erro


    linhas_text = text_items.split('\n')


    for linha in linhas_text[1:]:
        cod_fornecedor = re.findall(pattern_cod_fornecedor, linha)[0]
        quantidade_item = re.findall(pattern_quantidade, linha)[0].replace(',', '.')
        valor_unitario = re.findall(pattern_valor_unitario, linha)[0].replace(',', '.')

        json_pedido['items'].append({
            'sku_seller_id': str(cod_fornecedor),
            'quantity': float(quantidade_item),
            'sale_price': float(valor_unitario)
        })
    

    json_values_to_order = []

    for item in json_pedido.items():
        json_values_to_order.append(item)
        order_dict = OrderedDict(json_values_to_order)
    
    return order_dict


def processar_pedidos(parametro_folder_monitored):
    pdfs_pedidos = verify_folder(parametro_folder_monitored)
    list_json_pedidos = []

    if not pdfs_pedidos:
        return json.dumps({'pedidos': 'nenhum pdf encontrado na pasta'})
    
    for pdf in pdfs_pedidos:
        texts_extracted = extract_text_from_pdf(os.path.join(parametro_folder_monitored, pdf))
        for text_pedido in texts_extracted:
            json_pedido = standardize_text(text_pedido)
            list_json_pedidos.append(json_pedido)

    jsons_pedidos = json.dumps({'pedidos': list_json_pedidos}, ensure_ascii=False, indent=2)

    return jsons_pedidos