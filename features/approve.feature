Feature: Approve Endpoints
            Scenario: POST /api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve
            When I send a "POST" request to "/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
            Then I should receive a valid response