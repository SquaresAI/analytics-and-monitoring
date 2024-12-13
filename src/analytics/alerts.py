def send_alerts():
    print("Checking metrics for alerts...")
    metrics = {"CPU_Usage": 85, "Memory_Usage": 92}
    for metric, value in metrics.items():
        if value > 80:
            print(f"ALERT: {metric} has exceeded the threshold! Current value: {value}%")
    print("Alerts processed.")
