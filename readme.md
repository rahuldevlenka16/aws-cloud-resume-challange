Cloud Resume Challenge – AWS Implementation

This project is my implementation of the Cloud Resume Challenge, built on AWS using real cloud and DevOps skills.
The goal is to deploy a fully functional, secure, serverless resume website with a live visitor counter.

Work in progress..

diagram:

![alt text](<aws diagram.png>)

Flow:

    Users: They send HTTPS requests to access a secured HTML website hosted on Amazon CloudFront.

    Amazon CloudFront: Acts as a CDN, serving the static website (HTML, CSS, JS) to the user.

    S3 Bucket: Stores the static content of the website (e.g., index.html and CSS) and handles the synchronization of updates.

    API Gateway: Handles the GET request from the frontend to fetch the visitor count from the backend.

    Lambda Function: Responds to API requests, fetching the current visitor count and interacting with DynamoDB to update the count.

    DynamoDB: Stores the visitor count in a NoSQL database, updating each time a new request comes in.

    GitHub Actions: Triggered by commits to the Frontend repository (like new HTML, CSS updates) which deploy the changes to S3 and CloudFront.

    GitHub Secrets: Stores sensitive information such as AWS access keys used to manage the deployment process.