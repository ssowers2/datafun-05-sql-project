-- Get all dogs older than 3 years
SELECT * FROM Dogs WHERE age > 3;

-- Get all owners whose names start with 'S'
SELECT * FROM Owners WHERE owner_name LIKE 'S%';

-- Get dogs owned by 'Lisa Kennedy'
SELECT Dogs.* FROM Dogs
JOIN Owners ON Dogs.owner_id = Owners.owner_id
WHERE Owners.owner_name = 'Lisa Kennedy';