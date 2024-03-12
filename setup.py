from setuptools import find_namespace_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Yusuf Aliyu",
    author_email="yaliyu003@gmail.com",
    install_requires = ["openai",'langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_namespace_packages()
)