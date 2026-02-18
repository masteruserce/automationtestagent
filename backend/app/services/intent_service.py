from agent.behavior_explorer import BehaviorExplorer
from agent.intent_model_builder import IntentModelBuilder


class IntentService:

    def build_intent_model(self, swagger_json: dict, base_url: str, endpoints: list[dict] = None):
        print(f"server_url in intent service: {base_url}")
        print(f"endpoints in intent service: {endpoints}")
        explorer = BehaviorExplorer(
            base_url=base_url,
            endpoints=endpoints,
        )
        
        behavior_report = explorer.explore_all()

        builder = IntentModelBuilder(behavior_report)
        intent_model = builder.build()

        return intent_model
