Feature: Events Endpoints
            Scenario: GET /api/v1/api/workflows/workflows/events/{job_id}
            When I send a "GET" request to "/api/v1/api/workflows/workflows/events/{job_id}"
            Then I should receive a valid response