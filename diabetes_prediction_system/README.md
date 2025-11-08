# Setting up the environment

## Updating Ubuntu and installing dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip -y
```

## Create a FastAPI project

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### On Unix or macOS:

```bash
source venv/bin/activate
```

---

## Create a `requirements.txt` file

Create a `requirements.txt` file in the root directory of the project and paste the below content.
This file contains all required dependencies so they can be installed with a single command.

```
fastapi
uvicorn
scikit-learn
numpy
pandas
pydantic
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## Set up Kaggle API and download dataset

```bash
pip install kaggle
mkdir ~/.kaggle
echo '{"username":"YOUR_KAGGLE_USERNAME","key":"YOUR_KAGGLE_API_KEY"}' > ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d uciml/pima-indians-diabetes-database
unzip pima-indians-diabetes-database.zip -d data/
```

> ⚠️ **Note:** Replace `YOUR_KAGGLE_USERNAME` and `YOUR_KAGGLE_API_KEY` with your actual credentials.

---

**Reference:**

* [Kaggle API Documentation](https://www.kaggle.com/docs/api)
