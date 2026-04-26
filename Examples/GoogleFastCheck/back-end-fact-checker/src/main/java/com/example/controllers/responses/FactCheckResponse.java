package com.example.controllers.responses;

import lombok.Data;

@Data
public class FactCheckResponse {
    private int errorRate;
    private String text;
    private String publisher;
    private String rating;
}
