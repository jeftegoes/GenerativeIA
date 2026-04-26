package com.example.clients.responses;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

import java.util.List;

@Data
public class FactCheckClientResponse {
    @JsonProperty("claims")
    private List<ClaimData> claims;

    @Data
    public static class ClaimData {
        private String text;
        private String claimant;
        private String claimDate;
        @JsonProperty("claimReview")
        private List<ClaimReviewData> claimReviews;
    }

    @Data
    public static class ClaimReviewData {
        private String url;
        private String title;
        private String textualRating;
        @JsonProperty("publisher")
        private PublisherData publisher;
    }

    @Data
    public static class PublisherData {
        private String name;
        private String site;
    }
}
