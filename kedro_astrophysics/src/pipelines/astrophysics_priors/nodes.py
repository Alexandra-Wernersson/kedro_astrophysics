import logging
import bilby
import pandas as pd
import numpy as np

def make_priors(num_samples: int):
    """
    Function to generate prior samples for bilby's sampler.

    Parameters:
    -----------
    num_samples: int
      Number of samples to be generated.

    Returns:
    --------
    json:
      Dictionary containing the prior samples.
    """

    priors = bilby.core.prior.PriorDict(dict(
    m=bilby.core.prior.TruncatedNormal(mu=0, sigma=1, minimum=0, maximum=3, name="m"),
    c=bilby.core.prior.Uniform(-5, 5, name="c"),
    ))

    return priors

