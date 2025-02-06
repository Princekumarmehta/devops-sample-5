import docker
import time

client = docker.from_env()
flask_container = "flask_app"

while True:
    try:
        container = client.containers.get(flask_container)
        if container.status != "running":
            print(f"Restarting {flask_container}...")
            container.restart()
        else:
            print(f"{flask_container} is running fine")
    except docker.errors.NotFound:
        print(f"Container {flask_container} not found")
    time.sleep(10)
