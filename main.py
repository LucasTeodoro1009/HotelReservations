import tarfile
import boto3
import xgboost as xgb
import os
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv, find_dotenv
from models import dataModels

# Inicializa o FastAPI
app = FastAPI(
    title="Hotel Reservation Prediction API",
    description="API para prever o status de reservas de hotel usando um modelo XGBoost treinado.",
    version="1.0.0"
)

# Inicializa o dotenv
load_dotenv(find_dotenv(), override=True)

# Configurações do S3 e carregamento do modelo
bucket_name = 'sprint4-5'
model_key = 'modelos/hotel_reservation/XGBoost/output/sagemaker-xgboost-2024-09-16-00-18-36-300/output/model.tar.gz'

def load_model_from_s3():
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('REGION'),
        aws_session_token=os.getenv('SESSION_TOKEN'))
    
    s3 = session.client('s3')
    
    # Baixa o arquivo do modelo
    s3.download_file(bucket_name, model_key, 'model.tar.gz')

    # Extrai o arquivo .tar.gz
    with tarfile.open('model.tar.gz', 'r:gz') as tar:
        tar.extractall(path='.')

    model = xgb.Booster()
    model.load_model('./xgboost-model')

    return model

# Carrega o modelo ao iniciar o aplicativo
model = load_model_from_s3()

# Mapeamentos de variáveis categóricas
market_segment_mapping = {
    'Online': 0,
    'Offline': 1,
    'Corporate': 2,
    'Others': 3
}

booking_status_mapping = {
    'Confirmed': 0,
    'Canceled': 1,
    'Pending': 2
}

@app.post("/api/v1/inference", response_model=dataModels.InferenceResponse, summary="Realiza inferência sobre uma reserva de hotel")
async def inference(request: dataModels.InferenceRequest):
    """
    Realiza uma inferência com base nos dados fornecidos na solicitação.

    Converte as variáveis categóricas em valores numéricos e prepara os dados 
    para o modelo XGBoost. Realiza a previsão e retorna o resultado.

    - **no_of_adults**: Número de adultos na reserva.
    - **no_of_children**: Número de crianças na reserva.
    - **no_of_weekend_nights**: Número de noites de fim de semana.
    - **no_of_week_nights**: Número de noites durante a semana.
    - **type_of_meal_plan**: Tipo de plano de refeições (representado como inteiro).
    - **required_car_parking_space**: Espaço de estacionamento necessário (representado como inteiro).
    - **room_type_reserved**: Tipo de quarto reservado (representado como inteiro).
    - **lead_time**: Tempo de antecedência da reserva em dias.
    - **arrival_year**: Ano de chegada.
    - **arrival_month**: Mês de chegada.
    - **arrival_date**: Dia de chegada.
    - **market_segment_type**: Tipo de segmento de mercado (ex: 'Online', 'Offline').
    - **repeated_guest**: Indica se o hóspede é repetido (0 ou 1).
    - **no_of_previous_cancellations**: Número de cancelamentos anteriores.
    - **no_of_previous_bookings_not_canceled**: Número de reservas anteriores que não foram canceladas.
    - **no_of_special_requests**: Número de solicitações especiais.
    - **booking_status**: Status da reserva (ex: 'Confirmed', 'Canceled').

    Retorna:
    - **result**: Resultado da previsão. O valor pode representar diferentes categorias ou classificações dependendo do treinamento do modelo.

    - **Exemplo de resposta:**
    
    ```json
    {
        "result": 1.0
    }
    ```
    """
    try:
        # Converte as variáveis categóricas em dummies
        market_segment = market_segment_mapping.get(request.market_segment_type, 0)  # Default para 'Online'
        booking_status = booking_status_mapping.get(request.booking_status, 0)  # Default para 'Confirmed'

        # Converte os dados da solicitação em um formato adequado para o modelo
        features = [
            request.no_of_adults,
            request.no_of_children,
            request.no_of_weekend_nights,
            request.no_of_week_nights,
            request.type_of_meal_plan,
            request.required_car_parking_space,
            request.room_type_reserved,
            request.lead_time,
            request.arrival_year,
            request.arrival_month,
            request.arrival_date,
            market_segment,
            request.repeated_guest,
            request.no_of_previous_cancellations,
            request.no_of_previous_bookings_not_canceled,
            request.no_of_special_requests,
            booking_status
        ]
        
        data = np.array([features])
        
        # Realiza a previsão
        dmatrix = xgb.DMatrix(data)
        predictions = model.predict(dmatrix)

        # Retorna a previsão
        return dataModels.InferenceResponse(result=float(predictions[0]))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
