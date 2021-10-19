# Kubernetes module

## Task 1
* Create minikube cluster
* Create Dockerfile with fortune app
* Deploy image to Docker Hub
* Crate deployment and service in K8s

## Structure
* [default](default) - nginx configure file with fcgiwrap module
* [Dockerfile](Dockerfile) - file for creation docker image
* [fortune-service.yaml](fortune-service.yaml) - service for k8s
* [fortune.yaml](fortune.yaml) - deployment for k8s
* [test.py](test.py) - python appllication

## Requierments
* Docker - [link](https://docs.docker.com/engine/install/)
* kubectl - [link](https://kubernetes.io/ru/docs/tasks/tools/install-kubectl/)
* minikube - [link](https://kubernetes.io/ru/docs/tasks/tools/install-minikube/) 
* VirtualBox - [link](https://www.virtualbox.org/wiki/Downloads)
* Docker Hub accaunt - [link](https://hub.docker.com/)



## Steps

1. Launch minikube cluster
     ```
     minukube start
     ```
2. Create docker image and push to Docker hub
    ```
    docker build -t <your_accaount>/<image_name>:<tag> .

    docker push <your_accaount>/<image_name>:<tag>
    ```
3. Create deployment and service
    ```
    kubectl create deployment -f fortune.yaml
    kubectl create service -f fortune-service.yaml
    ```
    The output
    
    ```
    kubectl get deployment
    NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
    fortune-deployment   2/2     2            2           21m
    ```
    ```
    kubectl get pods
    NAME                                  READY   STATUS    RESTARTS   AGE
    fortune-deployment-7b9dd4956c-bmkwt   1/1     Running   0          24m
    fortune-deployment-7b9dd4956c-tpfl4   1/1     Running   0          24m
    ```
    ```
    kubectl get service
    NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
    fortune-service   ClusterIP   10.102.253.81   <none>        80/TCP    23m
    kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP   22h
    ```
4. Testing result
    > We use minikube on local machine, so we need to do some steps

    ```
     minikube service fortune-service
    |-----------|-----------------|-------------|--------------|
    | NAMESPACE |      NAME       | TARGET PORT |     URL      |
    |-----------|-----------------|-------------|--------------|
    | default   | fortune-service |             | No node port |
    |-----------|-----------------|-------------|--------------|
    * service default/fortune-service has no node port
    * Starting tunnel for service fortune-service.
    |-----------|-----------------|-------------|------------------------|
    | NAMESPACE |      NAME       | TARGET PORT |          URL           |
    |-----------|-----------------|-------------|------------------------|
    | default   | fortune-service |             | http://127.0.0.1:57700 |
    |-----------|-----------------|-------------|------------------------|
    ```

    And the result in browser

    ```
    curl http://127.0.0.1:57700/cgi-bin/test.py


    StatusCode        : 200
    StatusDescription : OK
    Content           : Test message
                        Good day for a change of scene.  Repaper the bedroom wall.    
    ```