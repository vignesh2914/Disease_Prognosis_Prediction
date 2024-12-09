## **Disease Prognosis**



### **Screenshot Predicted Output**

![Disease Prognosis Overview](images/ss_01.png)
![Disease Prognosis Overview](images/ss_02.png)

### **Docker Image**

The Docker image for this project is available on Docker Hub:

[ponvigneswaran/disease-prognosis-app](https://hub.docker.com/r/ponvigneswaran/disease-prognosis-app/tags)


### MLflow Integration

We have successfully integrated MLflow to track and save model parameters for experimentation. You can view the details of the tested parameters in the following links:

- **Run Details**: 🏃[View run unruly-bear-197](https://dagshub.com/vignesh2914/Disease_Prognosis_Prediction.mlflow/#/experiments/0/runs/ccfea322ad5746d7a89dbe361afa51c1)
- **Experiment Overview**: 🧪[View experiment](https://dagshub.com/vignesh2914/Disease_Prognosis_Prediction.mlflow/#/experiments/0)

## **Workflow**

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update app.py

## **Important Note**

- One of the main focuses of this project is modular coding.
- Additionally, the prediction process is a key component.

Happy learning!!!!

## **AWS-CICD-Deployment-with-Github-Actions**

1. Login to AWS console.
2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## **3. Create ECR repo to store/save docker image**

- Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/mlproj

## **4. Create EC2 machine (Ubuntu)**

## **5. Open EC2 and Install docker in EC2 Machine:**

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## **6. Configure EC2 as self-hosted runner:**

setting>actions>runner>new self hosted runner> choose os> then run command one by one

## **7. Setup github secrets:**

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app




