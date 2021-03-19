# Compredict_challenge
Compredict challenge work



# Assignement 

# Objective:


## Task 1

Submit the kubernetes yaml files that do the following:
Deploy an empty Django application in two or more instances using kubernetes. 
The application is composed of the following services: 

Eventually, you should specify the order on how to apply the manefists with command `kubectl apply -f <manifest.yaml>`:


## Services

- Django (Deployment):
	- image: alang/django but you need to take care of gunicorn or write your own dockerfile.
	- 2 replicas
	- restart policy on failure max 3 times
	- Create ingress rule to expose the application the application.
	- Rollout update policy should be handled as 2 replicas should be up all time. (configure MaxSurge and availability in manefist)

- redis (Deployment):
	- image: redis:3.2
	- no public ports
	- on backend network
	- 1 replica
	- restart policy on failure max 3 times

- db (StatefulSet):
	- image: postgres:12.3
	- no public ports
	- on backend network
	- 1 replica
	- set username, database and port as ConfigMaps where as the password as Secret (use dataString).
	- Use Dynamic Volume Provisioning to create a volume for postgres and mount it to /var/lib/postgresql/data 


P.S: You can use Docker Desktop or the [play-with-kubernetes](https://labs.play-with-k8s.com/) to have multiple instances to test your script or use free AWS instances.


## Task 2

Write a python script that uses [kubernetes-python](https://github.com/kubernetes-client/python) SDK or any [other sdks](https://kubernetes.io/docs/reference/using-api/client-libraries/) 
to create a new Pod programatically or scale one of the services in Task 1.


## Submission

Please submit both task 1 and task 2 as zip file by email. If the zip file is too big, then put it on a cloud storage and provide us with the link. Otherwise, you can push the solution to github and pass over the link.
