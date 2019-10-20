# devopsassignment

## Deploy the microservices on k8s cluster

### Clone the project 
kubectl create -f ms1/ms1-deployment.yaml
kubectl create -f ms2/ms2-deployment.yaml

## API Description :

curl -X POST \
  http://10.0.0.27:31401/api/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: c4307df4-9618-4548-bfca-eff371ce8805' \
  -H 'cache-control: no-cache' \
  -d '{"message": "Hello World"}'

