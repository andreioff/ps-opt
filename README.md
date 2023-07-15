# pslearn
Particle Swarm Optimization For Machine Learning

Installation
------------

To use evolearn, first install it using pip:

    pip install pslearn

Genetic Optimization CV
----------------

import pandas as pd
from sklearn.datasets import make_classification
from pslearn.hyperparameters_tuning import ParticleSwarmSearchCV
from pslearn.search_space_characteristics import Categorical, Real, Integer
from sklearn.linear_model import LogisticRegression


X, y = make_classification()
X = pd.DataFrame(X)
y = pd.Series(y)

search_space = {
    "penalty": Categorical("l1", "l2", "elasticnet", None),
    "max_iter": Integer(10, 20, "exponential"),
    "tol": Real(.0001, .1, "uniform"),
    "solver": Categorical('lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga')
}

psocv = ParticleSwarmSearchCV(
    search_space=search_space,
    n_particles=30,
    estimator=LogisticRegression,
    cv=5,
    scoring="accuracy",
    max_iter=10,
    n_jobs=1,
    verbosity=0
)

psocv.fit(X, y)

print(f"Best Score: {psocv.best_score_}")
print(f"Best Parameters: {psocv.best_params_}")
print(f"Best Probabilities: {psocv.best_proba_}")


# Best Score: 0.85
# Best Parameters: {'solver': 'saga', 'penalty': 'l2', 'max_iter': 40, 'tol': 0.9745153143592415}
# Best Probabilities: {
#     '__l1_penalty__': 0.0642647183158804,
#     '__l2_penalty__': 0.7783339727146499, 
#     '__elasticnet_penalty__': 0.08866833136772977,
#     '__None_penalty__': 0.0687329776017401, 
#     'max_iter': 40.0, 'tol': 0.9745153143592415,
#     '__lbfgs_solver__': 0.11322358364859948,
#     '__liblinear_solver__': 0.13393371361649387,
#     '__newton-cg_solver__': 0.1168855854059326,
#     '__sag_solver__': 0.16334363891584566, 
#     '__saga_solver__': 0.4726134784131283
# }


Genetic Feature Selection
-------------------------

import pandas as pd
from sklearn.datasets import make_classification
from pslearn.feature_selection import ParticleSwarmFeatureSelectionCV
from pslearn.search_space_characteristics import Categorical, Real, Integer
from sklearn.linear_model import LogisticRegression


X, y = make_classification()
X = pd.DataFrame(X)
y = pd.Series(y)

search_space = {
    "penalty": Categorical("l1", "l2", "elasticnet", None),
    "max_iter": Integer(10, 20, "exponential"),
    "tol": Real(.0001, .1, "uniform"),
    "solver": Categorical('lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga')
}

psocv = ParticleSwarmFeatureSelectionCV(
    n_particles=30,
    estimator=LogisticRegression,
    cv=5,
    scoring="accuracy",
    max_iter=10,
    n_jobs=-1,
    verbosity=0
)

psocv.fit(X, y)

print(f"Best Score: {psocv.best_score_}")
print(f"Best Features: {psocv.best_features_}")
print(f"Best Probabilities: {psocv.best_proba_}")

Best Score: 0.9
Best Features: (6, 10, 14, 17)
Best Probabilities: [0.782711593275808, 0.8084822421165769, 0.8219410644289048, 0.7502198513093719]

