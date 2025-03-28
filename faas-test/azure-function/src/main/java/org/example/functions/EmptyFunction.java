package org.example.functions;

import java.util.*;
import com.microsoft.azure.functions.annotation.*;
import com.microsoft.azure.functions.*;

/**
 * Azure Functions with HTTP Trigger.
 */
public class EmptyFunction {
    /**
     * This function listens at endpoint "/api/EmptyFunction". Two ways to invoke it using "curl" command in bash:
     * 1. curl -d "HTTP Body" {your host}/api/EmptyFunction
     * 2. curl {your host}/api/EmptyFunction?name=HTTP%20Query
     */
    @FunctionName("empty_function")
    public HttpResponseMessage run(
            @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.FUNCTION) HttpRequestMessage<Optional<String>> request,
            final ExecutionContext context) {
            return request.createResponseBuilder(HttpStatus.OK).body("").build();
    }
}
