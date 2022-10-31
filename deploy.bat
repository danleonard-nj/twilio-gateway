docker build -t azureks.azurecr.io/gateway/twilio-gateway:1906 .
docker push azureks.azurecr.io/gateway/twilio-gateway:1906
kubectl rollout restart deployment twilio-gateway