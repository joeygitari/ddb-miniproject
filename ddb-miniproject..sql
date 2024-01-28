USE `ddb-miniproject`;

CREATE TABLE Travellers (
    travellerID INT PRIMARY KEY,
    travellerName VARCHAR(50),
    travellerAge INT,
    travellerCountry VARCHAR(50)
);

-- insert travellers data
INSERT INTO Travellers (travellerID, travellerName, travellerAge, travellerCountry)
VALUES
    (1, 'John Doe', 15, 'Kenya'),
    (2, 'Jane Smith', 10, 'Canada'),
    (3, 'Alice Johnson', 22, 'Kenya'),
    (4, 'Tony Stark', 40, 'USA'),
    (5, 'Steve Rogers', 56, 'Wakanda'),
    (6, 'Natasha Romanoff', 35, 'Russia'),
    (7, 'Thor Odinson', 50, 'Asgard'),
    (8, 'Bruce Banner', 30, 'USA'),
    (9, 'Peter Parker', 20, 'USA'),
    (10, 'TChalla', 35, 'Wakanda'),
    (11, 'Carol Danvers', 30, 'Canada'),
    (12, 'Stephen Strange', 45, 'Canada'),
    (13, 'Peter Quill', 40, 'Asgard'),
    (14, 'Wanda Maximoff', 30, 'Kenya'),
    (15, 'Scott Lang', 45, 'USA');

-- Hotels table
CREATE TABLE Hotels (
    hotelID INT PRIMARY KEY,
    travellerID INT,
    hotelName VARCHAR(100),
    roomType VARCHAR(50),
    price DECIMAL(10, 2),
    FOREIGN KEY (travellerID) REFERENCES Travellers(travellerID)
);

-- insert hotel data
INSERT INTO Hotels (hotelID, travellerID, hotelName, roomType, price)
VALUES
    (1, 1, 'Hotel A', 'Single', 150.00),
    (2, 1, 'Hotel B', 'Double', 200.00),
    (3, 2, 'Hotel C', 'Single', 120.00),
    (4, 4, 'Stark Tower Hotel', 'Suite', 500.00),
    (5, 5, 'The Avengers Mansion', 'Penthouse', 1000.00),
    (6, 6, 'Red Room Inn', 'Single', 100.00),
    (7, 7, 'Asgardian Palace', 'Double', 300.00),
    (8, 8, 'Gamma Base Lodge', 'Single', 120.00),
    (9, 9, 'Parker Residence', 'Penthouse', 3000.00),
    (10, 10, 'Wakanda Royal Palace', 'Suite', 2000.00),
    (11, 11, 'Air Force Base Hotel', 'Double', 180.00),
    (12, 12, 'Sanctum Sanctorum Inn', 'Single', 300.00),
    (13, 13, 'Milano Inn', 'Single', 250.00),
    (14, 14, 'Sokovian Embassy Residence', 'Penthouse', 13000.00),
    (15, 15, 'Ant-Mans Tiny Hotel', 'Suite', 5000.00);


-- Flights table
CREATE TABLE Flights (
    flightID INT PRIMARY KEY,
    travellerID INT,
    flightName VARCHAR(100),
    departureLocation VARCHAR(50),
    arrivalLocation VARCHAR(50),
    departureDate DATE,
    departureTime TIME,
    arrivalDate DATE,
    arrivalTime TIME,
    FOREIGN KEY (travellerID) REFERENCES Travellers(travellerID)
);

-- insert flights data
INSERT INTO Flights (flightID, travellerID, flightName, departureLocation, arrivalLocation, departureDate, departureTime, arrivalDate, arrivalTime)
VALUES
    (1, 1, 'Flight X', 'USA', 'Canada','2024-02-02', '08:00', '2024-02-02', '10:00'),
    (2, 2, 'Flight Y', 'Canada', 'USA', '2024-04-02', '09:00', '2024-04-02','11:00'),
    (3, 3, 'Flight Z', 'USA', 'Wakanda','2024-05-06', '10:00', '2024-05-08','14:00'),
    (4, 4, 'Stark Industries Flight', 'USA', 'Sokovia', '2024-12-02','12:00', '2024-12-03','15:00'),
    (5, 5, 'Captain America Express', 'USA', 'Wakanda', '2024-11-02','11:00', '2024-11-04','14:00'),
    (6, 6, 'Black Widow Jet', 'Russia', 'USA', '2024-01-02','10:00','2024-01-05', '12:00'),
    (7, 7, 'Bifrost Airlines', 'Asgard', 'USA', '2024-01-19','09:00','2024-01-20', '12:00'),
    (8, 8, 'Gamma Ray Airways', 'USA', 'Canada','2024-03-03', '08:00','2024-03-03', '10:00'),
    (9, 9, 'Web-Slinger Airlines', 'USA', 'Germany', '2024-07-02','07:00', '2024-07-03','09:00'),
    (10, 10, 'Wakanda Air', 'Wakanda', 'USA','2024-02-02', '06:00', '2024-02-05','09:00'),
    (11, 11, 'Air Force One', 'USA', 'Russia', '2024-08-02','05:00', '2024-08-04','07:00'),
    (12, 12, 'Mystic Airways', 'USA', 'Hong Kong', '2024-09-02','04:00', '2024-09-05','08:00'),
    (13, 13, 'Guardians Starship', 'USA', 'Space','2024-10-02', '03:00','2024-10-05', '10:00'),
    (14, 14, 'Sokovian Airlines', 'Sokovia', 'USA','2024-11-02', '02:00', '2024-11-03','06:00'),
    (15, 15, 'Ant-Mans Tiny Flight', 'USA', 'Microverse', '2024-02-02','01:00','2024-02-02', '03:00');


-- Bookings table
CREATE TABLE Bookings (
    bookingID INT PRIMARY KEY,
    travellerID INT,
    hotelID INT,
    flightID INT,
    bookingDate DATE,
    FOREIGN KEY (travellerID) REFERENCES Travellers(travellerID),
    FOREIGN KEY (hotelID) REFERENCES Hotels(hotelID),
    FOREIGN KEY (flightID) REFERENCES Flights(flightID)
);

-- insert Bookings data
INSERT INTO Bookings (bookingID, travellerID, hotelID, flightID, bookingDate)
VALUES
    (1, 1, 1, 1, '2024-02-01'),
    (2, 2, 2, 2, '2024-04-04'),
    (3, 3, 3, 3, '2024-03-05'),
    (4, 4, 4, 4, '2024-01-30'),
    (5, 5, 5, 5, '2024-05-20'),
    (6, 6, 6, 6, '2024-06-29'),
    (7, 7, 7, 7, '2024-07-28'),
    (8, 8, 8, 8, '2024-08-12'),
    (9, 9, 9, 9, '2024-09-22'),
    (10, 10, 10, 10, '2024-10-02'),
    (11, 11, 11, 11, '2024-12-15'),
    (12, 12, 12, 12, '2024-02-26'),
    (13, 13, 13, 13, '2024-11-19'),
    (14, 14, 14, 14, '2024-04-03'),
    (15, 15, 15, 15, '2024-05-05');