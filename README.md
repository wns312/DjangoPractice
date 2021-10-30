# 🍕장고 리마인드 및 실습

#### Django 설치

```java
python -m pip install Django
```

------

#### Django 프로젝트 시작

> django나 test와 같은 프로젝트 이름은 피하는 것이 좋다

```python
django-admin startproject <프로젝트이름>
# 안되는 경우
python -m django startproject <프로젝트이름>
```

---

#### 가상환경 설정 및 필요 패키지 설치 및 requirements.txt 생성

```python
python -m venv venv

source ./venv/Scripts/activate
# 또는 ctrl + shift + p로 Select Interpretor 후 가상환경의 python.exe 파일을 찾아 선택
# 가상환경에는 Django가 없으므로 설치해주어야 한다 + 주로 사용하는 패키지들
pip install Django black mysqlclient djangorestframework django-cors-headers djangorestframework-simplejwt
```

---

#### 프로젝트 설정

>  프로젝트를 생성하면 기본적으로 프로젝트를 시작하기 전에 마이그레이션을 해야한다. 만약 DB를 변경하고 싶다면 migrate를 하기 전에 변경하는 것이 좋다. makemigrations의 초기화를 하고싶다면 migration 관련 파일을 삭제해야한다. 이 때 pycache의 다른 파일들을 삭제하지 않도록 주의한다. 삭제된 __pycache파일은 python manage.py runserver를 하면 다시 생성된다.

```python
python manage.py migrate
```

#### settings.py

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



---

#### DB 연결

##### mysqlclient 설치

```py
pip install mysqlclient
```



> HOST가 가장 중요한데, 로컬에서 컨테이너에 연결할 때는 localhost, 
>
> 컨테이너간 연결할 때는 컨테이너 이름 또는 127.0.0.1을 사용하면 된다.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "testdb",
        "USER": "root",
        "PASSWORD": "jyk",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

