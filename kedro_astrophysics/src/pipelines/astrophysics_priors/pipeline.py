from kedro.pipeline import Node, Pipeline

from .nodes import make_priors


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            Node(
                func=make_priors,
                inputs="params:num_samples",
                outputs="priors_raw",
                name="make_priors_node",
            ),
        ]
    )
