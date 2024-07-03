import pymongo

# MongoDB connection information
mongo_uri = "mongodb://localhost:27017/"
mongo_db = "logs"
mongo_collection = "nginx"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

# Total number of documents in the collection
total_logs = collection.count_documents({})

print(f"{total_logs} logs")

# Counting methods: GET, POST, PUT, PATCH, DELETE
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

print("Methods:")
for method, count in method_counts.items():
    print(f"    method {method}: {count}")

# Counting specific method and path combination
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")

# Close MongoDB connection
client.close()
