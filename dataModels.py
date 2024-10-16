from pydantic import BaseModel

class inferenceRequest(BaseModel):
    """
    Modelo de dados para a solicitação de inferência.

    Representa os dados necessários para realizar uma inferência com o modelo XGBoost.

    Attributes:
        no_of_adults (int): Número de adultos na reserva.
        no_of_children (int): Número de crianças na reserva.
        no_of_weekend_nights (int): Número de noites de fim de semana.
        no_of_week_nights (int): Número de noites durante a semana.
        type_of_meal_plan (int): Tipo de plano de refeições (representado como inteiro).
        required_car_parking_space (int): Espaço de estacionamento necessário (representado como inteiro).
        room_type_reserved (int): Tipo de quarto reservado (representado como inteiro).
        lead_time (int): Tempo de antecedência da reserva em dias.
        arrival_year (int): Ano de chegada.
        arrival_month (int): Mês de chegada.
        arrival_date (int): Dia de chegada.
        market_segment_type (str): Tipo de segmento de mercado (ex: 'Online', 'Offline').
        repeated_guest (int): Indica se o hóspede é repetido (0 ou 1).
        no_of_previous_cancellations (int): Número de cancelamentos anteriores.
        no_of_previous_bookings_not_canceled (int): Número de reservas anteriores que não foram canceladas.
        no_of_special_requests (int): Número de solicitações especiais.
        booking_status (str): Status da reserva (ex: 'Confirmed', 'Canceled').
    """
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    type_of_meal_plan: int
    required_car_parking_space: int
    room_type_reserved: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    market_segment_type: str
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    no_of_special_requests: int
    booking_status: str

class inferenceResponse(BaseModel):
    """
    Modelo de resposta para a inferência.

    Representa o resultado da previsão feita pelo modelo XGBoost.

    Attributes:
        result (float): Resultado da previsão.
    """
    result: float
