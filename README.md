# kedro_astrophysics

This repository was created following the [Pyladies Amsterdam workshop by Merel Theisen](https://github.com/pyladiesams/kedro-prod-ready-ds-pipelines-aug2025).

It demonstrates how to use [Kedro](https://kedro.org/) to build a parameter estimation pipeline for astrophysical signals.  
The project currently contains two pipelines:
- **`astrophysics_priors`** – generates prior samples for the sampler.  
- **`astrophysics_sampler`** – defines the likelihood and runs the sampler.  

Results are stored in:
```data/08_reporting/```

# Step 0: Install the requirements

Clone this repository 
```git clone git@github.com:Alexandra-Wernersson/kedro_astrophysics.git```

Install requirements (Python >= 3.8):
```pip install -r requirements.txt```

# Step 1: Configure

Parameters and catalog entries can be found in:

```conf/base/catalog.yml``` 
```conf/base/parameters_astrophysics_sampler.yml```. 

# Step 2: Generate the prior samples

Run
``` kedro run --pipeline astrophysics_priors```

This will generate prior samples and save them to:

```data/02_intermediate/results.pkl```

# Step 3: Run the sampler
Run
``` kedro run --pipeline astrophysics_sampler```
This will execute the sampler and save results to:
```data/08_reporting/```.

# Step 4: Explore the results
Open the notebook:
```jupyter notebook notebooks/results_demo.ipynb```

Alternatively open the notebook
```jupyter notebook notebooks/kedro_astrophysics_pipeline.ipynb```
To see the full run-through of the pipeline.

# Roadmap
This project currently uses a simple signal model.
Next steps will extend it to a full gravitational wave signal example. 🚀
