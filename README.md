# devopsassignment

## Prerequisite : K8s secret regcred should be present in the same namespace

## Deploy the microservices on k8s cluster

### Clone the project 
kubectl create -f ms1/ms1-deployment.yaml

kubectl create -f ms2/ms2-deployment.yaml

## API Description :

curl -X POST \
  http://<< K8S API SERVER IP >>:31401/api/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: c4307df4-9618-4548-bfca-eff371ce8805' \
  -H 'cache-control: no-cache' \
  -d '{"message": "Hello World"}'

where << K8S API SERVER IP >> : Replace this with the API server IP 
