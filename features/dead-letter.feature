Feature: Dead-letter Endpoints
            Scenario: GET /api/v1/api/workflows/workflows/admin/dead-letter
            When I send a "GET" request to "/api/v1/api/workflows/workflows/admin/dead-letter"
            Then I should receive a valid response