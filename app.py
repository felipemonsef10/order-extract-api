# import os
from funcoes import processar_pedidos # verify_folder, extract_text_from_pdf, standardize_text, processar_pedidos
from flask import Flask, Response, request
# import json


app = Flask(__name__)


@app.route('/pedidos', methods=['GET'])
def lista_pedidos():
    parametro_folder_monitored = request.args.get('folder')

    jsons_pedidos = processar_pedidos(parametro_folder_monitored)

    return Response(jsons_pedidos, content_type='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# http://localhost:5000/pedidos?folder=pasta_monitorada
# http://xxx.xx.x.xxx:5000/pedidos?folder=pasta_monitorada