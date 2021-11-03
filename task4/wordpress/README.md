# Kubernetes module

## Task 4

* Create helm chart

## Structure
```
wordpress/
├── .helmignore   # Contains patterns to ignore when packaging Helm charts.
├── Chart.yaml    # Information about your chart
├── values.yaml   # The default values for your templates
├── charts/       # Charts that this chart depends on
└── templates/    # The template files
    └── tests/    # The test files
```

## Requirements
1. Kubernetes cluster
2. Installed helm
3. kubectl installed

## Steps

1. Clone the repo
 ```
 git clone https://github.com/vlddryga2233/kubernetes.git
 ```
2. Move to the chart folder
 ```
 cd ./kubernetes/task4/wordpress
 ```
3. Edit deployment in `values.yaml` file

4. Validate template
 ```
 helm template . --debug
 ```
 > The output must be our templates in yaml format

5. Install chart
 ```
 helm install . --generate-name
 ```
6. Check environment
 ```
 kubectl get all -n <your namespace>

 kubectl get all -n vlad
 NAME                                               READY   STATUS    RESTARTS   AGE
 pod/chart-1635942159-demo-mysql-58bdd4f5dd-rps9j   1/1     Running   0          2m42s
 pod/wordpress-9d48b5d6c-gv2z6                      1/1     Running   0          2m42s

 NAME                                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
 service/chart-1635942159-demo-mysql   ClusterIP   10.43.192.1    <none>        3306/TCP       2m42s
  service/chart-1635942159-wordpress    NodePort    10.43.51.105   <none>        80:30243/TCP   2m42s

 NAME                                          READY   UP-TO-DATE   AVAILABLE   AGE
 deployment.apps/chart-1635942159-demo-mysql   1/1     1            1           2m42s
 deployment.apps/wordpress                     1/1     1            1           2m42s

 NAME                                                     DESIRED   CURRENT   READY   AGE
 replicaset.apps/chart-1635942159-demo-mysql-58bdd4f5dd   1         1         1       2m42s
 replicaset.apps/wordpress-9d48b5d6c                      1         1         1       2m42s
 ```
7. Check application
 ```
 curl https://wordpress-vlad.kubelab.spainip.es/

 StatusCode        : 200
 StatusDescription : OK
 ```

