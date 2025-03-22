-- Drivers Table
CREATE TABLE drivers (
    driver_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    license_number VARCHAR(20) UNIQUE NOT NULL,
    contact VARCHAR(15)
);

-- Vehicles Table
CREATE TABLE vehicles (
    vehicle_id VARCHAR(20) PRIMARY KEY, -- e.g., "ABC-123"
    type VARCHAR(50), -- Car, Bike, Truck
    owner_id INT,
    make VARCHAR(50),
    model VARCHAR(50),
    FOREIGN KEY (owner_id) REFERENCES drivers(driver_id)
);

-- Violations Table
CREATE TABLE violations (
    violation_code VARCHAR(10) PRIMARY KEY, -- e.g., "OVSPD"
    description TEXT,
    fine_amount DECIMAL(10, 2) NOT NULL
);

-- Challans Table
CREATE TABLE challans (
    challan_id INT PRIMARY KEY AUTO_INCREMENT,
    driver_id INT,
    vehicle_id VARCHAR(20),
    violation_code VARCHAR(10),
    issue_date DATE NOT NULL,
    location VARCHAR(100),
    paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (violation_code) REFERENCES violations(violation_code)
);