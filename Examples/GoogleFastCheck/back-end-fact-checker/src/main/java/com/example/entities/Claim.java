package com.example.entities;

import jakarta.persistence.*;
import lombok.Data;

import java.time.Instant;
import java.util.List;

@Data
@Entity
@Table(name = "claims")
public class Claim {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(columnDefinition = "TEXT")
    private String text;

    private String claimant;

    private Instant claimDate;

    @OneToMany(mappedBy = "claim", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<ClaimReview> claimReviews;
}
