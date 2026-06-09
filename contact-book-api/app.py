from flask import Flask, jsonify, request
import sqlite3


def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "name TEXT,"
                   "phone TEXT,"
                   "email TEXT)")
    conn.commit()
    conn.close()


app = Flask(__name__)


@app.route("/")
def home():
    return "Contact Book API is running!"


contacts = []


@app.route("/contacts", methods=["GET"])
def get_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    contacts_list = []
    for row in contacts:
        contacts_list.append({
            "id": row[0],
            "name": row[1],
            "phone": row[2],
            "email": row[3]
        })
    return jsonify(contacts_list)


@app.route("/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()
    name = data["name"]
    phone = data["phone"]
    email = data["email"]

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts(name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Contact added successfully!"}), 201


@app.route("/contacts/<name>", methods=["DELETE"])
def delete_contact(name):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name, ))
    if cursor.rowcount == 0:
        return jsonify({"message": "Contact not found"})
    conn.commit()
    conn.close()

    return jsonify({"message": "Contact deleted!"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
