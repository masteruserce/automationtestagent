Feature: Reset Endpoints
            Scenario: POST /api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset
            When I send a "POST" request to "/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
            Then I should receive a valid response