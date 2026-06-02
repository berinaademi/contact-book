from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Contact Book API is running!"


contacts = []


@app.route("/contacts", methods=["GET"])
def get_contacts():
    return jsonify(contacts)


@app.route("/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()
    new_contact = {
        "name": data["name"],
        "phone": data["phone"],
        "email": data["email"]
    }
    contacts.append(new_contact)
    return jsonify({"message": "Contact added successfully!"}), 201


@app.route("/contacts/<name>", methods=["DELETE"])
def delete_contact(name):
    found = False
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            found = True
            return jsonify({"message": "Contact deleted!"})
    return jsonify({"message": "Contact not found!"})


if __name__ == "__main__":
    app.run(debug=True)
