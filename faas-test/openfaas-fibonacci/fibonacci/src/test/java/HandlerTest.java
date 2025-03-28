import com.openfaas.model.IResponse;
import com.openfaas.model.Request;
import org.junit.Test;

import static org.junit.Assert.*;

import com.faas.function.Handler;
import com.openfaas.model.IHandler;

import java.util.HashMap;

public class HandlerTest {


    @Test
    public void testCalculateFibonacci() {
        IHandler handler = new Handler();
        assertTrue("Expected handler not to be null", handler != null);

        IResponse response = handler.Handle(new Request("", new HashMap<>()));
        assertTrue("HTTP status code should be 200", response.getStatusCode() == 200);
        System.out.println(response.getBody());
        assertTrue("Image processing failed: " + response.getBody(), response.getBody().equals(Integer.toString(514229)));
    }
}
