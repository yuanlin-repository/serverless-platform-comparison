package com.faas.function;

import com.openfaas.model.IResponse;
import com.openfaas.model.IRequest;
import com.openfaas.model.Response;

public class Handler extends com.openfaas.model.AbstractHandler {

    public IResponse Handle(IRequest req) {
        Response res = new Response();
        int fibonacciNum = calculateFibonacci(30);
        res.setBody(Integer.toString(fibonacciNum));
        res.setStatusCode(200);
        return res;
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
