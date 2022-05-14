import os
import argparse
import time
import mlflow



def evaluate(a1,a2):
    return a1+a2
def main(p1,p2):
    ## log the matrix
    with mlflow.start_run():
        mlflow.log_param("param1",p1)
        mlflow.log_param("param2",p2)

        matric = evaluate(p1,p2)
        mlflow.log_metric("Some_metric", matric)
        os.makedirs("temp", exist_ok=True)
        with open("temp/sampe.txt","w") as f:
            f.write(time.asctime())
        mlflow.log_artifacts("temp")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--a1","-a1", type=int, default=2)
    args.add_argument("--a2","-a2", type=int, default=2)
    parsed_args= args.parse_args()
    main(parsed_args.a1, parsed_args.a2)
    

