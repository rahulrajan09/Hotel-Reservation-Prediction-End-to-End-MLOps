from setuptools import setup , find_packages

#opening requirements.txt and reading line by line
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

#project info setup
setup(
    name="Hotel Reservation Prediction — End-to-End MLOps on GCP" ,
    version="0.0.1" ,
    author="RahulR" ,
    packages=find_packages() ,
    install_requires=requirements ,
    
)