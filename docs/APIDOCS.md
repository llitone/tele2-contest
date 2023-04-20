<h1 align="center">API</h1>


# v1.0
## 1. Обзор

API для связи клиента и сервера

## 1.1 Users

### POST
#### Пример запроса в формате json
```python
{
    "name": {name}, 
    "age": {age}, 
    "phone_number": {phone_number}, 
    "password": {password}, 
    "points": {points}
}
```
`name` - 
`age` - 
`naphone_number` - 
`password` - 
`points` - 

#### Пример запроса
```python
import requests

json = {
    "name": {name}, 
    "age": {age}, 
    "phone_number": {phone_number}, 
    "password": {password}, 
    "points": {points}
}

requests.post("http://{host}/app/api/v1.0/users/", json=json)
```

`name` - 1<br>
`age` - 1<br>
`phone_number` - 1<br>
`password` - 1<br>
`points` - 1<br>


#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/users/<phone>")
```
#### Ответ
```python
{
    "id": {id},
    "name": {name},
    "age": {age},
    "phone_number": {phone_number},
    "password": {password},
    "points": {points}
}
```

## 1.2 Answers

### POST
#### Пример запроса в формате json
```python
{
    "question_id": {question_id}, 
    "answer": {answer}, 
    "is_correct": {is_correct}
}
```
#### Пример запроса
```python
import requests

json = {
    "question_id": {question_id}, 
    "answer": {answer}, 
    "is_correct": {is_correct}
}

requests.post("http://{host}/app/api/v1.0/answers/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET

#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/answers/<int:question_id>")
```
#### Ответ
```python
{
    "id": {id},
    "question_id": {question_id},
    "answer": {answer},
    "is_correct": {is_correct}
}
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/answers/<int:question_id>")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.3 Questions

### POST
#### Пример запроса в формате json
```python
{
    "age": {age}, 
    "question": {question}, 
    "difficulty": {difficulty}, 
    "value": {value},
    "subject_id": {subject_id}, 
    "explanation": {explanation}, 
    "author_id": {author_id}
}
```
#### Пример запроса
```python
import requests

json = {
    "age": {age}, 
    "question": {question}, 
    "difficulty": {difficulty}, 
    "value": {value},
    "subject_id": {subject_id}, 
    "explanation": {explanation}, 
    "author_id": {author_id}
}

requests.post("http://{host}/app/api/v1.0/questions/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса для одного question
```python
import requests

requests.get("http://{host}/app/api/v1.0/questions/<int:question_id>")
```
#### Ответ
```python
{
    "id": {id},
    "age": {age},
    "question": {question},
    "difficulty": {difficulty},
    "value": {value},
    "subject_id": {subject_id},
    "explanation": {explanation}, 
    "author_id": {author_id}
}
```
#### Пример запроса для всех questions
```python
import requests

requests.get("http://{host}/app/api/v1.0/questions/")
```
#### Ответ
```python
[
    {
        "id": {subject_id},
        "subject": {subject_subject},
        "questions": [
            {
                "age": {question_age},
                "author_id": {question_author_id},
                "difficulty": {question_difficulty},
                "explanation": {question_explanation},
                "id": {question_id},
                "question": {question_question},
                "subject_id": {question_subject_id},
                "value": {question_value},
                "answers": [
                    {
                        "answer": {answer_answer},
                        "id": {answer_id},
                        "is_correct": {answer_is_correct},
                        "question_id": {answer_question_id}
                    }
                ]
            }
        ]
    }
]
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/questions/<int:question_id>")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.4 Subjects

### POST
#### Пример запроса в формате json
```python
{
    "name": {name}
}
```
#### Пример запроса
```python
import requests

json = {
    "name": {name}
}

requests.post("http://{host}/app/api/v1.0/subjects/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса для всех subjects
```python
import requests

requests.get("http://{host}/app/api/v1.0/subjects/")
```
#### Ответ
```python
[
    {
        "id": {id},
        "subject": {subject}
    }
]
```
#### Пример запроса для одного subject
```python
import requests

requests.get("http://{host}/app/api/v1.0/subjects/<name>")
```
#### Ответ
```python
{
    "id": {id},
    "subject": {subject}
}
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/subjects/<name>")
```

#### Ответ
```python
{
    "success": True
}
```
## 1.5 Quizzes

### POST
#### Пример запроса в формате json
```python
{
    "room_id": {room_id}
}
```
#### Пример запроса
```python
import requests

json = {
    "room_id": {room_id}
}

requests.post("http://{host}/app/api/v1.0/quizzes/", json=json)
```

#### Ответ
```python
{
    "success": True
}
```
### GET
#### Пример запроса
```python
import requests

requests.get("http://{host}/app/api/v1.0/quizzes/<int:room_id>")
```
#### Ответ
```python
{
    "id": {id}, 
    "room_id": {room_id}, 
    "start_at": {start_at}
    }
```
### DELETE
#### Пример запроса
```python
import requests

requests.delete("http://{host}/app/api/v1.0/quizzes/<int:room_id>")
```

#### Ответ
```python
{
    "success": True
}
```