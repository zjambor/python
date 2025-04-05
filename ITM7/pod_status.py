from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()

def get_pod_status(namespace, pod_name):
    """
    Get the status and age of a pod.

    Args:
        namespace (str): The namespace the pod is in.
        pod_name (str): The name of the pod.

    Returns:
        A dictionary containing the pod's status and age.
    """
    pod = v1.read_namespaced_pod(namespace=namespace, name=pod_name)
    status = pod.status.phase
    creation_timestamp = pod.metadata.creation_timestamp
    age = (datetime.now(timezone.utc) - creation_timestamp).total_seconds() / 60
    return {"status": status, "age": f"{age:.2f} minutes"}

# Usage
namespace = "default"
pod_name = "my-pod"
print(get_pod_status(namespace, pod_name))