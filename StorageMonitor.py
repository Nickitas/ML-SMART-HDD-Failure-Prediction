from DataCollector import DataCollector 
from MachineLearningModel import MachineLearningModel


class StorageMonitor:
    def __init__(self):
        self.model = None
        self.data_collector = DataCollector()

    def train_model(self, training_data):
        # Обучение модели на основе предоставленных данных
        self.model = MachineLearningModel()
        self.model.train(training_data)

    def predict_state(self, new_data):
        # Прогнозирование состояния накопителя на основе новых данных
        if self.model is not None:
            return self.model.predict(new_data)
        else:
            raise Exception("Модель не обучена")

    def collect_data(self):
        # Сбор данных с устройств
        return self.data_collector.collect()