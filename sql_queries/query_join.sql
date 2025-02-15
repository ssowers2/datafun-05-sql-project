-- Get all dogs with their owner's name using INNER JOIN
SELECT Dogs.dog_name, Dogs.breed, Dogs.age, Owners.owner_name
FROM Dogs
INNER JOIN Owners ON Dogs.owner_id = Owners.owner_id;

-- Get all owners and their dogs, including owners who have no dogs using LEFT JOIN
SELECT Owners.owner_name, Dogs.dog_name, Dogs.breed
FROM Owners
LEFT JOIN Dogs ON Owners.owner_id = Dogs.owner_id;