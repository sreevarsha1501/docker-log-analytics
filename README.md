# Docker Log Analytics Project

## Project Overview

This project demonstrates core Docker concepts through a simple Flask-based Log Analytics application. The goal of this project is to understand how Docker containers handle application deployment, persistent storage, logging, networking, debugging, and image distribution using Docker Hub.
The key goal is to work on both Volumes and Bind Mounts.
Throughout this project, the following Docker concepts were implemented and tested:

* Docker Images
* Docker Containers
* Docker Volumes
* Docker Bind Mounts
* Docker Compose
* Docker Networking
* Docker Logs & Debugging
* Container Inspection
* Docker Hub Image Management

---

# Project Structure

```text
docker-log-analytics/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── logs/
│   └── app.log
│
├── dockerfile
├── docker-compose.yml
└── README.md
```

---

# Step 1: Creating Project Structure

The project was created from scratch by creating separate folders for application source code and log storage.

```bash
mkdir docker-log-analytics
cd docker-log-analytics

mkdir app logs
```

The Flask application source code was placed inside the `app` directory while application logs were configured to be written into the `logs` directory.

---



<img width="1920" height="1080" alt="Project structure" src="https://github.com/user-attachments/assets/64a2534f-0308-4f17-b114-110138f1081f" />


---

# Step 2: Creating Flask Application

A simple Flask application was developed to:

* Serve a web page
* Generate application logs
* Store logs inside a mounted Docker volume

Every user visit generates log entries that are written into `app.log`.

Example:

```text
INFO:root:User visited Home Page
```

---

# Step 3: Building Docker Image

A Dockerfile was created to package the Flask application into a reusable Docker image.

Image Build Command:

```bash
docker build -t log-app .
```

After the build process, Docker created a new image containing:

* Python Runtime
* Flask Dependencies
* Application Source Code

Verify Images:

```bash
docker images
```

---

## Screenshot

<img width="1920" height="633" alt="Building images" src="https://github.com/user-attachments/assets/cd7d49fe-1ca6-4368-b0a5-3cf37c743ff9" />


# Step 4: Docker Volumes

A Docker Volume was created to persist application logs even after container deletion.

Create Volume:

```bash
docker volume create app-logs
```

Verify:

```bash
docker volume ls
```

Run Container Using Volume:

```bash
docker run -d \
-p 5000:5000 \
-v app-logs:/logs \
--name log-container \
log-app
```

---

## Why Docker Volumes?

Normally, container data is lost when a container is deleted.

Volumes provide:

* Persistent Storage
* Data Retention
* Backup Capability
* Container Independence

Even after removing the container:

```bash
docker rm -f log-container
```

the log file remains inside the volume.

---
<img width="1918" height="1010" alt="Creating volume" src="https://github.com/user-attachments/assets/3a0fb0fc-458d-4fc3-9454-92af4d240f35" />

---

# Step 5: Running Containers & Generating Logs

After starting the container, the application became accessible through:

```text
http://localhost:5000
```

Every page visit generated new log entries.

Logs were verified from inside the container.

Enter Container:

```bash
docker exec -it log-container bash
```

View Logs:

```bash
cat /logs/app.log
```

---

<img width="1882" height="823" alt="Running containers and viewing logs" src="https://github.com/user-attachments/assets/b969cdeb-a05a-4875-9685-4143a06707f9" />

---

# Step 6: Testing Application

The Flask application was accessed through the browser.

Each page request generated:

* Application Logs
* Access Logs
* Container Logs

This demonstrated how containerized applications generate runtime logs.

---
<img width="1918" height="868" alt="Flask application output" src="https://github.com/user-attachments/assets/4e4ee87e-ac93-4d3b-acb3-e929091ae326" />

---

# Step 7: Docker Bind Mounts

Next, Docker Bind Mounts were implemented.

Container Logs were directly mapped to a host machine folder.

Run Container:

```bash
docker run -d \
-p 5000:5000 \
-v $(pwd)/logs:/logs \
--name log-container \
log-app
```

Now logs became immediately visible on the host machine.

Host Verification:

```bash
cd logs
cat app.log
```

---

## Why Bind Mounts?

