-- Count how many dogs each owner has
SELECT owner_id, COUNT(*) AS dog_count
FROM Dogs
GROUP BY owner_id;

-- Find the average age of dogs per owner
SELECT owner_id, AVG(age) AS avg_dog_age
FROM Dogs
GROUP BY owner_id;