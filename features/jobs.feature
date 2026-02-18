Feature: Jobs Endpoints
            Scenario: GET /api/v1/api/workflows/workflows/admin/jobs/{job_id}
            When I send a "GET" request to "/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
            Then I should receive a valid response
            
            Scenario: GET /api/v1/api/workflows/workflows/jobs
            When I send a "GET" request to "/api/v1/api/workflows/workflows/jobs"
            Then I should receive a valid response