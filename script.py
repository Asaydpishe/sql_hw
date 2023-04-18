import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=dvdrental user=postgres host=localhost password = yourpassword")












answer_list = []
# Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query
# cur.execute("""Select title,length from film
# order by length desc
# limit 10;""")

# # Retrieve query results
# records = cur.fetchall()
# cur = conn.cursor()

# answer_list.append(records)
# print(answer_list)
###############################################
# cur = conn.cursor()
# cur.execute("""Select  film.film_id,film.title,film_category.category_id from film
# join film_category on film.film_id = film_category.category_id
# order by rental_rate desc
# limit (1);""")
# records = cur.fetchall()
# cur = conn.cursor()
# answer_list.append(records)
# print(answer_list)
###############################################
# cur = conn.cursor()
# cur.execute("""Select customer.first_name,customer.last_name,film.length from customer
# join rental on rental.customer_id = customer.customer_id
# join inventory on rental.inventory_id = inventory.inventory_id
# join film on inventory.film_id = film.film_id
# order by film.length desc
# limit (5);
# """)
# records = cur.fetchall()
# cur = conn.cursor()
# answer_list.append(records)
# print(answer_list)
###############################################
# cur = conn.cursor()
# cur.execute("""""")
# records = cur.fetchall()
# cur = conn.cursor()
# answer_list.append(records)
# print(answer_list)
###############################################
# cur = conn.cursor()
# cur.execute("""Select title,length from film
# order by length desc
# limit 10;""")
# records = cur.fetchall()
# cur = conn.cursor()
# answer_list.append(records)
# print(answer_list)

