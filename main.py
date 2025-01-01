from textSummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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