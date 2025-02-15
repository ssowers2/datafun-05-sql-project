-- Count total number of dogs
SELECT COUNT(*) AS total_dogs FROM Dogs;

-- Find the average age of all dogs
SELECT AVG(age) AS avg_dog_age FROM Dogs;

-- Sum of all owners' phone numbers
SELECT SUM(length(phone_number)) AS total_phone_digits FROM Owners;