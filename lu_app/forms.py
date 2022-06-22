from django.forms import Form, CharField


class AddPostForm(Form):

    title = CharField(label='Title', max_length=100)
    content = CharField(label='Content', max_length=4000)
