
def process_data(data):
    print("Processing data...")
    # Example processing
    gpu_average = sum(data["gpu_usage"]) / len(data["gpu_usage"])
    transaction_success_rate = sum(1 for tx in data["transaction_logs"] if tx["status"] == "success") / len(data["transaction_logs"])
    
    processed_data = {
        "gpu_average_usage": gpu_average,
        "transaction_success_rate": transaction_success_rate
    }
    print(f"Processed data: {processed_data}")
    return processed_data
