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
					price_id INT AUTO_INCREMENT PRIMARY KEY
					case_id INT,
					time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
					FOREIGN KEY(case_id) REFERENCES cases(id)
				);
				"""

# insert data

# retrieve data