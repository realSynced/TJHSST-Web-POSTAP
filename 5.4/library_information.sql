DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS checkouts;

-- Title	                                                        Author First	        Author Last	                Publication Year	
-- Why Rocks are Awesome	                                        Melissa	                Anderson	                1990	
-- How to pick up big rocks	                                        Reginald                Worthington	Farnsworth III	1974	
-- In Search of the World’s Most Interesting Rocks	                Shaun	                O'Malley	                2006	
-- Hidden Secrets: The Story of Rocks	                            Liam Michael	        Walker	                    2014	
-- North American Cloud Patterns, A Survey	                        Victoria	            Collins	                    2008	
-- Once upon a cloud: Tales On the Density of Dreams and Boulders	George	                Brown	                    2017	
-- The Magesty of Tectonic Plates	                                Anna Marie	            Green	                    1999	
-- Geothermal Structures Beneath the Sea Floor	                    Jameson	                Clark	                    2008	
-- Colliding Continents and the Rocks they Create	                Olivia                  Harrison	                1978	
-- A Cloud Collector's Guide to Grounded Thoughts	                Katherine	            LeBlanc	                    2020	
-- How Rain Makes Rocks Beautiful	                                Brian	                Davis	                    2011	
-- Cloudy with a Chance of Pebbles	                                Jameson	                Clark	                    2023	
-- Fog on the Fault Line: A Memoir in Stone and Sky	                Fiona	                Murray	2005	

CREATE TABLE books (
    b_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author_first_name TEXT NOT NULL,
    author_last_name TEXT NOT NULL,
    publication_year INT NOT NULL
);

-- Title	                                        Patron	    Checkout	    Checkin	        Fines
-- Why Rocks are Awesome	                        1005	    2024-07-15	    2024-08-10	    3.75
-- Why Rocks are Awesome	                        1010	    2024-10-14	    2024-11-04	    0
-- Fog on the Fault Line: A Memoir in Stone and Sky	1929	    2025-01-12	    2025-02-10	    6
-- In Search of the World’s Most Interesting Rocks	1005	    2025-04-24	    2025-05-08	    0
-- Geothermal Structures Beneath the Sea Floor	    1010	    2020-05-16	    2026-06-02	    0
-- How Rain Makes Rocks Beautiful	                1003	    2021-04-11	    2021-05-11	    6.75
-- Geothermal Structures Beneath the Sea Floor	    1755	    2023-05-20	    2023-06-07	    0
-- Hidden Secrets: The Story of Rocks	            1209	    2024-08-25	    2024-09-18	    2.25
-- How to pick up big rocks	                        1003	    2021-04-11	    2021-04-27	    0
-- How to pick up big rocks	                        1003	    2022-06-04	    2022-06-24	    0
-- How to pick up big rocks	                        1003	    2023-11-09	    2023-11-28	    0
-- How to pick up big rocks	                        1003	    2025-03-15	    2025-04-12	    5.25

CREATE TABLE checkouts (
    c_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL REFERENCES books(title),
    patron INT NOT NULL,
    check_in DATE,
    fines DECIMAL(10, 2) DEFAULT 0.00
);

INSERT INTO books (b_id, title, author_first_name, author_last_name, publication_year) 
VALUES
(0, "Why Rocks are Awesome", "Melissa", "Anderson", 1990),
(1, "How to pick up big rocks", "Reginald", "Worthington-Farnsworth III", 1974),
(2, "In Search of the World’s Most Interesting Rocks", "Shaun", "O'Malley", 2006),
(3, "Hidden Secrets: The Story of Rocks", "Liam Michael", "Walker", 2014),
(4, "North American Cloud Patterns, A Survey", "Victoria", "Collins", 2008),
(5, "Once upon a cloud: Tales On the Density of Dreams and Boulders", "George", "Brown", 2017),
(6, "The Magesty of Tectonic Plates", "Anna Marie", "Green", 1999),
(7, "Geothermal Structures Beneath the Sea Floor", "Jameson", "Clark", 2008),
(8, "Colliding Continents and the Rocks they Create", "Olivia", "Harrison", 1978),
(9, "A Cloud Collector's Guide to Grounded Thoughts", "Katherine", "LeBlanc", 2020),
(10, "How Rain Makes Rocks Beautiful", "Brian", "Davis", 2011),
(11, "Cloudy with a Chance of Pebbles", "Jameson", "Clark", 2023),
(12, "Fog on the Fault Line: A Memoir in Stone and Sky", "Fiona", "Murray", 2005);


INSERT INTO checkouts (c_id, title, patron, check_in, fines) 
VALUES
(0, "Why Rocks are Awesome", 1005, "2024-07-15", 3.75),
(1, "Why Rocks are Awesome", 1010, "2024-10-14", 0),
(2, "Fog on the Fault Line: A Memoir in Stone and Sky", 1929, "2025-01-12", 6),
(3, "In Search of the World’s Most Interesting Rocks", 1005, "2025-04-24", 0),
(4, "Geothermal Structures Beneath the Sea Floor", 1010, "2020-05-16", 0),
(5, "How Rain Makes Rocks Beautiful", 1003, "2021-04-11", 6.75),
(6, "Geothermal Structures Beneath the Sea Floor", 1755, "2023-05-20", 0),
(7, "Hidden Secrets: The Story of Rocks", 1209, "2024-08-25", 2.25),
(8, "How to pick up big rocks", 1003, "2021-04-11", 0),
(9, "How to pick up big rocks", 1003, "2022-06-04", 0),
(10, "How to pick up big rocks", 1003, "2023-11-09", 0),
(11, "How to pick up big rocks", 1003, "2025-03-15", 5.25);