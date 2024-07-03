#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main(collection):
    """ log stats """
    num_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    results = {method: 0 for method in methods}  # Use a dictionary for results
    
    # Count number of logs for each HTTP method
    for method in methods:
        num_method = collection.count_documents({"method": method})
        results[method] = num_method
    
    # Count number of status checks
    num_status_check = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{num_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {results[method]}")
    
    print(f"{num_status_check} status check")


if __name__ == "__main__":
    try:
        client = MongoClient()
        db = client.logs
        logs = db.nginx
        main(logs)
    except Exception as e:
        print(f"Error: {e}")
