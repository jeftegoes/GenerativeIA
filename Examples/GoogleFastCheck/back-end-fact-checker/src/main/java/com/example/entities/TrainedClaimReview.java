package com.example.entities;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "trained_claim_reviews")
public class TrainedClaimReview {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @JoinColumn(name = "error_rate")
    private int errorRate;
    private String text;
    private String publisher;
    private String rating;
    private String checksum;
}
