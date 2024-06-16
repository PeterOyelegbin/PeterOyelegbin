from decouple import config
import psycopg2 as postgres
import pymongo as mongodb

print("start")
# Connect to PostgreSQL database
conn = postgres.connect(
    dbname = config('DB_NAME'),
    user = config('DB_USER'),
    password = config('DB_PASS'),
    host = config('DB_HOST'),
    port = config('DB_PORT')
)
print("connected")
# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM public.api_project")

# Fetch all the rows from the result set
rows = cursor.fetchall()
print(rows)
# Process the rows as needed
for row in rows:
    print(rows)
    # Extract the data from the row
    id = row[0]
    title = row[1]
    # category = row[2]
    cover_image = row[2]
    description = row[3]
    project_url = row[4]
    github_url = row[5]
    date = row[6]


    # Connect to the MongoDB database
    client = mongodb("mongodb://your_mongodb_connection_string")
    db = client["peter_portfolio"]

    # Create a MongoDB collection
    collection = db["your_mongodb_collection"]

    # Create a document to store the extracted data
    document = {
        'id': id,
        "title": title,
        # "category": category,
        "cover_image": cover_image,
        "description": description,
        "project_url": project_url,
        "github_url": github_url,
        "date": date
    }

    # Insert the document into the MongoDB collection
    collection.insert_one(document)


# Close the cursor and connection
cursor.close()
conn.close()
