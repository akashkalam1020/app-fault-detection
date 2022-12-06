from sensor.logger import logging
from sensor.exception import SensorException
import sys, os
from sensor.entity import config_entity

if __name__=="__main__":
    try:
        TrainingPipelineConfig = config_entity.TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config = training_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)