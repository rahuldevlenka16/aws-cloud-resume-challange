Update 1 : added terraaform code for complete infra provising (cloudfront, s3, api GW, lambda, dynamodb), refer to this github repo : https://github.com/rahuldevlenka16/Terraform-CRC-infra



![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![CloudFront](https://img.shields.io/badge/CloudFront-CDN-purple?logo=amazonaws)
![S3](https://img.shields.io/badge/S3-Static%20Hosting-red?logo=amazonaws)
![Lambda](https://img.shields.io/badge/Lambda-Serverless-orange?logo=awslambda)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-4053D6?logo=amazon-dynamodb)
![API Gateway](https://img.shields.io/badge/API%20Gateway-REST%20API-blueviolet?logo=amazonaws)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions)
![Serverless](https://img.shields.io/badge/Serverless-Architecture-FD5750?logo=serverless)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript)
![Python](https://img.shields.io/badge/Python-Lambda%20Function-3776AB?logo=python)


🌩️ Cloud Resume Challenge – Serverless Web App with Visitor Counter

This project is a complete implementation of the Cloud Resume Challenge, featuring a secure static website hosted on AWS, a fully serverless backend for tracking visitor count, and CI/CD automation using GitHub Actions.

It demonstrates practical experience with AWS, CI/CD, Serverless Architecture, Automation, and Full-Stack Cloud Development.

The challange : https://cloudresumechallenge.dev/docs/the-challenge/aws/

🚀 Features

    Static website hosted on Amazon S3
    
    CloudFront CDN for global, HTTPS-secured delivery
    
    AWS Lambda backend to increment visitor count
    
    DynamoDB table to store and update count
    
    API Gateway exposing /count endpoint
    
    GitHub Actions CI/CD pipelines for:
    
    Frontend deploy to S3
    
    Backend Lambda code updates
    
    Secure handling of AWS credentials with GitHub Secrets


🔐 Security Considerations

    All traffic served over HTTPS via CloudFront
    
    S3 bucket is not public — only CloudFront accesses it
    
    AWS credentials stored in GitHub Secrets
    
    IAM follows least privilege principle

Architecture diagram:

<!-- <img width="1132" height="622" alt="aws diagram" src="https://github.com/user-attachments/assets/9aa44f27-3cfe-42f7-8cee-2ee49736c129" /> -->
<!-- <img width="1506" height="701" alt="2" src="https://github.com/user-attachments/assets/34a011b7-3166-4a82-8c54-94b6f910f6bb" /> -->
<img width="2445" height="1451" alt="CRC original" src="https://github.com/user-attachments/assets/b145b95c-7e07-4864-9b71-6b2215d40d57" />


<!-- <img width="1819" height="1048" alt="cicd" src="https://github.com/user-attachments/assets/65e68d7b-614c-4470-9d59-04f1193d383a" /> -->


<!-- <img width="1893" height="1027" alt="runtime" src="https://github.com/user-attachments/assets/11806686-c377-40d1-ac8b-d93b11a70cb6" /> -->


Architecture Flow:

    Frontend (HTML/CSS/JS) and Backend (Lambda code) are stored in GitHub.

    Code commits trigger GitHub Actions CI/CD pipelines:
    
        Frontend pipeline uploads static files to S3 and (optionally) invalidates CloudFront cache.
        
        Backend pipeline packages and deploys updated Lambda code.
    
    CloudFront serves the website securely over HTTPS, fetching files from the S3 Bucket.
    
    When a visitor opens the site, frontend JavaScript calls the /count API endpoint.
    
    API Gateway forwards this request to the Lambda function.
    
    Lambda reads, increments, and updates the visitor count in DynamoDB which reponds with new count.
    
    Lambda forwards the new count to API Gateway.

    API Gateway forwards JSON response to Website.
    
    The website updates the displayed visitor count dynamically based on the Lambda response.



Screenshots:

Sample resume from cloudfront url with visitor counts
![alt text](images/resume-website.png)


s3 bucket with static resume content
![alt text](images/s3.png)


API gateway with GET reoute and lambda integration
![alt text](images/image.png)

Lambda function with API gateway trigger
![alt text](images/lambda-func.png)


DynamoDB visitor-count table
![alt text](images/dynamodb.png)


Frontend github action
![alt text](images/frontend-yaml.png)

Before running the pipeline
![alt text](images/before.png)

After running the pipeline
![alt text](images/after.png)

before cloudfront invalidation
![alt text](images/old-resume.png)

after cloudfront invalidation
![alt text](images/new-resume.png)

it created and updated in console
![alt text](images/invalidation-success.png)
