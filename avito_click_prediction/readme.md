# Участвую в kaggle competition [Avito Context Ad Clicks](https://www.kaggle.com/c/avito-context-ad-clicks)

## Работа состоит из следующих этапов:
- Загрузка и разархивация данных из kaggle и помещение их на hdfs
- Формирование датасета для обучения с помощью spark.sql
- Перевод данных в Vowpal Wabbit кодировку
- Обучение Vowpal Wabbit логистической регрессии (таргет - предсказание клика по контекстной рекламе)
- Подсчет метрик качества
- kaggle submit

[notebook лежит тут](https://github.com/Blausher/show/blob/main/avito_click_prediction/click_prediction_notebook.ipynb)

## Как устроены данные в соревновании:
<p align="center">
  <img src="https://storage.googleapis.com/kaggle-media/competitions/kaggle/4438/media/DB_schema.png" width="50%"/>
</p>
