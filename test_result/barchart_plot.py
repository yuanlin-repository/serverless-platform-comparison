import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv_and_get_mean(csv_file):
    try:
        df = pd.read_csv(csv_file, header=None)
        data = [float(value) for value in df.iloc[0].values]
        return np.mean(data)
    except Exception as e:
        print(f"Error reading file {csv_file}: {e}")
        sys.exit(1)

def plot_latency_comparison(azure_log, azure_local, openfaas_log, openfaas_local):
    azure_log_mean = read_csv_and_get_mean(azure_log)
    azure_local_mean = read_csv_and_get_mean(azure_local)
    openfaas_log_mean = read_csv_and_get_mean(openfaas_log)
    openfaas_local_mean = read_csv_and_get_mean(openfaas_local)

    labels = ['Azure', 'OpenFaaS']
    log_means = [azure_log_mean, openfaas_log_mean]
    local_means = [azure_local_mean, openfaas_local_mean]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, log_means, width, label='Server Side Latency')
    rects2 = ax.bar(x + width/2, local_means, width, label='Client Side Latency')

    ax.set_xlabel('Platform')
    ax.set_ylabel('Latency (ms)') 
    ax.set_title('Average Latency Comparison: Azure vs OpenFaaS')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),textcoords="offset points",ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error invalid arguments")
        sys.exit(1)

    plot_latency_comparison(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])