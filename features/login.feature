Feature: Login Endpoints
            Scenario: POST /api/v1/auth/auth/login
            When I send a "POST" request to "/api/v1/auth/auth/login"
            Then I should receive a valid response