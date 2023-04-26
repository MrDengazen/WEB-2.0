from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class CdelForm(FlaskForm):
    emty = StringField("  ")
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Примечания к сделке")
    typef = SelectField("Тип", choices=["Дом с землёй", "Квартира", "Комната", "Участок земли"])
    price = IntegerField("Цена")
    price_type = SelectField("Тип оплаты", choices=["Наличные", "Ипотека"])
    pr_fio = StringField("ФИО Продавца")
    po_fio = StringField("ФИО Покупателя")
    pr_data = DateField("Дата Рождения")
    po_data = DateField("Дата Рождения")
    pr_cer = IntegerField("Серия паспорта")
    pr_no = IntegerField("Номер паспорта")
    po_cer = IntegerField("Серия паспорта")
    po_no = IntegerField("Номер паспорта")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')