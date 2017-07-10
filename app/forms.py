from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class UserCreateForm(Form):
    username = StringField("Username",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])
    email = EmailField("E-mail",
                       [
                           validators.Required(message="Preenchimento obrigatório"),
                           validators.Email(message="Preenchimento inválido")
                       ])
    password = PasswordField("Password",
                             [
                                 validators.Required(message="Preenchimento obrigatório"),
                                 validators.length(min=6, max=15, message="Mínimo de 6 e máximo de 15 caracteres")
                             ])


class LoginForm(Form):
    username = StringField("Username",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])
    password = PasswordField("Password",
                             [
                                 validators.Required(message="Preenchimento obrigatório"),
                                 validators.length(min=6, max=15, message="Mínimo de 6 e máximo de 15 caracteres")
                             ])
