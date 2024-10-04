from flask import Flask, jsonify, request, send_from_directory
from flask_mysqldb import MySQL
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'odd*357.'
app.config['MYSQL_DB'] = 'india_post_db'

mysql = MySQL(app)

# Serve the index.html file from the static folder as default
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

# Route to fetch records based on id, pincode, and delivery date
@app.route('/get_postman', methods=['POST'])
def get_postman():
    data = request.get_json()
    postman_id = data.get('id')
    pincode = data.get('pincode')
    delivery_date = data.get('date')

    if not postman_id or not pincode or not delivery_date:
        return jsonify({'message': 'ID, Pincode, and Delivery Date are required'}), 400

    cur = mysql.connection.cursor()

    # Query to fetch Postman details based on id and pincode
    cur.execute("SELECT * FROM Postman WHERE id = %s AND pincode = %s", (postman_id, pincode))
    postman_result = cur.fetchone()

    if not postman_result:
        cur.close()
        return jsonify({'message': 'No records found for the given ID and Pincode'}), 404

    # Query to fetch parcel deliveries based on the entered pincode and delivery date
    cur.execute("""
        SELECT recipient_name, recipient_contact, delivery_address, delivery_date, time_slot 
        FROM parcel_deliveries 
        WHERE delivery_pincode = %s AND delivery_date = %s
    """, (pincode, delivery_date))
    delivery_result = cur.fetchall()
    cur.close()

    deliveries = []
    for delivery in delivery_result:
        deliveries.append({
            'recipient_name': delivery[0],
            'recipient_contact': delivery[1],
            'delivery_address': delivery[2],
            'delivery_date': delivery[3],
            'time_slot': delivery[4]
        })

    return jsonify({
        'postman': {
            'id': postman_result[0],
            'name': postman_result[1],
            'pincode': postman_result[2]
        },
        'deliveries': deliveries
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
