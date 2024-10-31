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

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/get_postman', methods=['POST'])
def get_postman():
    data = request.get_json()
    postman_id = data.get('id')
    pincode = data.get('pincode')
    delivery_date = data.get('date')

    if not postman_id or not pincode or not delivery_date:
        return jsonify({'message': 'ID, Pincode, and Delivery Date are required'}), 400

    cur = mysql.connection.cursor()

    # Query Postman details
    cur.execute("SELECT id, name, phone_number, pincode FROM Postman WHERE id = %s AND pincode = %s", (postman_id, pincode))
    postman_result = cur.fetchone()

    if not postman_result:
        cur.close()
        return jsonify({'message': 'No records found for the given ID and Pincode'}), 404

    # Query deliveries
    cur.execute(""" 
        SELECT id, recipient_name, recipient_contact, recipient_address, delivery_date, delivery_time_slot 
        FROM parcel_deliveries 
        WHERE recipient_pincode = %s AND delivery_date = %s
    """, (pincode, delivery_date))
    delivery_result = cur.fetchall()

    # Query pickups
    cur.execute(""" 
        SELECT id, sender_name, sender_contact, sender_address, pickup_date, pickup_time_slot 
        FROM parcel_deliveries
        WHERE sender_pincode = %s AND pickup_date = %s
    """, (pincode, delivery_date))
    pickup_result = cur.fetchall()

    cur.close()

    # Prepare deliveries data
    deliveries = [{
        'id': delivery[0],
        'recipient_name': delivery[1],
        'recipient_contact': delivery[2],
        'delivery_address': delivery[3],
        'delivery_date': delivery[4],
        'delivery_time_slot': delivery[5]
    } for delivery in delivery_result]

    # Prepare pickups data
    pickups = [{
        'id': pickup[0],
        'sender_name': pickup[1],
        'sender_contact': pickup[2],
        'sender_address': pickup[3],
        'pickup_date': pickup[4],
        'pickup_time_slot': pickup[5]
    } for pickup in pickup_result]

    # Prepare postman data
    postman_data = {
        'id': postman_result[0],
        'name': postman_result[1],
        'phone_number': postman_result[2],
        'pincode': postman_result[3],
        'profile_image': None  # Add logic for postman profile image if necessary
    }

    return jsonify({'postman': postman_data, 'deliveries': deliveries, 'pickups': pickups})

if __name__ == '__main__':
    app.run(debug=True)
