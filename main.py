from textSummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummariser.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummariser.logging import Logger

STAGE_NAME = 'Data Ingestion stage'
try:
    Logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    Logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX================X")
except Exception as e:
    Logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation stage'
try:
    Logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    Logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX================X")
except Exception as e:
    Logger.exception(e)
    raise e