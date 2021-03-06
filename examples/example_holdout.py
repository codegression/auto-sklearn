"""
=======
Holdout
=======

In *auto-sklearn* it is possible to use different resampling strategies
by specifying the arguments ``resampling_strategy`` and
``resampling_strategy_arguments``. The following example shows how to use the
holdout method as well as set the train-test split ratio when instantiating
``AutoSklearnClassifier``.
"""

import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

import autosklearn.classification


############################################################################
# Data Loading
# ============

X, y = sklearn.datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, random_state=1)

############################################################################
# Building the classifier
# =======================

automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120,
    per_run_time_limit=30,
    tmp_folder='/tmp/autosklearn_holdout_example_tmp',
    output_folder='/tmp/autosklearn_holdout_example_out',
    disable_evaluator_output=False,
    # 'holdout' with 'train_size'=0.67 is the default argument setting
    # for AutoSklearnClassifier. It is explicitly specified in this example
    # for demonstrational purpose.
    resampling_strategy='holdout',
    resampling_strategy_arguments={'train_size': 0.67}
)
automl.fit(X_train, y_train, dataset_name='breast_cancer')

############################################################################
# Print the final ensemble constructed by auto-sklearn
# ====================================================

print(automl.show_models())

############################################################################
# Print statistics about the auto-sklearn run
# ===========================================

# Print statistics about the auto-sklearn run such as number of
# iterations, number of models failed with a time out.
print(automl.sprint_statistics())

############################################################################
# Get the Score of the final ensemble
# ===================================

predictions = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, predictions))