Bind mounts are useful during development because changes made inside the container are instantly visible on the host system.

Benefits:

* Real-time file access
* Easy debugging
* Development convenience

---
<img width="1917" height="802" alt="Bind mounting the logs" src="https://github.com/user-attachments/assets/1777c0c7-c3e7-48a1-be28-b4ead73c999f" />

---

# Docker Volume vs Bind Mount

| Feature                  | Docker Volume | Bind Mount |
| ------------------------ | ------------- | ---------- |
| Managed By Docker        | Yes           | No         |
| Stored In Docker Storage | Yes           | No         |
| Host Path Required       | No            | Yes        |
| Production Usage         | Recommended   | Limited    |
| Development Usage        | Good          | Excellent  |
| Portability              | High          | Low        |

---

# Step 8: Docker Compose

Managing containers using long Docker commands becomes difficult in real-world projects.

Docker Compose was introduced to simplify container management.

A `docker-compose.yml` file was created.

Start Application:

```bash
docker compose up -d
```

Stop Application:

```bash
docker compose down
```

---

## Benefits of Docker Compose

* Infrastructure as Code
* Single Command Deployment
* Easier Scaling
* Automatic Networking
* Easier Maintenance

---

## Automatic Network Creation

When Compose started, Docker automatically created:

```text
docker-log-analytics_default
```

This custom bridge network allows future services such as:

* PostgreSQL
* Redis
* Nginx

to communicate using service names instead of IP addresses.

Example:

```text
Flask → PostgreSQL
Flask → Redis
```

without manually creating networks.

---
<img width="1918" height="1021" alt="Docker compose" src="https://github.com/user-attachments/assets/79db7a41-50ec-42c5-b123-43d3fbacea65" />


---

# Step 9: Docker Logs & Debugging

Docker provides built-in log inspection.

View Logs:

```bash
docker logs flask-app
```

Follow Live Logs:

```bash
docker logs -f flask-app
```

Timestamped Logs:

```bash
docker logs -t flask-app
```

These commands are commonly used for troubleshooting containerized applications.

---

<img width="1773" height="648" alt="Logs" src="https://github.com/user-attachments/assets/829d7e51-d522-4fd1-8a52-7525c204bd7f" />


---

# Step 10: Container Inspection & Port Verification

The running container was inspected.

Enter Container:

```bash
docker exec -it flask-app bash
```

Install Network Tools:

```bash
apt update
apt install net-tools -y
```

Verify Listening Ports:

```bash
netstat -tulpn
```

Output showed:

```text
0.0.0.0:5000
```

which confirmed the Flask application was actively listening on port 5000 inside the container.

---

## Why netstat?

netstat helps identify:

* Running Services
* Open Ports
* Active Connections
* Network Troubleshooting

This is a common debugging technique used by DevOps engineers.

---
<img width="1918" height="701" alt="Checking details using netstat" src="https://github.com/user-attachments/assets/45c2a66c-65ed-4fd8-9496-029252241881" />

---

# Step 11: Publishing Images to Docker Hub

After successful testing, images were pushed to Docker Hub.

Tag Image:

```bash
docker tag log-app varsha1501/docker-log-analytics-app
```

Push Image:

```bash
docker push varsha1501/docker-log-analytics-app
```

Benefits:

* Centralized Image Storage
* Easy Sharing
* CI/CD Integration
* Production Deployment

Images can later be pulled using:

```bash
docker pull varsha1501/docker-log-analytics-app
```

and run without requiring the original project source code.

---
<img width="1918" height="966" alt="Dockerhub" src="https://github.com/user-attachments/assets/9810bdce-23c3-4653-9ea9-c798545d2db5" />

---


# Future Enhancements

This project can be extended into a production-grade architecture by integrating:

* PostgreSQL Database
* Redis Cache
* Nginx Reverse Proxy
* Health Checks
* Environment Variables
* Multi-Container Communication
* Monitoring & Alerting

---

# Conclusion

This project provided hands-on experience with Docker fundamentals while demonstrating how real-world containerized applications manage storage, logging, networking, debugging, and deployment. It serves as a strong foundation for building multi-container applications using Docker Compose and cloud-native deployment workflows.
