import psycopg2

# conecting database
con = psycopg2.connect(database="valorant")

# creating cursor
cur = con.cursor()

# inserting
n = int(input())
for i in range(n):
    name, fav_agent = input().split()
    cur.execute("insert into names(name,fav_agent) values (%s,%s)", (name, fav_agent))

# executing command
cur.execute("select * from names")
# fetching
rows = cur.fetchall()

for r in rows:
    print(f"name = {r[0]} => fav_agent = {r[1]}")


# commiting changes
con.commit()
# closing cursor and connection
cur.close()

con.close()
