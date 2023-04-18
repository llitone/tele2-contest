import sqlalchemy
from sqlalchemy import orm

from ..db_session import SqlAlchemyBase

__all__ = ("Question",)


class Question(SqlAlchemyBase):
    __tablename__ = 'questions'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    age = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    question = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    difficulty = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    value = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
    )
    subject_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("subjects.id")
    )
    explanation = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    subject = orm.relationship('Subject')

    def __str__(self):
        return "Question(id={0}, age={1}, question={2}, difficulty={3}, " \
               "value={4}, subject_id={5}, explanation={6})".format(
                    self.id, self.age, self.question, self.difficulty,
                    self.value, self.subject_id, self.explanation
                )
