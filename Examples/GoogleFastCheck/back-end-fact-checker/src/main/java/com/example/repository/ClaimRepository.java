package com.example.repository;

import com.example.entities.Claim;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ClaimRepository extends JpaRepository<Claim, Long> {
    List<Claim> findByText(String text);
    List<Claim> findByClaimant(String claimant);
}
