def generate_dashboard():
    print("Generating dashboard for analytics...")
    metrics = {"CPU_Usage": 85, "Memory_Usage": 92}
    for metric, value in metrics.items():
        print(f"Dashboard: {metric} - {value}%")
    print("Dashboard generated successfully.")
