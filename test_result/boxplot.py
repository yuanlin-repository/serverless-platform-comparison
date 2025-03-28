import sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_horizontal_boxplots(csv_file1, csv_file2):
    try:
        df1 = pd.read_csv(csv_file1, header=None)
        data1 = [float(value) for value in df1.iloc[0].values]
    except Exception as e:
        print(f"Error reading file {csv_file1}: {e}")
        return

    try:
        df2 = pd.read_csv(csv_file2, header=None)
        data2 = [float(value) for value in df2.iloc[0].values]
    except Exception as e:
        print(f"Error reading file {csv_file2}: {e}")
        return

    combined_data = [data1, data2]
    labels = ["Azure","OpenFaaS"]

    plt.figure(figsize=(8, 5))
    plt.boxplot(combined_data, vert=False, patch_artist=True, labels=labels)
    plt.title("Hot Start Latency Comparison")
    plt.xlabel("Latency (ms)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error invalid arguments")
        sys.exit(1)

    csv_filename1 = sys.argv[1]
    csv_filename2 = sys.argv[2]

    plot_horizontal_boxplots(csv_filename1, csv_filename2)
