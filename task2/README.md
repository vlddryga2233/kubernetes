# Kubernetes module

## Task 2
* Connect to the cluster
* Deploy fortune deployment
* Deploy fortune service
* Deploy ingress controller
* Create namespace

## Steps
1. Move `config` file to `.kube/` folder
2. Check connection to the cluster
   ```
   kubectl get nodes
   NAME       STATUS   ROLES                  AGE   VERSION
   kube-lab   Ready    control-plane,master   75m   v1.21.5+k3s2
   ```
4. Create namespace
   ```
   kubectl create namespace vlad
   kubectl config set-context --current --namespace=vlad
   ```
3. Deploy fortune
   ```
   kubectl apply -f fortune.yaml
   kubectl apply -f fortune-service.yaml
   kubectl apply -f ingress-with-cert-manager-cluster-issuer.yaml
   ```
4. Check result
   ```
   kubectl get all

   NAME                                      READY   STATUS    RESTARTS   AGE
   pod/fortune-deployment-7b9dd4956c-w9kjn   1/1     Running   0          57m
   pod/fortune-deployment-7b9dd4956c-j5clp   1/1     Running   0          57m
   pod/cm-acme-http-solver-j8tbd             1/1     Running   0          57m

   NAME                                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
   service/fortune-service             ClusterIP   10.43.188.210   <none>        80/TCP           57m 
   service/cm-acme-http-solver-cq7z2   NodePort    10.43.137.41    <none>        8089:31699/TCP   57m

   NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/fortune-deployment   2/2     2            2           57m
 
   NAME                                            DESIRED   CURRENT   READY   AGE
   replicaset.apps/fortune-deployment-7b9dd4956c   2         2         2       57m
   ```

   Output

   ```
   curl fortune-vlad.kubelab.spainip.es/cgi-bin/test.py


   StatusCode        : 200
   StatusDescription : OK
   Content           : Test message
                       Q:  What looks like a cat, flies like a bat, brays like a donkey, and
                       plays like a monkey?
                       A:  Nothing.
   ```