#!/bin/bash

# Установить начальное время как текущее время минус один месяц
declare -i startTime=$(date -d '-1 month' +%s)
# Установить конечное время как текущее время
declare -i endTime=$(date -d now +%s)

# Цикл выполняется, пока startTime меньше или равно endTime
while ((startTime <= endTime)); do
  # Установить конец интервала как startTime плюс один час
  declare -i intervalEnd=$((startTime + 60*60))
  # Преобразовать startTime и intervalEnd в формат ISO 8601
  declare startTimeIso="$(date -d @$startTime +%FT%T)"
  declare intervalEndIso="$(date -d @$intervalEnd +%FT%T)"

  # Создать URL для запроса к API
  declare url="https://api.hh.ru/vacancies?per_page=100&page=$i&date_from=$startTimeIso&date_to=$intervalEndIso"

  # Выполнить запрос к API (например, с использованием curl)
  echo "Fetching data from: $url"  # Добавлено для вывода URL
  
  # Обновить startTime для следующей итерации
  startTime=$intervalEnd
done
