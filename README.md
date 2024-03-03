### Автоматическое добавление ссылки на задачу в описание коммита

Получает из названия ветки номер задачи (KANN-111, NORN-111, WEBDEV-1111) и вставляет (если его нет) в описание коммита.

Если в названии ветки нет указания задачи, то ничего не добавляет.

Например, из ветки `feature/WEBDEV-1111` в начало коммита будет добавлена ссылка на задачу `WEBDEV-1111: Ваше описание коммита`.

### Разработка

Адаптировано под VSCode и Docker. 

- python 3.9
- pytest
- autopep8
- mypy
- flake8

### Установка

1. Скопировать файл samples/prepare-commit-msg в .git/hooks
2. В случае необходимости поменять путь к python (указать полный или прописать в env)

#### Windows

1. должен быть с переносами crlf (учтено в samples)
2. перед вызовом команды установлен PYTHONIOENCODING=utf-8
3. в path прописан python