import mlflow

print('inicio2')

mlflow.start_run(experiment_id=0)

mlflow.log_param('b', 99)
mlflow.log_metric('a', 99)

mlflow.end_run()



print('fim')
