Feature: Steps Endpoints
            Scenario: GET /api/v1/api/workflows/workflows/{job_id}/steps/{step}
            When I send a "GET" request to "/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
            Then I should receive a valid response