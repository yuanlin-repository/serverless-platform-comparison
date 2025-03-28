package org.example.functions;

import java.util.*;
import com.microsoft.azure.functions.annotation.*;
import com.microsoft.azure.functions.*;

/**
 * Azure Functions with HTTP Trigger.
 */
public class FibonacciFunction {
    /**
     * This function listens at endpoint "/api/HttpTriggerJava". Two ways to invoke it using "curl" command in bash:
     * 1. curl -d "HTTP Body" {your host}/api/HttpTriggerJava
     * 2. curl {your host}/api/HttpTriggerJava?name=HTTP%20Query
     */
    @FunctionName("fibonacci")
    public HttpResponseMessage run(
            @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.FUNCTION) HttpRequestMessage<Optional<String>> request,
            final ExecutionContext context) {
        context.getLogger().info("Java HTTP trigger processed a request.");

        int res = calculateFibonacci(30);
        return request.createResponseBuilder(HttpStatus.OK).body(res).build();
    }

    /**
     * Calculate fibonacci number
     * @param number Which Fibonacci number
     * @return Fibonacci number
     */
    private int calculateFibonacci(int number) {
        if (number == 1) {
            return 0;
        } else if (number == 2) {
            return 1;
        }
        int num1 = 0, num2 = 1, res = 0;
        for (int i = 3; i <= number; i++) {
            res = num1 + num2;
            num1 = num2;
            num2 = res;
        }
        return res;
    }
}
