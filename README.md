# pslearn
This Python package provides a tool for hyperparameter tuning and feature selection in machine learning models using Particle Swarm Optimization (PSO) techniques. The package includes a vanilla PSO for feature selection, a vanilla PSO for hyperparameter tuning, and two different PSO variants for machine learning hyperparameter tuning.

Features
Vanilla PSO for Feature Selection: This feature uses the standard PSO algorithm to select the most optimal features for a given machine learning model. The algorithm works by searching the feature space and identifying a subset of features that maximizes the performance of the model.
Vanilla PSO for Hyperparameter Tuning: This feature uses the standard PSO algorithm to tune the hyperparameters of a given machine learning model. The algorithm works by searching the hyperparameter space and identifying a set of parameters that maximize the performance of the model.
PSO Variants for Hyperparameter Tuning: This package includes two different PSO variants for hyperparameter tuning. These variants offer different search strategies and can provide better results depending on the specific characteristics of the problem.
Cross-Validation: The package uses cross-validation in the hyperparameter tuning process to avoid overfitting and to ensure that the tuned parameters generalize well to unseen data.
Example Usage
The following is a basic example of how to use this package:


Installation
------------

Install it using pip:

    pip install pslearn

Hyperparameters Tuning
----------------

https://github.com/yuenshingyan/pslearn/blob/main/hyperparameters_tuning_example.py


Feature Selection
-------------------------

https://github.com/yuenshingyan/pslearn/blob/main/feature_selection_example.py
