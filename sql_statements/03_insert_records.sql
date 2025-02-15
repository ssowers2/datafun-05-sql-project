-- Insert records into the Owners table
INSERT INTO Owners (owner_id, owner_name, phone_number) VALUES
('O001', 'Sarah Miller', '555-1234'),
('O002', 'John Doe', '555-5678'),
('O003', 'Lisa Kennedy', '555-9876'),
('O004', 'James Carter', '555-1122'),
('O005', 'Emily Watson', '555-3344'),
('O006', 'Michael Brown', '555-5566'),
('O007', 'Olivia Parker', '555-7788'),
('O008', 'David Johnson', '555-9900'),
('O009', 'Sophia Martinez', '555-2233'),
('O010', 'Daniel Wilson', '555-4455');

-- Insert records into the Dogs table
INSERT INTO Dogs (dog_name, breed, age, owner_id) VALUES
('Bella', 'Labrador', 3, 'O001'),
('Max', 'Poodle', 2, 'O002'),
('Rocky', 'Bulldog', 4, 'O003'),
('Daisy', 'Beagle', 1, 'O004'),
('Charlie', 'Golden Retriever', 5, 'O005'),
('Luna', 'German Shepherd', 3, 'O006'),
('Milo', 'Corgi', 2, 'O007'),
('Bailey', 'Husky', 4, 'O008'),
('Coco', 'Dachshund', 1, 'O009'),
('Teddy', 'Border Collie', 6, 'O010');