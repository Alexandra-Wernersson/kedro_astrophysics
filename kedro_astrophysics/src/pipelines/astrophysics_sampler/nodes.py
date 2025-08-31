"""
This is a boilerplate pipeline 'astrophysics_sampler'
generated using Kedro 1.0.0
"""
import logging
import bilby
import pandas as pd
import numpy as np

def load_observation_time(df: pd.DataFrame):
    return df["time"].to_numpy(), df["observation"].to_numpy()

def load_priors(priors_dict: dict) -> bilby.core.prior.PriorDict:
    return bilby.core.prior.PriorDict(dictionary=priors_dict)

def run_sampler(time, observation, priors, likelihood_params):
    def signal_model(time, m, c):
        return time * m + c
    likelihood = bilby.likelihood.GaussianLikelihood(
        time, observation, signal_model, sigma=likelihood_params["sigma"]
    )
    result = bilby.run_sampler(
        likelihood=likelihood,
        priors=priors,
        sampler=likelihood_params["sampler"],
        nlive=likelihood_params["nlive"],
        sample=likelihood_params["sample"],
        outdir=likelihood_params["outdir"],
        label=likelihood_params["label"],
    )
    return result
