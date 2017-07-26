from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from mainapp.models.tables import User


class UserCreateForm(Form):
    username = StringField("Usuário",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])
    name = StringField("Nome",
                       [
                           validators.Required(message="Preenchimento obrigatório"),
                           validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                       ])
    cpf = StringField("Cpf",
                      [
                      ])
    company = StringField("Company",
                          [
                              validators.Required(message="Preenchimento obrigatório"),
                              validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                          ])
    cnpj = StringField("Cnpj",
                       [
                       ])
    email = EmailField("E-mail",
                       [
                           validators.Required(message="Preenchimento obrigatório"),
                           validators.Email(message="Preenchimento inválido")
                       ])
    password = PasswordField("Senha",
                             [
                                 validators.Required(message="Preenchimento obrigatório"),
                                 validators.length(min=6, max=15, message="Mínimo de 6 e máximo de 15 caracteres")
                             ])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise validators.ValidationError("Usuário já cadastrado!")


class UserReadForm(Form):
    username = StringField("Usuário",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])


class OltCreateForm(Form):
    username = StringField("Username",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])
    name = StringField("Name",
                       [
                           validators.Required(message="Preenchimento obrigatório"),
                           validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                       ])
    cpf = StringField("Cpf",
                      [
                      ])
    company = StringField("Company",
                          [
                              validators.Required(message="Preenchimento obrigatório"),
                              validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                          ])
    cnpj = StringField("Cnpj",
                       [
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
    admin = StringField("Admin",
                        [
                        ])
    created_date = StringField("Create date",
                               [
                               ])


class LoginForm(Form):
    username = StringField("Usuário",
                           [
                               validators.Required(message="Preenchimento obrigatório"),
                               validators.length(min=4, max=25, message="Mínimo de 4 e máximo de 25 caracteres")
                           ])
    password = PasswordField("Senha",
                             [
                                 validators.Required(message="Preenchimento obrigatório"),
                                 validators.length(min=6, max=15, message="Mínimo de 6 e máximo de 15 caracteres")
                             ])
