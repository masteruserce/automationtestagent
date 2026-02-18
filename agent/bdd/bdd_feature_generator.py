from collections import defaultdict


class BDDFeatureGenerator:

    def __init__(self, swagger_spec: dict, base_url: str):
        self.swagger = swagger_spec
        self.base_url = base_url.rstrip("/")

    def generate(self) -> dict:
        """
        Returns:
        {
            "feature_name": "string",
            "content": "gherkin text"
        }
        """

        paths = self.swagger.get("paths", {})
        grouped = defaultdict(list)

        # ----------------------------
        # Group by primary resource
        # ----------------------------
        for path, methods in paths.items():

            segments = [s for s in path.split("/") if s and "{" not in s]
            if not segments:
                continue

            resource = segments[-1]

            for method in methods.keys():
                grouped[resource].append({
                    "path": path,
                    "method": method.upper()
                })

        features = {}

        for resource, endpoints in grouped.items():
            feature_text = self._build_feature(resource, endpoints)
            features[resource] = feature_text

        return features

    def _build_feature(self, resource, endpoints):

        feature = []
        feature.append(f"@{resource} @api")
        feature.append(
            f"Feature: Validate {resource.title()} API - ({self.base_url}/{resource})"
        )
        feature.append("")
        feature.append("  Background:")
        feature.append("    Given The endpoint URI is already configured")
        feature.append("")

        methods = {e["method"] for e in endpoints}

        # ------------------------
        # Positive GET
        # ------------------------
        if "GET" in methods:
            feature.append("  @positive")
            feature.append(f"  Scenario: Get valid {resource}")
            feature.append(f'    Then I set the base path "/{resource}" to URI')
            feature.append('    When I GET the valid endpoint at "1"')
            feature.append('    Then I should have the status code "200" displayed')
            feature.append('    And content type should be in "JSON" format')
            feature.append("")

            # Invalid case
            feature.append("  @invalid")
            feature.append(f"  Scenario: Get invalid {resource}")
            feature.append(f'    Then I set the base path "/{resource}" to URI')
            feature.append('    When I GET the valid endpoint at "999999"')
            feature.append('    Then I should have the status code "404" displayed')
            feature.append("")

        # ------------------------
        # POST
        # ------------------------
        if "POST" in methods:
            feature.append("  @post")
            feature.append(f"  Scenario: Create {resource}")
            feature.append(f'    Then I set the base path "/{resource}" to URI')
            feature.append('    And I set the request header "Content-Type" as "application/json"')
            feature.append('    Then I POST data in json format')
            feature.append('    """')
            feature.append('    {')
            feature.append('      "sample": "value"')
            feature.append('    }')
            feature.append('    """')
            feature.append('    Then I should have the status code "201" displayed')
            feature.append("")

        # ------------------------
        # PUT
        # ------------------------
        if "PUT" in methods or "PATCH" in methods:
            feature.append("  @update")
            feature.append(f"  Scenario: Update {resource}")
            feature.append(f'    Then I set the base path "/{resource}" to URI')
            feature.append('    And I PUT the resource "1" with following data')
            feature.append('    """')
            feature.append('    {')
            feature.append('      "sample": "updated"')
            feature.append('    }')
            feature.append('    """')
            feature.append('    Then I should have the status code "200" displayed')
            feature.append("")

        # ------------------------
        # DELETE
        # ------------------------
        if "DELETE" in methods:
            feature.append("  @delete")
            feature.append(f"  Scenario: Delete {resource}")
            feature.append(f'    Then I set the base path "/{resource}" to URI')
            feature.append('    And I DELETE the valid resource "1"')
            feature.append('    Then I should have the status code "200" displayed')
            feature.append("")

        return "\n".join(feature)
