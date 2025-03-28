import time
import requests
import statistics
import csv

URL = "https://fibonaccifunction001.azurewebsites.net/api/empty_function"

latency_list = []

def send_100_requests():
    for i in range(0, 100):
        try:
            time.sleep(5)
            start = time.time()
            response = requests.post(URL, data="", timeout=10)
            latency = time.time() - start
            latency_list.append(int(latency * 1000))
            print("Test Completed, latency: {:.0f}ms".format(latency * 1000))
        except requests.exceptions.RequestException:
            print("Exception occured~")

def save_latency_to_csv(filename="hot_start.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(latency_list)
        print(f"\nLatency data saved to {filename}")
    except Exception as e:
        print(f"\nError saving CSV file: {e}")

if __name__ == "__main__":
    send_100_requests()
    save_latency_to_csv()
