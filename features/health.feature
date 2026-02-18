Feature: Health Endpoints
            Scenario: GET /api/v1/api/health/health
            When I send a "GET" request to "/api/v1/api/health/health"
            Then I should receive a valid response