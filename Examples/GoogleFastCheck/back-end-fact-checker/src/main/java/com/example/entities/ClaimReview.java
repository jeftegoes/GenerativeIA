package com.example.entities;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "claim_reviews")
public class ClaimReview {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String url;

    @Column(columnDefinition = "TEXT")
    private String title;

    private String textualRating;

    @ManyToOne
    @JoinColumn(name = "claim_id")
    private Claim claim;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "publisher_id")
    private Publisher publisher;
}
