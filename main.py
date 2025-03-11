from flask import Flask, render_template, redirect
from data import db_session
from data.news import News
from data.users import User
from forms.RegisterForm import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_keyaetjmhfjxdftryjdftgyhjrestyjdghjestykjdct512!T'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# def test_add_user():
#     user = User(name='Kowlad', about='Test2', email='test@mail.com')
#     db_sess = db_session.create_session()
#     db_sess.add(user)
#     db_sess.commit()


def main():
    db_session.global_init("db/blogs.db")
    # news = News(title="Dnjhfw35w3456354z но24524524вость", content="Привет блоwrtgfwrt3w4t!",
    #             user_id=2, is_private=True)
    # db_sess = db_session.create_session()
    # db_sess.add(news)
    # db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
