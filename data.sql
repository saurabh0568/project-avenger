CREATE DATABASE india_post_db;

USE india_post_db;

CREATE TABLE parcel_deliveries (
    id INT PRIMARY KEY AUTO_INCREMENT,  
    customer_id INT NOT NULL,
    sender_name VARCHAR(255) NOT NULL,
    recipient_name VARCHAR(255) NOT NULL,
    sender_contact VARCHAR(20) NOT NULL,
    recipient_contact VARCHAR(20) NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_pincode VARCHAR(6) NOT NULL, 
    delivery_date DATE NOT NULL,
    parcel_weight FLOAT NOT NULL,
    weight_unit ENUM('g', 'kg') NOT NULL,
    time_slot VARCHAR(50) NOT NULL
);



-- Create the Postman table
CREATE TABLE Postman (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    pincode VARCHAR(10)
);

-- Insert 30 records into the Postman table
INSERT INTO Postman (id, name, pincode) 
VALUES
(1, 'Rahul Sharma', '110001'),
(2, 'Priya Verma', '110002'),
(3, 'Anil Kumar', '110003'),
(4, 'Sunita Singh', '110004'),
(5, 'Rajesh Mehta', '110005'),
(6, 'Neeta Joshi', '110006'),
(7, 'Vikram Sethi', '110007'),
(8, 'Anita Rao', '110008'),
(9, 'Deepak Agarwal', '110009'),
(10, 'Suman Chaudhary', '110010'),
(11, 'Manish Gupta', '110011'),
(12, 'Sneha Iyer', '110012'),
(13, 'Karan Kapoor', '110013'),
(14, 'Geeta Sood', '110014'),
(15, 'Rajiv Bansal', '110015'),
(16, 'Tanvi Malhotra', '110016'),
(17, 'Arvind Choudhary', '110017'),
(18, 'Pooja Saxena', '110018'),
(19, 'Nikhil Sharma', '110019'),
(20, 'Ritika Jain', '110020'),
(21, 'Mohit Yadav', '110021'),
(22, 'Sakshi Verma', '110022'),
(23, 'Gaurav Mehta', '110023'),
(24, 'Nisha Reddy', '110024'),
(25, 'Amit Tiwari', '110025'),
(26, 'Kavita Bhardwaj', '110026'),
(27, 'Pankaj Srivastava', '110027'),
(28, 'Neha Thakur', '110028'),
(29, 'Rohit Kapoor', '110029'),
(30, 'Simran Malhotra', '110030');
