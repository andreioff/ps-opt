.. toctree::
   :maxdepth: 10
   :caption: Contents:

*****************
Feature Selection
*****************

GeneticFeatureSelectionCV
=========================
* ``n_gen``: int

  - Maximum number of generation (or loop) GenesSearchCV will run.
  
* ``initialization_fn``

  - Class object to generate solution candidates.
  
* ``fitness_fn``

  - Class object to evalute the fitness of solution candidates.
  
* ``selection_fn``

  - Class object to evalute the fitness of solution candidates.

  - Can either be:
     - optimization.selection.RankSelection,
          - optimization.selection.RouletteWheelSelection,
          - optimization.selection.SteadyStateSelection,
          - optimization.selection.TournamentSelection,
          - optimization.selection.StochasticUniversalSampling,
          - optimization.selection.BoltzmannSelection

          
  
* ``mating_fn`` 

  - Class object to pair the solution candidates for reproduction.
  
* ``reproduction_fn``

  - Class object to reproduce child population.

  - Can either be
       - optimization.reproduction.KPointCrossover,
       - optimization.reproduction.LinearCombinationCrossover,
       - optimization.reproduction.FitnessProportionateAverage

       
  
* ``mutation_fn``

  - Class object to mutate the child population.

  - Can either be
       - optimization.mutation.Boundary,
       - optimization.mutation.Shrink
       
       
  
* ``adaptive_population``=None

  - Class object to adaptively change the mating rate of the mating_fn.
  
* ``elitism``=None

  - Class object to perform elites selection, ace comparison and elites' traits induction.
  
* ``adaptive_mutation``=None

  - Class object to adaptively change the mutation probaility of the mutation_fn.

Initialization
--------------
Genes
-----
* ``search_space``: dict 

  - Defines the search range of the algorithm. Where keys are parameter names (strings) and values are int, float or str. Represents search spaceover parameters of the provided  estimator.
  
* ``pop_size``: int 

  - Size of the initial population.


Evaluation
----------
FitnessFunction
---------------
* ``estimator``: BaseEstimator

  - A object of that type is instantiated for each search point. This object is assumed to implement the scikit-learn estimator api. Either estimator needs to provide a   ``score`` function, or ``scoring`` must be passed.
  
* ``cv``: int

  - cross-validation generator or an iterable, optional Determines the cross-validation splitting strategy. Possible inputs for cv are:
          - None, to use the default 3-fold cross validation,
          - integer, to specify the number of folds in a `(Stratified)KFold`,
          - An object to be used as a cross-validation generator.
          - An iterable yielding train, test splits.
          
For integer/None inputs, if the estimator is a classifier and ``y`` is either binary or multiclass, :class:`StratifiedKFold` is used. In all other cases, :class:`KFold` is used.
  
* ``scoring``: str

  - callable or None, default=None A string (see model evaluation documentation) or a scorer callable object / function with signature ``scorer(estimator, X, y)``. If ``None``, the ``score`` method of the estimator is used.


Selection
---------
RankSelection
-------------
* ``pct_survivors``: int, float

  - Argument that controls the number of survivors.


|
RouletteWheelSelection
----------------------
* ``pct_survivors``: int, float

  - Argument that controls the number of survivors.


|
SteadyStateSelection
--------------------
* ``elimination_ratio``: float [default=.3]

  - Determine how many candidates are eliminated.


|
TournamentSelection
-------------------
* ``k``: int [default=2] 

  - Argument that controls the number of participants in each tourament.
  
* ``preserve_remainders``: bool [default=True]

  - If True, the remaining individuals not selected for tournament will survive the selection process.


|
StochasticUniversalSampling
---------------------------
* ``pct_survivors``: int, float

  - Argument that controls the number of survivors.


|
BoltzmannSelection
------------------
* ``pct_survivors``: float

  - Argument that controls the number of survivors.
  
* ``T0``: int, float

  - Initial Temperature to calculate Boltzmann probability. A number between [5, 100].
  
* ``a``: int, float

  - Alpha, a constant between [0, 1].


Mating
------
MatingFunction
--------------
* ``cr_proba``: int, float [default=1]

  - Percentage of survived population. Determines how many couples are paired during mating.
  
* ``increst_prevention``: bool [default=True]

  - If True, solution candidates sharing the same parents will be paired together.
  
|
Reproduction
------------
KPointCrossover
---------------
* ``k``: int

  - Number of times of the chromosomes being splitted.
  
* ``c_pt``: int, str [default='random']

  - If int, c_pt will be the position index of the splitting points. If str, the splitting point location where be randomly determined. If 'random', the splitting point will be randomly picked.


|
Mutation
--------
BitStringMutation
-----------------
* ``epsilon``: float [default=.15]

  - Mutation rate that determines if genes will mutate or not.


|
ExchangeMutation
----------------
* ``epsilon``: float [default=.15]

  - Mutation rate that determines if genes will mutate or not.
  

|
ShiftMutation
-------------
* ``epsilon``: float [default=.15]

  - Mutation rate that determines if genes will mutate or not.


|
Environment
-----------
AdaptiveReproduction
--------------------
* ``pop_cap``: int [default=None]

  - Maximum population size.


|
AdaptiveMutation
----------------
* ``a``: int, float [default=.2]

  - Alpha, a constant to adjust the self-adaptive mutation rate.


|
Elitism
-------
* ``pct``: int, float [default=.05]

  - Percentage of population being selected as elites.

