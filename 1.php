<?php
// Database credentials
$servername = "";
$username = ""; // Replace with your MySQL username
$password = "";     // Replace with your MySQL password
$dbname = "india_post";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $sender_name = $_POST['name'];
    $recipient_name = $_POST['recipient_name'];
    $sender_contact = $_POST['sender_contact'];
    $recipient_contact = $_POST['recipient_contact'];
    $delivery_address = $_POST['address'];
    $delivery_date = $_POST['date'];
    $parcel_weight = $_POST['weight'];
    $weight_unit = $_POST['weight-unit'];
    $time_slot = $_POST['timeSlot'];

    // Prepare SQL statement
    $stmt = $conn->prepare("INSERT INTO parcel_deliveries (sender_name, recipient_name, sender_contact, recipient_contact, delivery_address, delivery_date, parcel_weight, weight_unit, time_slot) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssssiss", $sender_name, $recipient_name, $sender_contact, $recipient_contact, $delivery_address, $delivery_date, $parcel_weight, $weight_unit, $time_slot);

    // Execute SQL query
    if ($stmt->execute()) {
        echo "Record saved successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
    $conn->close();
}
?>
