from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.config_entity import DataValidationConfig, DataTransformationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from sensor.entity.config_entity import ModelTrainerConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.exception import SensorException
import sys
from sensor.logger import logging


class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Data Ingestion Started")
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion Completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)
        
    
    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            logging.info("Data Validation Started")
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"Data Validation Completed")
            return data_validation_artifact
        except Exception as e:
            raise SensorException(e, sys)
        
    
    def start_data_transformation(self, data_validation_artifact:DataValidationArtifact):
        try:
            logging.info("Data Transformation Started")
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                     data_transformation_config=data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("Data Transformation Completed")
            return data_transformation_artifact
            
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_model_trainer(self, data_transformation_artfact:DataTransformationArtifact):
        try:
            logging.info("Model trainer started")
            model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,
                                         data_transformation_artifact=data_transformation_artfact)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("Model trainer completed")
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e, sys)
        

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        

    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact:DataValidationArtifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact:DataTransformationArtifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact:ModelTrainerArtifact = self.start_model_trainer(data_transformation_artfact=data_transformation_artifact) 
        except Exception as e:
            raise SensorException(e, sys)