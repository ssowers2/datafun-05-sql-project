-- Create two tables for a Doggie Daycare called Pawradise Playcare. Many to 1 relationship, since 1 owner can have many dogs.
CREATE TABLE Owners (
    owner_id TEXT PRIMARY KEY,
    owner_name TEXT NOT NULL,
    phone_number TEXT --since phone numbers can contain leading zeros or special characters should be text
);

CREATE TABLE Dogs (
    dog_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dog_name TEXT NOT NULL,
    breed TEXT,
    age INT,
    owner_id TEXT,
    FOREIGN KEY (owner_id) REFERENCES Owners (owner_id) 
);