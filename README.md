# Contents

README.md: Project introduction
faas-test: Specific implementation of azure function and openfaas function, using IntelliJ IDEA to build the project and Gradle to manage dependencies
script: Python and shell scripts used for testing
test_result: Scripts for generating result graphs

```
├── README.md
├── faas-test
│   ├── azure-function
│   ├── openfaas-emptyfunc
│   └── openfaas-fibonacci
├── script
│   ├── execute_test.sh
│   ├── openfaas_cold_start_test.sh
│   ├── send_http_hundred_request.py
│   ├── send_single_request.py
│   └── test_azurefunc_cold_start.py
└── test_result
    ├── azurefunc_cold_start_data.csv
    ├── azurefunc_hot_start_data.csv
    ├── azurefunc_hot_start_send_from_laptop.csv
    ├── openfaas_cold_start_data.csv
    ├── openfaas_hot_start_data.csv
    ├── openfaas_hot_start_send_from_laptop.csv
    ├── concurrent_performance_test.csv
    ├── barchart_plot.py
    ├── boxplot.py
    ├── concurrent_performance_comparison_plot.py
    ├── cold_start_latency_comparison.jpg
    ├── hot_start_latency_comparison.jpg
    ├── latency_concurrency_comparison.jpg
    ├── server_client_side_latency_comparison.jpg
    └── throughput_concurrency_comparison.jpg
```

