# ☁️ AWS S3 Bucket Setup for MLOps Workflow

This guide documents the process of creating and configuring an **Amazon S3 bucket** for use in an **MLOps workflow** (e.g., with MLflow and Kubernetes). It includes steps for creating a unique bucket, enabling versioning, and verifying configuration using the **AWS CLI**.

---

## 📋 Prerequisites

Before starting, make sure you have the following:

- ✅ An **AWS account** with sufficient permissions to create S3 buckets
- ✅ **AWS CLI** installed and configured with credentials
  ```bash
  aws configure
  ```

* ✅ A unique **bucket name** (since S3 bucket names are globally unique)

---

## 🪣 Step 1: Create an S3 Bucket

First, attempt to create your bucket in the `ap-southeast-1` region.

```bash
aws s3api create-bucket \
  --bucket my-bucket-1 \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
```

If you see the following error:

```
An error occurred (BucketAlreadyExists) when calling the CreateBucket operation:
The requested bucket name is not available. The bucket namespace is shared by all users of the system.
Please select a different name and try again.
```

It means that the bucket name is already taken. Choose a **unique** name and try again.

---

## ✅ Step 2: Create a Unique Bucket

```bash
aws s3api create-bucket \
  --bucket my-coder-bucket-1 \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
```

Expected output:

```json
{
  "Location": "http://my-coder-bucket-1.s3.amazonaws.com/"
}
```

---

## 🔄 Step 3: Enable Versioning

Enabling versioning helps track changes to objects and prevents accidental data loss.

```bash
aws s3api put-bucket-versioning \
  --bucket my-coder-bucket-1 \
  --versioning-configuration Status=Enabled
```

---

## 🧩 Step 4: Verify Versioning Status

To confirm versioning is enabled:

```bash
aws s3api get-bucket-versioning \
  --bucket my-coder-bucket-1
```

Expected output:

```json
{
  "Status": "Enabled"
}
```

---

## 🧠 Notes

- The **S3 bucket namespace is global** — all AWS users share it.
- Always use **region-specific constraints** when creating buckets outside of `us-east-1`.
- Versioning adds extra storage costs since all object versions are retained.

---

## 📚 References

- [AWS CLI — s3api create-bucket](https://docs.aws.amazon.com/cli/latest/reference/s3api/create-bucket.html)
- [AWS CLI — s3api put-bucket-versioning](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-versioning.html)
- [AWS S3 Bucket Naming Rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html)

```

```
