import os 
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime 

LONDON_COORDINATES = {"latitude": 51.5074, "longitude": -0.1278} 
BIRMINGHAM_COORDINATES = {"latitude": 52.4862, "longitude": -1.8904}  

#Calculate movement increments
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude'] - LONDON_COORDINATES["latitude"] / 100)
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude'] / 100)

#Environment Variables for configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC','vehicle_topic')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_topic')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_topic')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_topic')

start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()

def simulate_journey():



if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers' : KAFKA_BOOTSTRAP_SERVERS,
        'error_cb' : lambda err: print(f'Kafka serror: {err}')
    }
    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Vehicle-CodeWithYu-123')

    except KeyboardInterrupt:
        print('Simulation ended by the user')
    except Exception as e:
        print(f'Unexpected Error ocurred: {e}')