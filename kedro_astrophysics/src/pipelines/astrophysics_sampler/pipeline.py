"""
This is a boilerplate pipeline 'astrophysics_sampler'
generated using Kedro 1.0.0
"""
from kedro.pipeline import Node, Pipeline
from .nodes import run_sampler, load_observation_time, load_priors

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
                func=load_observation_time,
                inputs=["observation_time"],
                outputs=["time", "observation"],
                name="load_observation_time_node",
            ),
         Node(
                func=load_priors,
                inputs="priors_raw",
                outputs="priors",
                name="load_priors_node",
            ),
        Node(
                func=run_sampler,
                inputs=["time", "observation", "priors", "likelihood_params"],
                outputs="results",
                name="run_sampler_node",
            ),
    ])
