import docker

client = docker.from_env()

print("Running Containers:")
for container in client.containers.list():
    print(f"{container.name} - {container.status}")
