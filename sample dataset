-- Insert Drivers
INSERT INTO drivers (name, license_number, contact) VALUES
('Aarav Sharma', 'DL07AB2020', '+919876543210'),    -- Delhi
('Priyanka Reddy', 'KA05CD2021', '+919876543211'),  -- Karnataka
('Rohan Deshpande', 'MH01EF2022', '+919876543212'), -- Maharashtra 
('Ananya Patel', 'GJ03GH2023', '+919876543213'),    -- Gujarat
('Vikram Singh', 'RJ09IJ2024', '+919876543214'),    -- Rajasthan
('Deepika Iyer', 'TN02KL2025', '+919876543215'),    -- Tamil Nadu
('Arjun Mehta', 'MP08MN2026', '+919876543216'),     -- Madhya Pradesh
('Sanya Verma', 'UP04OP2027', '+919876543217'),     -- Uttar Pradesh
('Kiran Kumar', 'WB06QR2028', '+919876543218'),     -- West Bengal
('Neha Gupta', 'HR07ST2029', '+919876543219');      -- Haryana

-- Insert Violations
INSERT INTO violations (violation_code, description, fine_amount) VALUES
('DL-01', 'Driving without license', 2000.00),
('DL-02', 'Expired driving license', 1000.00),
('SPD-01', 'Over speeding (20-40 km/h)', 1500.00),
('SPD-02', 'Dangerous speeding (>40 km/h)', 5000.00),
('MVI-01', 'Using mobile while driving', 2500.00),
('NHL-01', 'No helmet (Rider)', 1000.00),
('NHL-02', 'No helmet (Pillion)', 500.00),
('SEAT-01', 'Not wearing seatbelt', 1000.00),
('PUC-01', 'Expired pollution certificate', 2000.00),
('DUI-01', 'Driving under influence', 10000.00);

-- Insert Vehicles
INSERT INTO vehicles (vehicle_id, type, owner_id, make, model) VALUES
('DL7CAB2020', 'Car', 1, 'Maruti', 'Swift'),
('KA05CD2021', 'Bike', 2, 'Royal Enfield', 'Classic 350'),
('MH01EF2022', 'Truck', 3, 'Tata', 'Prima'),
('GJ03GH2023', 'Car', 4, 'Hyundai', 'Creta'),
('RJ09IJ2024', 'SUV', 5, 'Mahindra', 'Scorpio'),
('TN02KL2025', 'Car', 6, 'Toyota', 'Innova'),
('MP08MN2026', 'Bike', 7, 'Hero', 'Splendor'),
('UP04OP2027', 'Bus', 8, 'Volvo', '9400'),
('WB06QR2028', 'Car', 9, 'Honda', 'City'),
('HR07ST2029', 'Truck', 10, 'Ashok Leyland', 'Boss');

-- Insert Challans
INSERT INTO challans (driver_id, vehicle_id, violation_code, issue_date, location, paid) VALUES
-- Delhi Cases
(1, 'DL7CAB2020', 'SPD-01', '2024-03-15', 'NH48, Gurgaon', 1),
(1, 'DL7CAB2020', 'MVI-01', '2024-07-22', 'Connaught Place, Delhi', 0),

-- Bengaluru Cases 
(2, 'KA05CD2021', 'NHL-01', '2024-02-14', 'MG Road, Bengaluru', 0),
(2, 'KA05CD2021', 'SPD-01', '2024-11-30', 'Electronic City, Bengaluru', 1),

-- Mumbai Cases
(3, 'MH01EF2022', 'SPD-02', '2024-05-05', 'Mumbai-Pune Expressway', 1),
(3, 'MH01EF2022', 'DUI-01', '2024-09-18', 'Bandra-Worli Sea Link', 0),

-- Ahmedabad Cases
(4, 'GJ03GH2023', 'SEAT-01', '2024-04-10', 'Sabarmati Riverfront', 0),

-- Jaipur Cases
(5, 'RJ09IJ2024', 'DUI-01', '2024-06-15', 'Amber Fort Road', 0),
(5, 'RJ09IJ2024', 'PUC-01', '2024-12-05', 'Sanganer Toll Plaza', 1),

-- Chennai Cases
(6, 'TN02KL2025', 'SPD-02', '2024-01-20', 'Marina Beach Road', 1),

-- Indore Cases
(7, 'MP08MN2026', 'NHL-02', '2024-03-08', 'Rajwada Palace Road', 1),

-- Uttar Pradesh Cases
(8, 'UP04OP2027', 'SPD-01', '2024-05-30', 'Agra Yamuna Expressway', 0),

-- Kolkata Cases
(9, 'WB06QR2028', 'DL-01', '2024-09-05', 'Howrah Bridge', 0),

-- Haryana Cases
(10, 'HR07ST2029', 'PUC-01', '2024-02-28', 'Manesar Industrial Area', 0),
(10, 'HR07ST2029', 'SPD-02', '2024-06-14', 'KMP Expressway', 1),

-- Repeat Offenders Pattern
(1, 'DL7CAB2020', 'SEAT-01', '2024-08-08', 'Dwarka Sector 21', 0),
(3, 'MH01EF2022', 'SPD-01', '2024-10-31', 'Vashi Toll Plaza', 1),
(5, 'RJ09IJ2024', 'DL-02', '2024-04-22', 'Ajmer Highway', 0);
