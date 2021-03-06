# ๐์ฅ๊ณ  ๋ฆฌ๋ง์ธ๋ ๋ฐ ์ค์ต

#### Django ์ค์น

```java
python -m pip install Django
```

------

#### Django ํ๋ก์ ํธ ์์

> django๋ test์ ๊ฐ์ ํ๋ก์ ํธ ์ด๋ฆ์ ํผํ๋ ๊ฒ์ด ์ข๋ค

```python
django-admin startproject <ํ๋ก์ ํธ์ด๋ฆ>
# ์๋๋ ๊ฒฝ์ฐ
python -m django startproject <ํ๋ก์ ํธ์ด๋ฆ>
```

---

#### ๊ฐ์ํ๊ฒฝ ์ค์  ๋ฐ ํ์ ํจํค์ง ์ค์น ๋ฐ requirements.txt ์์ฑ

```python
python -m venv venv

source ./venv/Scripts/activate
# ๋๋ ctrl + shift + p๋ก Select Interpretor ํ ๊ฐ์ํ๊ฒฝ์ python.exe ํ์ผ์ ์ฐพ์ ์ ํ
# ๊ฐ์ํ๊ฒฝ์๋ Django๊ฐ ์์ผ๋ฏ๋ก ์ค์นํด์ฃผ์ด์ผ ํ๋ค + ์ฃผ๋ก ์ฌ์ฉํ๋ ํจํค์ง๋ค
pip install Django black mysqlclient djangorestframework django-cors-headers djangorestframework-simplejwt
```

---

#### ํ๋ก์ ํธ ์ค์ 

>  ํ๋ก์ ํธ๋ฅผ ์์ฑํ๋ฉด ๊ธฐ๋ณธ์ ์ผ๋ก ํ๋ก์ ํธ๋ฅผ ์์ํ๊ธฐ ์ ์ ๋ง์ด๊ทธ๋ ์ด์์ ํด์ผํ๋ค. ๋ง์ฝ DB๋ฅผ ๋ณ๊ฒฝํ๊ณ  ์ถ๋ค๋ฉด migrate๋ฅผ ํ๊ธฐ ์ ์ ๋ณ๊ฒฝํ๋ ๊ฒ์ด ์ข๋ค. makemigrations์ ์ด๊ธฐํ๋ฅผ ํ๊ณ ์ถ๋ค๋ฉด migration ๊ด๋ จ ํ์ผ์ ์ญ์ ํด์ผํ๋ค. ์ด ๋ pycache์ ๋ค๋ฅธ ํ์ผ๋ค์ ์ญ์ ํ์ง ์๋๋ก ์ฃผ์ํ๋ค. ์ญ์ ๋ __pycacheํ์ผ์ python manage.py runserver๋ฅผ ํ๋ฉด ๋ค์ ์์ฑ๋๋ค.

```python
python manage.py migrate
```

#### settings.py

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



---

#### DB ์ฐ๊ฒฐ

##### mysqlclient ์ค์น

```py
pip install mysqlclient
```



> HOST๊ฐ ๊ฐ์ฅ ์ค์ํ๋ฐ, ๋ก์ปฌ์์ ์ปจํ์ด๋์ ์ฐ๊ฒฐํ  ๋๋ localhost, 
>
> ์ปจํ์ด๋๊ฐ ์ฐ๊ฒฐํ  ๋๋ ์ปจํ์ด๋ ์ด๋ฆ ๋๋ 127.0.0.1์ ์ฌ์ฉํ๋ฉด ๋๋ค.

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

