#! /usr/bin/env python
# -*- coding: utf-8 -*

from wtforms import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import DateField
from wtforms import validators

class SignUpForm(Form):
  username = TextField('Username', [validators.Length(min=4, max=50)])
  real_name = TextField('Real name', [validators.Length(min=6)])
  password = PasswordField \
  (
    'Password',
    [
      validators.Required(),
      validators.EqualTo('confirm_password', message = 'Passwords must match.')
    ]
  )
  confirm_password = PasswordField('Retype password')
  email = TextField \
  (
    'E-mail address',
    [
      validators.Required(),
      validators.EqualTo('confirm_email', message = 'E-mails must match.')
    ]
  )
  confirm_email = TextField('Retype e-mail')

class LoginForm(Form):
  username = TextField('Username', [validators.Required()])
  password = PasswordField('Password', [validators.Required()])

class EditTaskForm(Form):
  assigned = SelectField('Assigned to')

  priority_choices = []
  for elem in ['High', 'Normal', 'Low']:
    priority_choices.append((elem, elem))
  priority = SelectField('Priority', choices = priority_choices)

  title = TextField('Title', [validators.Length(min=6)])
  text = TextAreaField('Description')
  tags = TextField('Tags')

  status_choices = []
  for elem in ['New', 'Work in progress', 'Done', 'Closed']:
    status_choices.append((elem, elem))
  status = SelectField('Status', choices = status_choices)

  project = SelectField('Project')

  due_date = DateField('Due date', format = '%d.%m.%Y')

class EditProjectForm(Form):
  author = TextField('Author')
  title = TextField('Title')
  start_date = DateField('Start date', format = '%d.%m.%Y')
  due_date = DateField('Due date', format = '%d.%m.%Y')
  text = TextAreaField('Description')

class CommentForm(Form):
  text = TextAreaField('Text', [validators.Length(min=2)])
