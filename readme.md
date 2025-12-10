✅ PHASES COMPLETED SO FAR
✔️ Phase 1 — Static Resume Website

You have completed:

Built index.html + styles.css

Hosted on S3 static website

Bucket made public with correct policy

Uploaded files via AWS CLI (aws s3 cp, sync)

Status: DONE ✔️

✔️ Phase 2 — Backend Visitor Counter

You built a fully working serverless backend:

Backend components:

DynamoDB table with initial count

IAM role for Lambda

Lambda function that increments visitor count

HTTP API Gateway with GET /dev/count

CORS enabled

Frontend JavaScript fetch() integrated

Counter visible on webpage (works via curl)

Status: DONE ✔️
(Only the browser-side issue is pending, likely CORS or caching.)

🟡 Phase 3 — CloudFront + HTTPS

You have not done Phase 3 yet, but you requested it next.

This phase includes:

Create CloudFront distribution

Connect S3 website as origin

Enable HTTPS (default from CloudFront)

Switch your website URL to CloudFront URL

Status: PENDING ⏳

We will do this next.

🟡 Phase 4 — Custom Domain (Optional but Recommended)

You own:

rahuldevlenka.online

rahuldevlenka.info

This phase includes:

Request SSL certificate from ACM (us-east-1)

Add DNS validation records

Attach domain to CloudFront

Create CNAME or A-Record alias

Website becomes:

https://rahuldevlenka.online


Status: PENDING ⏳

🟡 Phase 5 — Terraform Rewrite

This is the DevOps part where you convert everything into code:

Terraform will create:

S3 bucket

CloudFront

DynamoDB table

Lambda

API Gateway

IAM roles

Then you will delete manual resources and redeploy via Terraform.

Status: PENDING ⏳

🟡 Phase 6 — CI/CD (GitHub Actions)

Two pipelines:

1. Frontend pipeline

Upload new files to S3

Invalidate CloudFront cache

2. Backend pipeline

Build + deploy Lambda

Update API automatically

Use infrastructure as code

Status: PENDING ⏳

🟡 Phase 7 — Write Blog + Publish

Document how you built the project.
This is required in the official challenge.

Status: PENDING ⏳

🧩 Summary Table
Phase	Description	Status
1	S3 static site	✔️ DONE
2	Lambda + DynamoDB + API Gateway + JS	✔️ DONE
3	CloudFront + HTTPS	⏳ Pending
4	Custom Domain + SSL	⏳ Pending
5	Terraform rewrite	⏳ Pending
6	CI/CD pipelines	⏳ Pending
7	Blog post	⏳ Pending