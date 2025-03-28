#!/bin/bash

# executing cold start test
./openfaas_cold_start_test.sh

# executing hot start test
python3 send_http_hundred_request.py

# executing faascli test
python3 send_faascli_hundred_request.py
