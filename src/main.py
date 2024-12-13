from analytics import data_collection, data_processing

if __name__ == "__main__":
    print("Starting Analytics and Monitoring module...")
    data_collection.initialize_collection()
    processed_data = data_processing.process_data(data_collection.collect_data())
    print("Analytics and Monitoring successfully completed.")
