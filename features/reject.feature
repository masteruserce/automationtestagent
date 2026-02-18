Feature: Reject Endpoints
            Scenario: POST /api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject
            When I send a "POST" request to "/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
            Then I should receive a valid response