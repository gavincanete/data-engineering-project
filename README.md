# Viper Data Pipeline
End-to-End project for extracting viper shoes </br>
The objective of this project is to be be able to view the list of shoes from the Jupyter notebook. <br>

<b>From this:</b> </br>
![Screenshot from 2023-07-20 19-37-09](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/51b2bb2d-ad62-4f60-8f0c-d8780854c4a3)

<b>To this:</b> </br>
![Screenshot from 2023-07-20 19-38-55](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/f06e53cf-61a1-4e69-ad77-ef9040bfc985)

## Data Flow
![viper_data_pipeline](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/369fade7-c978-4607-8763-44ef7cd1571c) </br>
<i>Explanation</i>: </br>
Applying Web scraping (BeautifulSoup) to extract the information from the shoes and load it into postgresql via Airflow

## Prerequisites
1) Install the following python packages: </br>
   (requests, beautifulsoup4, pyscopg2, apache-airflow) via pip install <package name> </br>
   ```E.g. pip install configParser```
2) Setting up Postgresql </br>
   ```sudo apt-get install postgresql``` </br>
   ```sudo -i -u postgres``` </br>
   if successfully login, type ```psql``` </br>
   [Output] </br>
   ![Screenshot from 2023-07-20 18-13-14](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/0e43bbe3-a49e-4966-b51e-e5be3246dcbf) </br>
3) Create Shoe Database from Postgresql </br>
   ```create database shoe_db;``` </br>
   ```\c shoe_db``` </br>
    [Output] </br>
    ![Screenshot from 2023-07-20 18-17-23](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/7e734b25-2906-4b3c-9f75-e1134bed819c)

## Setting up Data Pipeline
1) Clone this repository
2) Create <i>shoe_database.ini</i> and place it on the <i>dags folder</i> </br>
   <i>The content of the ini file, should look like this</i></br>
   ![Screenshot from 2023-07-20 19-01-06](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/d1be1dd9-f3c4-4de8-bb58-99185a8ad6a9)
3) Starting the airflow</br>
   ```cd dags/``` </br>
   ```airflow standalone``` (Note: Please change first the path under <i>airflow.cfg</i>)
4) In airflow UI, locate the <i>shoe_dag</i> and run this workflow </br>
   [DAG] </br>
   ![Screenshot from 2023-07-20 19-17-49](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/d06b03d0-4bb5-496c-9f40-1d4b14f94a09)
5) After completion, Open <i>Jupyter Notebook</i> under the <i>dags folder</i>
6) Under Notebook, Select <i>Shoe Visualizer</i>
7) Execute each code provided </br>
   [Output] </br>
   ![Screenshot from 2023-07-20 19-29-42](https://github.com/gavincanete/viper-data-pipeline/assets/33832344/ee5433d8-1d50-47d2-bda3-9bceb8aba5f0)


   




