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

# Best Score: 0.9
# Best Features: (6, 10, 14, 17)
# Best Probabilities: [0.782711593275808, 0.8084822421165769, 0.8219410644289048, 0.7502198513093719]
