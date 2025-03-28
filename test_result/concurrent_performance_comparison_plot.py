import pandas as pd
import matplotlib.pyplot as plt

def plot_latency_throughput(csv_filename):
    df = pd.read_csv(csv_filename)

    azure_data = df[df['Platform'] == 'Azure']
    openfaas_data = df[df['Platform'] == 'OpenFaaS']

    plt.figure(figsize=(10, 5))
    plt.plot(azure_data['Concurrency'], azure_data['Latency(ms)'], marker='o', label='Azure Latency')
    plt.plot(openfaas_data['Concurrency'], openfaas_data['Latency(ms)'], marker='o', label='OpenFaaS Latency')
    plt.xlabel('Concurrency')
    plt.ylabel('Latency (ms)')
    plt.title('Latency vs Concurrency')
    plt.grid(True)
    plt.legend()
    plt.xticks(azure_data['Concurrency'])
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(azure_data['Concurrency'], azure_data['Throughput'], marker='o', label='Azure Throughput')
    plt.plot(openfaas_data['Concurrency'], openfaas_data['Throughput'], marker='o', label='OpenFaaS Throughput')
    plt.xlabel('Concurrency')
    plt.ylabel('Throughput (requests/sec)')
    plt.title('Throughput vs Concurrency')
    plt.grid(True)
    plt.legend()
    plt.xticks(azure_data['Concurrency'])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_filename = 'concurrent_performance_test.csv'
    plot_latency_throughput(csv_filename)

    