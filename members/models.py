from django.db import models
from project.base_models import Base, Address, CreatedUpdatedAt


# 테이블 자동 생성 시 테이블 이름은 <app 이름>_<모델이름>이 된다 : members_member
class Member(Base, Address, CreatedUpdatedAt):
    # PK는 Bigint AutoIncrement로 자동 생성됨
    name = models.CharField(max_length=50)

    # 중개 테이블 작성해서 필드 연결 해보기
    # order = models.ForeignKey()
    class Meta:
        managed = True  # 데이터베이스에 테이블을 자동 생성할지에 대한 옵션으로 기본값은 True이다
        db_table = "member"  # 데이터베이스에 저장될 테이블 이름

    def __str__(self):
        string = (
            f"Member(name={self.name}, city={self.city}, street={self.street},"
            + f"zipcode={self.zipcode}, created_at={self.created_at}, updated_at={self.updated_at})"
        )
        return string
