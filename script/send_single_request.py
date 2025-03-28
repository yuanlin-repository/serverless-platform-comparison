import time
import requests
import statistics

URL = "http://172.167.92.49:8080/function/emptyfunc"
# URL = "http://131.145.88.24:8080/function/fibonacci"
# URL = "https://fibonaccifunction001.azurewebsites.net/api/empty_function"

def send_request():
    try:
        start = time.time()
        response = requests.post(URL, data="", timeout=5)
        latency = time.time() - start
        print("\nTest Completed, latency: {:.0f}ms".format(latency * 1000))
    except requests.exceptions.RequestException:
        print("\nException occured~")

if __name__ == "__main__":
    send_request()

