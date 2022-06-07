# Business_Intelligence_UCR

![GitHub issues](https://img.shields.io/github/issues/MarioQuirosLuna/Readme-Template)
![GitHub closed issues](https://img.shields.io/github/issues-closed/MarioQuirosLuna/Readme-Template)
![GitHub pull requests](https://img.shields.io/github/issues-pr/MarioQuirosLuna/Readme-Template)

[![GitHub contributors](https://img.shields.io/github/contributors/MarioQuirosLuna/Readme-Template.svg?color=blue)](https://github.com/MarioQuirosLuna/Readme-Template/network)
![GitHub repo size](https://img.shields.io/github/repo-size/MarioQuirosLuna/Readme-template)
![GitHub language count](https://img.shields.io/github/languages/count/MarioQuirosLuna/Readme-template)
![GitHub forks](https://img.shields.io/github/forks/MarioQuirosLuna/Readme-template)

## ✨ Demo.

| Visualization with Power BI |
|-----------------------------|
| ![Demo](https://user-images.githubusercontent.com/37676736/172446014-3d8bda24-224b-433e-a7b3-bfc2e86d98a5.png) |

| Data Warehouse Star Model | Entity relationship model |
|---------------------------|---------------------------|
| ![ModeloEstrella_DW_NIKY](https://user-images.githubusercontent.com/37676736/172446709-a6f0e01a-a23a-4316-8457-5d0127bffd04.PNG) | ![ModeloER](https://user-images.githubusercontent.com/37676736/172446350-4e1c2e47-d3ea-414b-91d5-7d92bda8d0d0.jpeg) |

## 💻 About the project.

   ### 📜 Descriptions.
   * There is a data source in PosgreSQL.
   * A data store must be created to be analyzed.
   * An ETL process is responsible for extracting the data from the data source to transform it in the way that the business needs and then load it into the data warehouse.
   * A multidimensional cube must be created that allows data to be analyzed and answers to questions of interest to the business.
   * Reports are generated with the data provided through the Power BI tool.
   
   ### 🏆 Specifications.
   
   - [Proyecto-AdministracionDeBasesDeDatosUCR-2022.pdf](https://github.com/MarioQuirosLuna/Business_Intelligence_UCR/blob/master/IF5100%20Proyecto%20Final.pdf)


   ### ⭐ Languages.
   ![Python](https://custom-icon-badges.herokuapp.com/badge/-Python-%233776AB?style=flat&logo=Python&logoColor=white&labelColor=111)

   ### 🎨 Frameworks.
   
   ### 💾 Databases and cloud hosting.
  
  ![MSSQL](https://custom-icon-badges.herokuapp.com/badge/-MSSQL-%23CC2927?style=flat&logo=MicrosoftSQLServer&logoColor=white&labelColor=111)
  ![PostgreSQL](https://custom-icon-badges.herokuapp.com/badge/-PostgreSQL-%234169E1?style=flat&logo=PostgreSQL&logoColor=white&labelColor=111)
  
   ### 🛠️ Software and Tools.
   
  ![Git](https://custom-icon-badges.herokuapp.com/badge/-Git-%23F05032?style=flat&logo=git&logoColor=white&labelColor=111)
  ![GitHub](https://custom-icon-badges.herokuapp.com/badge/-GitHub-%23181717?style=flat&logo=github&logoColor=white&labelColor=111)
  ![Markdown](https://custom-icon-badges.herokuapp.com/badge/-Markdown-%23000000?style=flat&logo=Markdown&logoColor=white&labelColor=111)
  ![PowerBI](https://custom-icon-badges.herokuapp.com/badge/-PowerBI-%23F2C811?style=flat&logo=PowerBI&logoColor=white&labelColor=111)

  ![VisualStudioCode](https://custom-icon-badges.herokuapp.com/badge/-VisualStudioCode-%23007ACC?style=flat&logo=VisualStudioCode&logoColor=white&labelColor=111)
  ![VisualStudio](https://custom-icon-badges.herokuapp.com/badge/-VisualStudio-%235C2D91?style=flat&logo=VisualStudio&logoColor=white&labelColor=111)

## 🚀 Getting Started.

   # 1. Databases
   
   ### 📌 Prerequisites and dependencies.
   
   - Have PGAdmin installed.
   - Have SQLServer installed.
      - SQLServer with analytics services.
   
   ### 👉 Installation.
   
   ### ⚡ Executing.
   
   - Execute the script for create database and insert the data in PostgreSQL in descending order.

   ![imagen](https://user-images.githubusercontent.com/37676736/169353912-c3a0824c-da4a-4f1f-9762-b04e673448f0.png)

   - Create your database for data warehouse in SQL Server.
   
   # 2. ETL Python

   ### 📌 Prerequisites and dependencies.
   
   - Need install virtualenv package

   ```
      pip install virtualenv
   ```

   - Create virtual environment for run project with command line
      * On your project folder run command
      * This command create new virtual environment for run your project.

   ```
      virtualenv -p python3 env
   ```

   ### 👉 Installation.
   
   - Install the requirements.txt file dependencies. 
   
   ```
      pip install dependency1 dependency2 dependency3
   ```

   ### ⚡ Executing.
   
   - Create a .env file with the credentials of the databases that you are using.
   ```
      POSGRESQL_HOST=""
      POSGRESQL_USER=""
      POSGRESQL_PASS=""
      POSGRESQL_DATABASE=""
      
      POSGRESQL_HOST_LOCAL=localhost
      POSGRESQL_DATABASE_LOCAL=IF5100_2022_DATAWAREHOUSE_NIKY

      SQLSERVER_HOST=""
      SQLSERVER_DATABASE=""
      SQLSERVER_USER=""
      SQLSERVER_PASS=""
      
      SQLSERVER_HOST_LOCAL=localhost
      SQLSERVER_DATABASE_LOCAL=IF5100_2022_DATAWAREHOUSE_NIKY
   ```
   - Execute the virtual environment 
      * On your local folder run script activate
   ```
      .\env\Scripts\activate 
   ```
   - Run ETL Script
   ```python
      python etl.py
   ```
   
   # 3. Multidimensional cube
   
   ### 📌 Prerequisites and dependencies.
   
   - Need install visual studio 2022.
   
   ### 👉 Installation.
   
   - Need extention Microsoft Analysis Services Project 2022.
   
   ### ⚡ Executing.
   
   - Open solution Cubo_Multidimensional_Niky.sln in visual studio 2022.
   - Process Cube.
   
   # 4. Visualization with Power BI
   
   ## 📌 Prerequisites and dependencies.
   
   - Power BI Desktop
   
   ### 👉 Installation.
   
   - Open multidimensional cube.
   
   ### ⚡ Executing.
   
   - Create the visualization that is needed for the business.

## ☕ Collaborators.

* [![Mario Quiros Luna](https://custom-icon-badges.herokuapp.com/badge/-Mario%20Quirós%20Luna-%23181717?style=flat&logo=github&logoColor=white&labelColor=111)](https://github.com/MarioQuirosLuna)

## 📝 License.

## 💬 Contact.

[![Website](https://img.shields.io/website?label=Portfolio&up_color=%231E0A46&up_message=Mario%20Quiros%20Luna%20Dev&url=https%3A%2F%2Fmarioql-dev.vercel.app%2F)](https://marioql-dev.vercel.app/)
[![LinkedIn](https://custom-icon-badges.herokuapp.com/badge/-LinkedIn%20Mario%20Quirós%20Luna-%230A66C2?style=flat&logo=LinkedIn&logoColor=white&labelColor=111)](https://www.linkedin.com/in/mario-quir%C3%B3s-luna-dev-b99050206/)
[![Twitter URL](https://img.shields.io/twitter/url?label=Twitter%20%40MarioQuirosL&style=social&url=https%3A%2F%2Ftwitter.com%2FMarioQuirosL)](https://twitter.com/MarioQuirosL)
[![Github](https://img.shields.io/github/followers/MarioQuirosLuna?label=Github&style=social)](https://github.com/MarioQuirosLuna)

## 💜 Acknowledgments.
   - https://simpleicons.org/
