import json

from flask import Flask, request, Response
app = Flask(__name__)

required_fields = ['title', 'topics', 'ownerId', 'locationString']

tables = [
    {
        "tableId": 1,
        "title": "TableC @ BostonHacks",
        "topics": ["#masseffect", "#typescript", "#rickandmorty"],
        "ownerId": 42,
        "locationString": "Metcalf Hall, upstairs",
    },
    {
        "tableId": 2,
        "title": "Spline Reticulation",
        "topics": ["#anything", "#anime"],
        "ownerId": 69,
        "locationString": "Sherman Gallery"
    }
]
counter = 3

@app.route('/api/v1/tables', methods=['GET', 'POST'])
def table_resource():
    if request.method == 'GET':
        return Response(json.dumps(tables), mimetype='application/json')
    elif request.method == 'POST':
        return Response(insert_into_dict(request.json))


def insert_into_dict(new_table: dict):
    in_fields = new_table.keys()
    for field in required_fields:
        if field not in in_fields:
            return 400
    global counter
    new_table['tableId'] = counter
    tables.append(new_table)
    counter += 1
    return 204


if __name__ == '__main__':
    app.run('0.0.0.0', 8069, debug=True)
