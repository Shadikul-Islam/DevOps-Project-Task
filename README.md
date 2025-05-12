<h2 align="center">DevOps Challenge: API Development, Deployment & System Architecture</h2>

<br><br><br>

| **SL** | **Topic** |
| --- | --- |
| 01 | [Introduction](#01) |
| 02 | [Repository Structure](#02) |
| 03 | [Part A: Develop & Deploy a REST API](#03) |
| 04 | [Part B:System Architecture Design](#04) |
| 05 | [Security Highlights](#05) |
| 06 | [Local Setup & Testing](#06) |
| 07 | [Screenshots](#07) |
| 08 | [Conclusion](#08) |

<br>

## <a name="01">Introduction</a>

This repository contains the solution to a DevOps challenge that includes developing and deploying a REST API (Part A), and designing a scalable system architecture for an e-commerce application (Part B). The project uses Python Flask, Jenkins, AWS, Docker, Kubernetes, and Terraform.

<br>

## <a name="02">Repository Structure</a>

      └── DevOps-Project-Task
          ├── docker-registry-setup
          │   └── docker-compose.yml
          ├── images
          │   ├── architecture-diagram.png
          │   └── screenshots
          │       ├── flask-api-response.png
          │       └── jenkins-success.png
          ├── jenkins-setup
          │   ├── docker-compose.yml
          │   └── Dockerfile
          ├── k8s-manifest
          │   ├── deployment.yml
          │   ├── secret.yml
          │   └── service.yml
          ├── README.md
          ├── terraform
          │   ├── envs
          │   │   └── prod
          │   │       ├── main.tf
          │   │       ├── terraform.tfstate
          │   │       ├── terraform.tfvars
          │   │       └── variables.tf
          │   └── modules
          │       └── eks
          │           ├── main.tf
          │           ├── outputs.tf
          │           └── variables.tf
          └── weather-api-project
              ├── code
              │   ├── app
              │   │   ├── __init__.py
              │   │   └── main.py
              │   └── requirements.txt
              ├── docker
              │   ├── docker-compose.yml
              │   ├── Dockerfile.dev
              │   └── Dockerfile.prod
              └── jenkins
                  ├── docker.jenkinsfile
                  └── k8s.jenkinsfile

<br>

## <a name="03">Part A: Develop & Deploy a REST API</a>

### 1. REST API Implementation:
   - **Framework:** Python Flask
   - **Endpoints:**
      - ```/api/hello:``` Returns hostname, datetime, version, and weather data for Dhaka.
      - ```/api/health:``` Health check that verifies API and 3rd-party weather service availability.

  - **Weather Integration:** Fetches real-time weather data from a free public API.
  - **Sample JSON response:**
    ```json
    {
      "hostname": "server1",
      "datetime": "2505121502",
      "version": "v1.0.0",
      "weather": {
        "dhaka": {
          "temperature": "33",
          "temp_unit": "c"
        }
      }
    }

### 2. Containerization
  - ```Dockerfile.dev:``` Used for local development with live reload.

  - ```Dockerfile.prod:``` Optimized for production deployment.

  - ```docker-compose.yml:``` For development environment.

### 3. CI/CD Pipeline (Jenkins)
  - **Tool:** Jenkins (Dockerized)

  - **Pipeline Includes:**

    - Pull latest code from Github
  
    - Build and tag Docker image using the release version
  
    - Push image to public Docker registry
  
    - Validate that /api/hello returns the correct version
  
    - Deploy the updated container to Kubernetes on AWS
  
    - Ensure zero-downtime deployments using Kubernetes rollout strategies

  - **Jenkinsfiles:**

    - ```docker.jenkinsfile:``` CI pipeline for Docker image build and push
    
    - ```k8s.jenkinsfile:``` CD pipeline for Kubernetes deployment

### 4. Infrastructure-as-Code

  - **Terraform (AWS EKS)**
    - Modular Terraform structure:

      - ```modules/eks:``` Manages EKS cluster creation
      
      - ```envs/prod:``` Environment-specific configurations and remote backend
      
      - Secrets (like API keys) are stored as Kubernetes secrets
      
      - Backend is managed via ```terraform.tfstate```
     
  - **Kubernetes**
    - ```deployment.yml:``` Defines Flask app deployment
    
    - ```service.yml:``` Exposes app within the cluster
    
    - ```secret.yml:``` Securely stores API credentials

<br>
   
## <a name="04">Part B: System Architecture Design</a>

### 1. Web Application Using AWS Services

  - **Amazon EC2 Instances:** We can use multiple EC2 instances running the web application code. These instances should be distributed across multiple Availability Zones for high availability.

  - **Auto Scaling:** Set up an Auto Scaling group to automatically adjust the number of EC2 instances based on traffic load.

  - **Using Open Source Tools:**

  - **Web Server:** We can use open-source web servers like Nginx or Apache to host the e-commerce website. We can deploy them on an AWS EC2 Instance or any virtual machines or dedicated servers.

  - **Application Framework:** We can build our application from scratch using any preferred programming language and also we can choose a web application framework such as Magento, WooCommerce (WordPress), or OpenCart for building the e-commerce site.


### 2. Database

  - **Amazon RDS for MySQL:** We can use Amazon RDS for the relational database by enabling Multi-AZ deployments for high availability and automated failover.

  - **Using Open Source Tools:**

  - **MySQL or PostgreSQL:** We can also use open-source relational databases like MySQL or PostgreSQL for storing product information, customer data, and order history.

### 3. Caching

  - **Amazon ElastiCache:** We can implement Amazon ElastiCache (Redis or Memcached) for caching frequently accessed data, such as product listings and session data, to reduce the load on the database and improve performance.

  - **Using Open Source Tools:**

  - **Redis:** We can also implement open-source caching solutions like Redis to cache frequently accessed data for faster response times.

### 4. Data Storage

  - **Amazon S3:** Store and serve static assets (images, CSS, JavaScript) from Amazon S3. Enable S3 standard for durable and scalable object storage.

  - **DynamoDB:** Use DynamoDB's on-demand capacity for storing high-traffic, low-latency data, such as user sessions and shopping carts.

  - **Using Open Source Tools:**

  - **Local File Storage:** Store static assets (images, CSS, JavaScript) on local file storage or network-attached storage (NAS).

### 5. Load Balancing

  - **Application Load Balancer (ALB):** Set up an Application Load Balancer to distribute incoming traffic among multiple EC2 instances for load balancing.


### 6. Security and Identity

  - **IAM:** Create IAM users and roles for role management and secure access to AWS resources.

  - **AWS Web Application Firewall (WAF):** Implement WAF to protect against web application attacks.

  - **Amazon Cognito:** Use Amazon Cognito for user authentication and secure access control.

  - **AWS KMS:** Manage encryption keys with AWS Key Management Service to ensure data is encrypted at rest and in transit.

### 7. Monitoring and Analytics

  - **Amazon CloudWatch:** Monitor resource utilization, set up alarms for scaling, and collect logs for analysis.

  - **AWS Lambda:** Use Lambda functions for custom metrics and monitoring tasks.

  - **Amazon CloudFront:** Integrate Amazon CloudFront as a Content Delivery Network (CDN) for faster content delivery and caching.

### 8. Email Service

  - **Amazon SES:** Integrate Amazon SES for sending transactional emails to customers with a responsive email design.

### 9. Backup and Recovery 

  - **Amazon EBS Snapshots (Elastic Block Store):** For backup and recovery of block storage volumes used with EC2 instances, Amazon EBS provides snapshot capabilities. Snapshots allow us to capture a point-in-time copy of our EBS volumes.

  - **AWS Backup:** AWS Backup is a centralized backup service that simplifies the process of backing up data from various AWS services, such as EC2, RDS, and EFS. It offers a unified management interface for creating and managing backups.

  - **Amazon RDS Automated Backups:** Amazon RDS for our RDS databases, comes with automated backup features. We can enable automated daily backups and maintain a specified retention period.

### 10. High Availability

  - **Multiple Availability Zones:** We need to use multiple Availability Zones for EC2 instances, RDS, and other critical services to ensure redundancy.

<br>

## <a name="05">Security Highlights</a>

  - Docker image runs as a non-root user
  
  - Secrets stored using Kubernetes secrets
  
  - Minimal RBAC in Jenkins and cloud roles
  
  - External API keys never hard-coded in source


<br>

## <a name="06">Local Setup & Testing</a>
### Setup
- Clone the repo: ```git clone https://github.com/Shadikul-Islam/DevOps-Project-Task.git```
- Go inside the directory: ```cd DevOps-Project-Task/weather-api-project/docker```
- Run Project: ```docker-compose up --build```

### Testing
- http://localhost:8000/api/hello
- http://localhost:8000/api/health


<br>
    
## <a name="07">Screenshots</a>

### 1. Directory Structure

      ├── images
      │   ├── architecture-diagram.png
      │   └── screenshots
      │       ├── flask-api-response.png
      │       └── jenkins-success.png


### 2. Cloud Architecture Diagram

<img src= "https://github.com/Shadikul-Islam/DevOps-Project-Task/blob/master/images/architecture-diagram.png" alt="architecture-diagram"> <br><be
                                                                                                                             >

### 3. Flask-api-response

<img src= "https://github.com/Shadikul-Islam/DevOps-Project-Task/blob/master/images/screenshots/flask-api-response.png" alt="flask-api-response"> <br><br>



### 4. Jenkins Success Pipeline

<img src= "https://github.com/Shadikul-Islam/DevOps-Project-Task/blob/master/images/screenshots/jenkins-success.png" alt="jenkins-success"> <br><br>


<br>

## <a name="08">Conclusion</a>
This project showcases a comprehensive DevOps workflow—from API development to production-ready deployment—by integrating modern technologies such as Flask, Docker, Jenkins, Terraform, and Kubernetes on AWS. Through modular infrastructure-as-code, secure CI/CD pipelines, and a scalable architecture design, the solution demonstrates best practices in automation, observability, and cloud-native development.

In Part A, a resilient and extensible REST API was built, containerized, and deployed with zero downtime using Kubernetes and Jenkins. In Part B, the proposed system architecture is designed to handle millions of global requests efficiently, focusing on scalability, high availability, and cost optimization.

This challenge provided a practical opportunity to apply DevOps principles end-to-end, reinforcing the importance of automation, modularity, and security in modern application delivery pipelines.
