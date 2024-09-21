CREATE DATABASE india_post;

USE india_post;

CREATE TABLE parcel_deliveries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_name VARCHAR(255) NOT NULL,
    recipient_name VARCHAR(255) NOT NULL,
    sender_contact VARCHAR(20) NOT NULL,
    recipient_contact VARCHAR(20) NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_date DATE NOT NULL,
    parcel_weight FLOAT NOT NULL,
    weight_unit ENUM('g', 'kg') NOT NULL,
    time_slot VARCHAR(50) NOT NULL
);
