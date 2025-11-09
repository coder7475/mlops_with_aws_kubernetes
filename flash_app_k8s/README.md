# 🚀 Flask App Deployment on Kubernetes

This project demonstrates how to create a simple **Flask REST API**, containerize it with **Docker**, and deploy it to **Kubernetes** using a **Makefile** for automation.

---

## 📁 Project Structure

```

.
├── app.py
├── Dockerfile
├── deployment.yaml
├── Makefile
└── README.md

````

---

## 🧩 Features

- Simple Flask REST API with dynamic routes  
- Dockerized application for easy deployment  
- Kubernetes Deployment and Service configuration  
- Automated build, push, and deploy using Makefile  
- LoadBalancer service for external access  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/flask-k8s-deploy.git
cd flask-k8s-deploy
````

### 2. Build and Run Locally (Optional)

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## ☸️ Kubernetes Deployment

### 3. Build, Push, and Deploy using Makefile

Update your Docker Hub username in the `Makefile`:

```makefile
IMAGE_NAME=your-dockerhub-username/flask-app
```

Then run:

```bash
make all
```

This will:

1. Build the Docker image
2. Push it to Docker Hub
3. Apply the Kubernetes deployment and service

---

## 🔍 Verify Deployment

Check running pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get svc
```

Once the external IP is assigned, open it in your browser:

```
http://<EXTERNAL-IP>
```

---

## 🧹 Cleanup

To delete all resources:

```bash
make clean
```

---

## 🧠 Technologies Used

* **Python** (Flask)
* **Docker**
* **Kubernetes**
* **Makefile**
* **kubectl**

---

## 🪲 Common Issues

### 🧩 Error: `requested access to the resource is denied`

* Run `docker login` to authenticate with Docker Hub.
* Ensure the repository name matches your Docker Hub username:

  ```makefile
  IMAGE_NAME=your-actual-username/flask-app
  ```

---

## 📚 References

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Docker Docs](https://docs.docker.com/)
* [Kubernetes Docs](https://kubernetes.io/docs/home/)
* [GNU Make Documentation](https://www.gnu.org/software/make/manual/make.html)


**Author:** Robiul Hossain
**License:** MIT



