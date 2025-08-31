"""
This is a boilerplate pipeline 'astrophysics_sampler'
generated using Kedro 1.0.0
"""
import logging
import bilby
import pandas as pd
import numpy as np

def load_observation_time(df: pd.DataFrame):
    """
    Load the observation and time data from a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'time' and 'observation' columns.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Arrays of time and observation values.
    """
    return df["time"].to_numpy(), df["observation"].to_numpy()

def load_priors(priors_dict: dict) -> bilby.core.prior.PriorDict:
    """
    Load priors from a dictionary into a Bilby PriorDict.

    Parameters
    ----------
    priors_dict : dict
        Dictionary defining priors.

    Returns
    -------
    bilby.core.prior.PriorDict
        Bilby PriorDict object.
    """
    return bilby.core.prior.PriorDict(dictionary=priors_dict)

def run_sampler(time, observation, priors, likelihood_params):
    """
    Run Bilby's sampler.

    Parameters
    ----------
    time : np.ndarray
        Time array.
    observation : np.ndarray
        Observational data.
    priors : bilby.core.prior.PriorDict
        Priors for the parameters.
    likelihood_params : dict
        Dictionary containing sampler settings (e.g. sigma, sampler type, nlive).

    Returns
    -------
    bilby.result.Result
        Bilby Result object containing the posterior samples and metadata.
    """
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
