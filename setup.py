from setuptools import setup, find_packages

setup(
    name="face_voting_system",
    version="0.1.0",
    author="Ajursha Dahal",
    author_email="ajursha@gmail.com",
    description="A face recognition-based voting system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/face_voting_system",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
        "opencv-python",
        "face-recognition",
        "numpy",
    ],
    python_requires=">=3.6",
)
