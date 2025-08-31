"""Project pipelines."""
from __future__ import annotations

from kedro.pipeline import Pipeline
from pipelines import astrophysics_data, astrophysics_sampler


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    data_pipeline = astrophysics_data.create_pipeline()
    sampler_pipeline = astrophysics_sampler.create_pipeline()

    return {
        "__default__": data_pipeline + sampler_pipeline,
        "astrophysics_data": data_pipeline,
        "astrophysics_sampler": sampler_pipeline,
    }
