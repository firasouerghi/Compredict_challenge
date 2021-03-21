from kubernetes import client, config



class Container:
    """
    A class that represents a container object.

    ...

    Attributes
    ----------
    container_name : str
        name of the container
    
    container_image : str
        name of the docker image 

    Methods
    -------
    create_container():
        Creats a kubernetes container object and Returns a list containing the created container.
    """

    def __init__(self,container_name:str, container_image:str):
        """
        Constructs all the necessary attributes for the container object.

        Parameters
        ----------
            container_name : str
                name of the container
            container_image : str
                name of the docker image
        """

        self.container_name = container_name
        self.container_image= container_image
    
    def create_container(self):
        """
        Creats a kubernetes container object and Returns a list containing the created container.

        Parameters
        ----------
            None

        Returns
        -------
                container_list (list): A list containing the kubernetes container object.
        """
        container_list = [client.V1Container(
                        name=self.container_name, 
                        image=self.container_image,
                        )]
        return container_list



class Pod:
    """
    A class that represents a kubernetes pod object.

    ...

    Attributes
    ----------
    client : kubernetes APIClient
        insures the communication to the kubernetes api and the pod creation  
    pod_name: str
        name of the pod
    name_space: str
        the namespace to which the created pod belongs to
    metadata: kubernetes metadata object 
        defines the pod metadata
    container: Container
        A list containing the container obejct to be used by the pod 
    spec: kubenetes Spec objet:
        defines all the pod specifications  

    Methods
    -------
    create_pod():
        Creats and launches a kubernetes pod.
    delete_pod():
        Deletes the created pod
    """

    def __init__(self, pod_name:str, name_space:str, container_name, container_image:str):
        
        """
        Constructs all the necessary attributes for a pod object.

        Parameters
        ----------
        client : kubernetes APIClient
            insures the communication to the kubernetes api and the pod creation  
        pod_name: str
            name of the pod
        name_space: str
            the namespace to which the created pod belongs to
        metadata: kubernetes metadata object 
            defines the pod metadata
        container: Container
            A list containing the container obejct to be used by the pod 
        spec: kubenetes Spec objet:
            defines all the pod specifications  
        """

        config.load_kube_config()
        self.client = client.CoreV1Api()
        self.pod_name = pod_name
        self.name_space = name_space

        self.metadata = client.V1ObjectMeta(
                    name=self.pod_name,
                    namespace= self.name_space
                    )
        self.container = Container(container_name,container_image).create_container()
        self.spec = client.V1PodSpec(
                        containers=self.container
                        )

    def create_pod(self):
        """
        Creats and launches a kubernetes pod.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        pod_body = client.V1Pod(
                        metadata=self.metadata,
                         spec=self.spec
                        )

        self.client.create_namespaced_pod(namespace= self.name_space,body=pod_body)


    def delete_pod(self):
        """
        Deletes the created pod.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        self.client.delete_namespaced_pod(name=self.pod_name, namespace=self.name_space, body=client.V1DeleteOptions())
