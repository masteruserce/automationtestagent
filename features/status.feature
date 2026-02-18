Feature: Status Endpoints
            Scenario: GET /api/v1/api/workflows/workflows/{job_id}/status
            When I send a "GET" request to "/api/v1/api/workflows/workflows/{job_id}/status"
            Then I should receive a valid response