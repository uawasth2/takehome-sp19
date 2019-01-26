from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

# @app.route("/shows", methods=['GET'])
# def get_all_shows():
#     return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!
@app.route("/shows/<id>", methods=['GET'])
def get_show_by_id(id):
    show = db.getById('shows', int(id))
    if show is None:
        return create_response(status=404, message="No show with this id exists")
    else:
        return create_response({"shows": show}, message="Show successfully displayed")

@app.route("/shows", methods=['GET']) #Gets all shows by query string minEpisodes
def get_show_by_min_episodes():
    min_episodes = int(request.args.get('minEpisodes'))
    show_list = [i for i in db.get('shows') if i["episodes_seen"] >= min_episodes]
    if not show_list:
        return create_response(status=404, message="No show with that many episodes watched exists")
    else:
        return create_response({"shows": show_list}, message="Shows successfully displayed")

@app.route("/shows", methods=['POST']) #Creates new show object
def add_show():
    data = request.get_json()
    if 'name' not in data:
        return create_response(status=422, message="No name provided for new show")
    if 'episodes_seen' not in data:
        return create_response(status=422, message="No number of episodes seen provided for new show")
    new_item = {
        "name": data['name'],
        "episodes_seen": data['episodes_seen']
    }
    return create_response(db.create('shows', new_item), message="New Item Added to DB", status=201)

@app.route("/shows/<id>", methods=['PUT']) #Changes show object
def change_show(id):
    show = db.getById('shows', int(id))
    if show is None:
        return create_response(status=404, message="No show with this id exists")

    new_item = dict()
    data = request.get_json()
    if 'name' in data:
        new_item['name'] = data['name']
    if 'episodes_seen' in data:
        new_item['episodes_seen'] = data['episodes_seen']
    return create_response(data=db.updateById('shows', int(id), new_item), message="Item successfully changed in DB", status=201)


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
