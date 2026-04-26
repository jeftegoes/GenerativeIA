package com.example.clients;

import com.example.clients.responses.FactCheckClientResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;

@Component
public class FactCheckClient {
    private final RestClient restClient;

    @Value("${google.factcheck.api.key}")
    private String apiKey;

    private static final String BASE_URL = "https://factchecktools.googleapis.com/v1alpha1";

    public FactCheckClient(RestClient restClient) {
        this.restClient = restClient;
    }

    public FactCheckClientResponse searchClaims(String query) {
        String url = UriComponentsBuilder.fromUri(URI.create(BASE_URL + "/claims:search"))
                .queryParam("query", query)
                .queryParam("languageCode", "pt-BR")
                .queryParam("key", apiKey)
                .build()
                .toUriString();

        return restClient.get()
                .uri(url)
                .retrieve()
                .body(FactCheckClientResponse.class);
    }
}
