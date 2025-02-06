import docker

client = docker.from_env()

# Create a network if not exists
network_name = "flask_network"
if network_name not in [net.name for net in client.networks.list()]:
    client.networks.create(network_name, driver="bridge")
    print(f"Network '{network_name}' created")
else:
    print(f"Network '{network_name}' already exists")

# Start Containers
containers = ["mongo_db", "flask_app"]
for container in containers:
    try:
        container_instance = client.containers.get(container)
        container_instance.start()
        print(f"Started {container}")
    except docker.errors.NotFound:
        print(f"{container} not found")
