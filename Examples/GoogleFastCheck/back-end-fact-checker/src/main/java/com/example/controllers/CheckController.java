package com.example.controllers;

import com.example.clients.FactCheckClient;
import com.example.controllers.responses.FactCheckResponse;
import com.example.entities.Claim;
import com.example.entities.ClaimReview;
import com.example.clients.responses.FactCheckClientResponse;
import com.example.entities.Publisher;
import com.example.repository.ClaimRepository;
import org.springframework.web.bind.annotation.*;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class CheckController {

    private final FactCheckClient factCheckClient;
    private final ClaimRepository claimRepository;

    public CheckController(FactCheckClient factCheckClient, ClaimRepository claimRepository) {
        this.factCheckClient = factCheckClient;
        this.claimRepository = claimRepository;
    }

    @GetMapping("/fact-checks")
    public FactCheckResponse getFacts(@RequestParam String query) {
        FactCheckResponse factCheckResponse = this.checkOnFactCheck(query);

        if (factCheckResponse == null) {
            factCheckResponse = this.checkOnML();
        }

        return factCheckResponse;
    }

    private FactCheckResponse checkOnML() {
        return null;
    }

    private FactCheckResponse checkOnFactCheck(String query) {
        FactCheckClientResponse response = factCheckClient.searchClaims(query);

        if (response != null && response.getClaims() != null) {
            List<Claim> savedClaims = new ArrayList<>();

            for (FactCheckClientResponse.ClaimData claimData : response.getClaims()) {
                Claim claim = new Claim();
                claim.setText(claimData.getText());
                claim.setClaimant(claimData.getClaimant());

                if (claimData.getClaimDate() != null) {
                    try {
                        claim.setClaimDate(Instant.parse(claimData.getClaimDate()));
                    } catch (Exception e) {
                        claim.setClaimDate(Instant.now());
                    }
                } else {
                    claim.setClaimDate(Instant.now());
                }

                List<ClaimReview> reviews = new ArrayList<>();
                if (claimData.getClaimReviews() != null) {
                    for (FactCheckClientResponse.ClaimReviewData reviewData : claimData.getClaimReviews()) {
                        ClaimReview review = new ClaimReview();
                        review.setUrl(reviewData.getUrl());
                        review.setTitle(reviewData.getTitle());
                        review.setTextualRating(reviewData.getTextualRating());
                        review.setClaim(claim);

                        if (reviewData.getPublisher() != null) {
                            Publisher publisher = new Publisher();
                            publisher.setName(reviewData.getPublisher().getName());
                            publisher.setSite(reviewData.getPublisher().getSite());
                            review.setPublisher(publisher);
                        }

                        reviews.add(review);
                    }
                }
                claim.setClaimReviews(reviews);

                Claim savedClaim = claimRepository.save(claim);
                savedClaims.add(savedClaim);
            }

            FactCheckResponse factCheckResponse = new FactCheckResponse();
            if ((savedClaims.getFirst().getClaimReviews() != null) && (!savedClaims.getFirst().getClaimReviews().isEmpty())) {
                factCheckResponse.setText(savedClaims.getFirst().getText());
                factCheckResponse.setPublisher(savedClaims.getFirst().getClaimReviews().getFirst().getPublisher().getName());
                factCheckResponse.setRating(savedClaims.getFirst().getClaimReviews().getFirst().getTextualRating());
                factCheckResponse.setErrorRate(100);
            }

            return factCheckResponse;
        }

        return null;
    }
}