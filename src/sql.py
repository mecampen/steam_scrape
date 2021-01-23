# initialize database
drop_cases = """
	DROP TABLE IF EXISTS cases;
"""

drop_prices = """
	DROP TABLE IF EXISTS prices;
"""

create_cases = """
	CREATE TABLE cases(
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(255)
	);
"""

create_prices = """
	CREATE TABLE prices(
		price_id INT AUTO_INCREMENT PRIMARY KEY,
		case_id INT,
		price VARCHAR(255),
		time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY(case_id) REFERENCES cases(id)
	);
"""

# insert data
insert_case = """
	INSERT INTO cases(name)
	VALUES (%s);
"""

insert_price = """
	INSERT INTO prices(case_id, price)
	VALUES (%s, %s);
"""


# retrieve data
select_all_cases = """
	SELECT id, name
	FROM cases
"""

select_all_prices = """
	SELECT price_id, case_id, price, time
	FROM prices
"""

select_case_id = """
	SELECT id
	FROM cases
	WHERE case=%s 
"""