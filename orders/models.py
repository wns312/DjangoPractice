from django.db import models

# Create your models here.
class Order(models.Model):
    # 선택 필드 : 선택 필드 변수와 배열은 class 내부에 작성하는 것이
    # 클래스를 import해 사용할 때 편하다. 클래스를 import하면 선택자도 같이 import 되기 때문
    ORDER = "ORDER"
    CANCEL = "CANCEL"

    ORDER_STATUS = [
        (ORDER, "Order"),
        (CANCEL, "Cancel"),
    ]
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default=ORDER)

    # models.ForeignKey() -> 멤버

    # 중개 테이블 작성해서 필드 연결 해보기
    # order = models.ForeignKey()

    # 클래스, 테이블에 대한 각종 정보를 지정하는 하위클래스
    # https://docs.djangoproject.com/ko/3.2/ref/models/options/#table-names
    class Meta:
        managed = True  # 데이터베이스에 테이블을 자동 생성할지에 대한 옵션으로 기본값은 True이다
        db_table = "orders"
