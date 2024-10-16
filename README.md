# 🗂️ Hotel Reservations

## 📚 Descrição

Este projeto visa desenvolver uma **Web API** para a categorização de reservas de hotéis, utilizando **Python** e o framework **FastAPI**. A API oferece um endpoint `/api/v1/inference` que permite realizar inferências sobre novas reservas, utilizando um modelo de **Machine Learning** treinado com **XGBoost** para prever a categoria das reservas com base nas informações fornecidas pelo usuário.

A arquitetura do projeto foi desenhada para garantir escalabilidade e eficiência, empregando serviços da **AWS** para armazenamento e processamento. O modelo de machine learning foi treinado e gerenciado no **AWS SageMaker** e posteriormente armazenado no **AWS S3**. A API é hospedada no **AWS EC2**, e os dados das reservas são armazenados no banco de dados **AWS RDS**.

<br>

<img src="https://skillicons.dev/icons?i=python,aws,fastapi,docker,mysql&perline=8" />

---

## 📑 Índices

1. [Tecnologias](#tecnologias)
   - [Trello](#trello)
   - [Python](#python)
   - [Docker](#docker)
   - [API](#api)
   - [Machine Learning](#machine-learning)
   - [AWS](#aws)
2. [Funcionalidades](#funcionalidades)
3. [Deployment](#deployment)
4. [Requisitos](#requisitos)
   - [Técnicos](#técnicos)
   - [Cliente Final](#cliente-final)
   - [Custos](#custos)
5. [Acesso](#acesso)
6. [Aprendizado](#aprendizado)
   - [Dificuldades Gerais](#dificuldades-gerais)
   - [Lições Aprendidas](#lições-aprendidas)
7. [Cargos](#cargos)
8. [Colaboradores](#colaboradores)

---

## 🛠️ Tecnologias

### ![Trello](https://img.shields.io/badge/-026AA7?style=plastic&logo=trello&logoColor=white) **Trello**
- **Gestão de Tarefas**: Utilizado para planejamento e acompanhamento das atividades do projeto.

### ![Python](https://img.shields.io/badge/-3E719A?style=plastic&logo=python&logoColor=FFE873) **Python**
- **Linguagem Principal**: Usada para o desenvolvimento da API, manipulação de dados e integração com serviços AWS.

### ![Docker](https://img.shields.io/badge/-ffffff?style=plastic&logo=docker&logoColor=3E719A) **Docker**
- **Containerização**: Facilita a criação de ambientes isolados para a execução da aplicação e garante consistência na implantação.

---

### 🌐 **API**
- **FastAPI**: Framework utilizado para construir a API de forma rápida e eficiente.
- **Docker**: Containeriza a API para simplificar a implantação e garantir ambientes consistentes.

### 📚 **Documentação da API**
- Acesse a documentação interativa da API através deste [link](http://98.82.230.43:80/docs).

### 🧠 **Machine Learning**
- **XGBoost**: Algoritmo de regressão e aprendizado supervisionado utilizado para categorizar reservas de hotéis com base em dados históricos.

### ☁️ **Serviços AWS**
- **AWS RDS**: Armazena os dados de reservas e permite o treinamento contínuo do modelo.
- **AWS SageMaker**: Serviço para treinamento e otimização do modelo de machine learning.
- **AWS S3**: Armazena o modelo de machine learning treinado e outros arquivos necessários.
- **AWS EC2**: Hospeda a API publicamente, permitindo seu acesso e consumo.

<br>

## 📦 Estrutura de Pastas

### EC2
- 📁 Api/
   - 📁 Api/
      - 📄 dataModels.py
   - 📄 .env
   - 📄 Dockerfile
   - 📄 main.py
   - 📄 requirements.txt

### S3
📁 sprint4-5/📁 modelos/📁 hotel-reservation/📁 XGBoost/📁 output/📁 sagemaker-xgboost.../📁 output/📚 model.tar.gz

### SageMaker
- 📄 XGBoost.ipynb

<br>

## 🔧 Funcionalidades
- Inferência em tempo real para novas reservas de hotéis através da API.
- Integração completa com serviços **AWS** para processamento e armazenamento.
- Treinamento contínuo do modelo com base em novos dados armazenados no banco de dados **RDS**.

<br>

## 🚀 Deployment
- A **API** é executada em containers **Docker** e hospedada publicamente no **AWS EC2**.
- O modelo de **Machine Learning** é armazenado no **AWS S3** com acesso restrito.

<br>

## ⚙️ Requisitos

### 🛠️ Técnicos
- **Python 3.9+**: Necessário para executar a API localmente.
- **Docker**: Para containerizar e implantar a API.
- **Credenciais AWS**: Necessárias para acessar e configurar os serviços **S3**, **RDS**, **SageMaker**.
- **AWS CLI**: Configurada para interagir com os serviços da AWS.
- **.env**: Definição de variáveis de ambiente para fornecimento das credenciais AWS.

### .env mock

```dotenv
AWS_ACCESS_KEY_ID=[SUA_CHAVE_DE_ACESSO]
AWS_SECRET_ACCESS_KEY=[SUA_CHAVE_SECRETA_DE_ACESSO]
SESSION_TOKEN=[SEU_TOKEN_DE_SESSAO]
REGION=[SUA_REGIAO_DA_AWS]
```

### 🖥️ Cliente Final
- Acesso à internet para consumir a API hospedada no **AWS EC2**.
- Conhecimento básico sobre como fazer chamadas HTTP (via Postman ou outro meio de acesso).

### 💰 Custos
- **AWS EC2**: Custos pela instância selecionada, tempo de uso, armazenamento e transferência de dados.
- **AWS S3**: Custos baseados no volume de armazenamento e na quantidade de dados transferidos.
- **AWS RDS**: Custos da instância de banco de dados, incluindo armazenamento e operações realizadas.
- **AWS SageMaker**: Custos associados ao treinamento, inferência do modelo de **Machine Learning** e armazenamento do modelo.

<br>

## 🔑 Acesso
- URL da API: http://98.82.230.43:80/api/v1/inference
- [Saiba mais aqui](http://98.82.230.43:80/docs)

### 🚀 **Consumindo API**
- Exemplo de envio de dados para o endpoint:
```
{
  "no_of_adults": 2,
  "no_of_children": 1,
  "no_of_weekend_nights": 2,
  "no_of_week_nights": 3,
  "type_of_meal_plan": 1,
  "required_car_parking_space": 0,
  "room_type_reserved": 3,
  "lead_time": 45,
  "arrival_year": 2024,
  "arrival_month": 9,
  "arrival_date": 15,
  "market_segment_type": "Online",
  "repeated_guest": 0,
  "no_of_previous_cancellations": 1,
  "no_of_previous_bookings_not_canceled": 2,
  "no_of_special_requests": 3,
  "booking_status": "Confirmed"
}
```

<br>

## 💼 **Cargos**

👨‍💼 **Carlos Y. B. Vieira:**  
- ![Scrum Master](https://img.shields.io/badge/Scrum%20Master-00CC5C?style=plastic&logo=codeproject&logoColor=white)
- ![Engenheiro de Cloud](https://img.shields.io/badge/Engenheiro%20de%20Cloud-FF7401?style=plastic&logo=amazon&logoColor=white)  

👨‍💼 **Gabriel M. Santos:**  
- ![Banco de Dados](https://img.shields.io/badge/Banco%20de%20Dados-0068DA?style=plastic&logo=mysql&logoColor=white)
- ![Analista de Dados](https://img.shields.io/badge/Analista%20de%20Dados-7F7F7F?style=plastic&logo=databricks&logoColor=white)
- ![Suporte](https://img.shields.io/badge/Suporte-00C8B5?style=plastic&logo=imessage&logoColor=white)

👨‍💼 **Gustavo Gutierrez:**  
- ![Desenvolvedor API](https://img.shields.io/badge/Desenvolvedor%20API-8A2BE2?style=plastic&logo=fastapi&logoColor=white)
- ![Engenheiro de Machine Learning](https://img.shields.io/badge/Engenheiro%20de%20Machine%20Learning-00C7F6?style=plastic&logo=tensorflow&logoColor=white)
- ![Engenheiro de Cloud](https://img.shields.io/badge/Engenheiro%20de%20Cloud-FF7401?style=plastic&logo=amazon&logoColor=white) 

👨‍💼 **Lucas G. Teodoro:**  
- ![Engenheiro de DevOps](https://img.shields.io/badge/Engenheiro%20de%20DevOps-FF5C5C?style=plastic&logo=amazon&logoColor=white)
- ![Consultor de DevOps](https://img.shields.io/badge/Consultor%20de%20DevOps-FF8000?style=plastic&logo=amazon&logoColor=white)
- ![Arquiteto de Soluções](https://img.shields.io/badge/Arquiteto%20de%20Soluções-009900?style=plastic&logo=amazon&logoColor=white)

<br>

## 👥 Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/CarlosYanBezerraVieira">
        <img src="https://avatars.githubusercontent.com/u/80974859?v=4" width="100px;" alt="Colaborador Carlos"/><br>
        <sub>
          <b>Carlos Y. B. Vieira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gabrielsantos578">
        <img src="https://avatars.githubusercontent.com/u/127057846?v=4" width="100px;" alt="Colaborador Gabriel"/><br>
        <sub>
          <b>Gabriel M. Santos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Gustavo2022003">
        <img src="https://avatars.githubusercontent.com/u/54781049?v=4" width="100px;" alt="Colaborador Gustavo"/><br>
        <sub>
          <b>Gustavo Gutierrez</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LucasTeodoro1009">
        <img src="https://avatars.githubusercontent.com/u/152567868?v=4" width="100px;" alt="Colaborador Lucas"/><br>
        <sub>
          <b>Lucas G. Teodoro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<br>

## 📚 Aprendizado

### 🏆 Dificuldades Gerais
- **Integração dos serviços AWS**: Configuração e gerenciamento de múltiplos serviços AWS simultaneamente foi um desafio inicial.
- **Containerização com Docker**: Garantir que a API e o modelo de ML fossem devidamente configurados e funcionassem corretamente em containers foi um processo de aprendizado.

### 💡 Lições Aprendidas
- **Automação de Deploy**: A automação do processo de deploy e configuração do ambiente foi fundamental para a consistência e eficiência.
- **Escalabilidade com AWS**: A arquitetura baseada em serviços AWS permitiu uma escalabilidade flexível e adaptável às necessidades do projeto.
