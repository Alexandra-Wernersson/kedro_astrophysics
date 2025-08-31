"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from kedro_workshop.pipelines import astrophysics_data, astrophysics_sampler

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    return {
        "__default__": astrophysics_data.create_pipeline(),
        "astrophysics_data": astrophysics_data.create_pipeline(),
        "astrophysics_sampler": astrophysics_sampler.create_pipeline(),
    }
