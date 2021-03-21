import configparser as cfg 
from pod.python_pod import Pod 


def get_pod_spec(file_path:str)->dict:
    """
    Reads the user pod specifications from the .ini file and transforms it to a dict 

            Parameters:
            -----------
                    file_path (str): A String representing the path of the pod specifications .ini file 

            Returns:
            -----------            
                    confdict (dict): A dictionary containing the pod specifications defined by the user
    """
    
    parser = cfg.ConfigParser()
    parser.read(file_path)
    confdict  = parser.__dict__['_sections'].copy()
    return confdict
        



if __name__=='__main__':

    pod_conf = get_pod_spec('specifications.ini')
    
    pod = Pod(
                pod_conf['POD_METADATA']['name'],
                pod_conf['POD_METADATA']['namespace'],
                pod_conf['CONTAINER']['containername'],
                pod_conf['CONTAINER']['containerimage']
              )

