from flask import Flask, render_template, request, jsonify
from flask.helpers import redirect

app = Flask(__name__, template_folder='templates', static_folder='static')

items = [{
    "id": 1,
    "name": "leo",
}, {
    "id": 2,
    "name": "wil",
}]


#return all items
@app.route('/', methods=["GET"])
def hello():
  return render_template('index.html', items=items)


@app.route('/get', methods=["GET"])
def get_items():
  return jsonify({"message": "success", "items": items}), 200


#return 1 item
@app.route('/<int:item_id>', methods=["GET"])
def idnex(item_id):
  for item in items:
    if item["id"] == item_id:
      return render_template('index2.html', input=item)
  return render_template('index3.html')


@app.route('/User', methods=["POST"])
def post():
  name = request.form.get('name')
  print(name)
  length = len(items)
  new_item = {
      "id": length + 1,
      "name": name,
  }

  # Append the new item to the items list
  items.append(new_item)
  print(items)
  return render_template('index.html', items=items)


# @app.route('/<int:item_id>', methods=["DELETE"])
# def delete(item_id):
#   for item in items:
#     if item["id"] == item_id:
#       delete = request.form.get('delete')
#       items.remove(item)
#       return render_template('index2.html', input=item)
#   return render_template('index3.html')


@app.route('/<int:item_id>', methods=["DELETE"])
def delete(item_id):
  for item in items:
    if item["id"] == item_id:
      items.remove(item)
      return jsonify({"message": "success", "items": items}), 200
  return jsonify({"error": "Item not found"}), 400


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
