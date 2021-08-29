from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm
# Форма добавления нового поста
class CreatePostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    subtitle = StringField("Подзаголовок", validators=[DataRequired()])
    img_url = StringField("Ссылка на картинку", validators=[DataRequired(), URL()])
    body = CKEditorField("Текст поста", validators=[DataRequired()])
    submit = SubmitField("Подтвердить")


# Форма регистрации нового пользователя    
class RegisterForm(FlaskForm):
    email = StringField("Адрес эл. почты", validators=[Email(), DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


# Форма авторизации    
class LoginForm(FlaskForm):
    email = StringField("Адрес эл. почты", validators=[Email(), DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")


# Форма комментария    
class CommentForm(FlaskForm):
    comment = CKEditorField("Комментарий", validators=[DataRequired()])
    submit = SubmitField("Отправить")
