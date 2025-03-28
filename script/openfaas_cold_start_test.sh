#!/bin/bash

# perform 100 tests
for i in {1..100}
do
    echo "[$(date)] Running test #$i" | tee -a open_faas_cold_start_data.txt

    # 1. redeploy the function
    echo "Deploy function fibonacci again..."
    faas-cli deploy -f stack.yaml
    
    # 2. wait
    sleep 10

    # 3. execute python script
    echo "Invoking function..."
    python single_request.py | tee -a open_faas_cold_start_data.txt

    echo "--------------------------------------" | tee -a open_faas_cold_start_data.txt

    sleep 1
done

echo "All tests completed."
