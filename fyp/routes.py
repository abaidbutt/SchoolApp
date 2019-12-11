from flask import render_template, redirect, url_for, request, flash, abort
from fyp import app, db, bcrypt
from fyp.forms import InsertForm, LoginForm, UpdateAccountForm
from fyp.models import User
from flask_login import login_user, current_user, logout_user, login_required

# def is_admin():
#     if current_user.email=='admin@blog.com':
#         return redirect(url_for('admin'))
#     else:
#         abort(401)



@app.route('/admin')
def admin():
    return render_template('admin.html', title='admin-panel')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    form=InsertForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password, profession=form.profession.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created!', 'success')
        return redirect(url_for('about'))
    return render_template('insert.html', title='Register', form=form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in ', 'success')
            return redirect(url_for('admin'))
        elif user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        current_user.password=form.password.data
        current_user.profession=form.profession.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
       
    return render_template('account.html', title='account', form=form)



@app.route('/about')
def about():
    users=User.query.all()
    return render_template('about.html', title='about', users=users)
@app.route('/about/stud')
def about_stud():
    users=User.query.filter_by(profession='student')
    return render_template('about.html', title='about', users=users)
@app.route('/about/tech')
def about_tech():
    users=User.query.filter_by(profession='teacher')
    
    return render_template('about.html', title='about', users=users)

@app.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user=User.query.first()
    if user.id==user_id:
        db.session.delete(user)
        db.session.commit()
        flash('Your user has been deleted', 'success')
        return redirect(url_for('admin'))
@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    form=InsertForm()
    user=User.query.get(user_id)
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        user.password=form.password.data
        user.profession=form.profession.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('about'))
    elif request.method == 'GET':
        form.username.data=user.username
        form.email.data=user.email
        form.profession.data=user.profession
        
    return render_template('edit_user.html', title='about', form=form)
    