from fastapi import APIRouter
from agent.bdd.bdd_feature_generator import BDDFeatureGenerator
from backend.state import state

router = APIRouter(prefix="/bdd", tags=["BDD"])

@router.post("/generate")
def generate_bdd(base_url: str):

    generator = BDDFeatureGenerator(
        state.swagger_spec,
        base_url
    )

    features = generator.generate()

    return features
