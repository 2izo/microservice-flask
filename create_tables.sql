CREATE SCHEMA IF NOT EXISTS car_hiring_management;
USE car_hiring_management;
CREATE TABLE IF NOT EXISTS models (
  model_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS vehicles(
vehicle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
model_id INT NOT NULL,
CONSTRAINT fk_model_id FOREIGN KEY (model_id) REFERENCES models(model_id)
);

CREATE TABLE IF NOT EXISTS small_cars(
vehicle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
capacity INT NOT NULL DEFAULT 4,
CONSTRAINT fk_vehicle_id_small_cars FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

CREATE TABLE IF NOT EXISTS family_cars(
vehicle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
capacity INT NOT NULL DEFAULT 7,
CONSTRAINT fk_vehicle_id_family_cars FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

CREATE TABLE IF NOT EXISTS vans(
vehicle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
capacity INT NOT NULL DEFAULT 10,
CONSTRAINT fk_vehicle_id_vans FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

CREATE TABLE IF NOT EXISTS customers (
customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name varchar(100) NOT NULL,
phone varchar(30) NOT NULL,
email varchar(50));

CREATE TABLE IF NOT EXISTS bookings(
booking_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
customer_id INT NOT NULL,
vehicle_id INT NOT NULL,
cost DECIMAL(10,2) NOT NULL,
start_date DATE NOT NULL CHECK (start_date <=  SYSDATE() + INTERVAL 7 DAY),
end_date DATE NOT NULL CHECK (end_date <= SYSDATE() + INTERVAL 14 DAY),
CONSTRAINT fk_vehicle_id_booking FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
CONSTRAINT fk_customer_id_bookings FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

