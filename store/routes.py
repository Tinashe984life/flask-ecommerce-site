from flask import render_template, redirect, url_for, flash, request, abort
from store import app, db, bcrypt
from store.forms import RegistrationForm, LoginForm
from store.models import User, Cart, Orders
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        return render_template('home.html', cartlength=cartlength)      
    else:
        return render_template('home.html', title='DILLIGAF - HOME')
    #return render_template('home.html', cartlength=cartlength)

@app.route('/footwear')
def footwear():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        return render_template('footwear.html', title='Footwear', cartlength=cartlength)
    else:
        return render_template('footwear.html', title='Footwear')

@app.route('/footwear/superstar', methods=['GET', 'POST'])
def superstar():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Adidas Superstar', description='Adidas Superstar - Black', price=700, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('superstar.html', cartlength=cartlength)
    else:
        return render_template('superstar.html')

@app.route('/footwear/nikesb1', methods=['GET', 'POST'])
def nikesb1():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Sb FC Classic', description='Black colorway', price=650, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('nikesb1.html', cartlength=cartlength)
    else:
        return render_template('nikesb1.html')

@app.route('/footwear/nikesb2', methods=['GET', 'POST'])
def nikesb2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Sb FC Classic', description='Light Grey', price=650, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('nikesb2.html', cartlength=cartlength)
    else:
        return render_template('nikesb2.html')

@app.route('/footwear/niketrainer', methods=['GET', 'POST'])
def niketrainer():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Trainer', description='Black & white Colorway', price=450, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('niketrainer.html', cartlength=cartlength)
    else:
        return render_template('niketrainer.html')

@app.route('/footwear/niketrainer2', methods=['GET', 'POST'])
def niketrainer2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Womens Trainer', description='Black & white Colorway', price=485, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('niketrainer2.html', cartlength=cartlength)
    else:
        return render_template('niketrainer2.html')

@app.route('/footwear/nikesb3', methods=['GET', 'POST'])
def nikesb3():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Sb Blazer', description='White colorway', price=745, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('nikesb3.html', cartlength=cartlength)
    else:
        return render_template('nikesb3.html')

@app.route('/footwear/nikesb4', methods=['GET', 'POST'])
def nikesb4():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Sb Dunk', description='Red, Pink & white colorway', price=895, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('nikesb4.html', cartlength=cartlength)
    else:
        return render_template('nikesb4.html')

@app.route('/footwear/nikesb5', methods=['GET', 'POST'])
def nikesb5():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nike Sb Womens Dunk', description='High Top, Pink, Brown Sole', price=955, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('nikesb5.html', cartlength=cartlength)
    else:
        return render_template('nikesb5.html')

@app.route('/footwear/dclynx1', methods=['GET', 'POST'])
def dclynx1():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='DC Lynx OG', description='OG Colorway, Grey + Navy', price=975, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('dclynx1.html', cartlength=cartlength)
    else:
        return render_template('dclynx1.html')

@app.route('/footwear/dclynx2', methods=['GET', 'POST'])
def dclynx2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='DC Lynx OG', description='OG Mist Colorway', price=975, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('dclynx2.html', cartlength=cartlength)
    else:
        return render_template('dclynx2.html')

@app.route('/footwear/dclynx3', methods=['GET', 'POST'])
def dclynx3():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='DC Lynx OG', description='OG Blue Mist Colorway', price=975, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('dclynx3.html', cartlength=cartlength)
    else:
        return render_template('dclynx3.html')

@app.route('/footwear/dclynx4', methods=['GET', 'POST'])
def dclynx4():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='DC Lynx OG', description='OG Peach Fuzz Colorway', price=975, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('footwear'))
        return render_template('dclynx4.html', cartlength=cartlength)
    else:
        return render_template('dclynx4.html')

@app.route('/men')
def men():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        return render_template('men.html', title='Men', cartlength=cartlength)
    else:
        return render_template('men.html', title='Men')

@app.route('/men/capetown', methods=['GET', 'POST'])
def capetown():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Cape Town Tee', description='Light Blue Printed Tee', price=160, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('capetown.html', cartlength=cartlength)
    else:
        return render_template('capetown.html')

@app.route('/men/capetown2', methods=['GET', 'POST'])
def capetown2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Cape Town Tee', description='Yellow Printed Tee', price=160, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('capetown2.html', cartlength=cartlength)
    else:
        return render_template('capetown2.html')

@app.route('/men/bronzeshirt1', methods=['GET', 'POST'])
def bronzeshirt1():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Bronze Tee', description='Logo Tee', price=250, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('bronzeshirt1.html', cartlength=cartlength)
    else:
        return render_template('bronzeshirt1.html')

@app.route('/men/bronzeshirt2', methods=['GET', 'POST'])
def bronzeshirt2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Bronze Tee', description='Puppies Print Tee', price=250, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('bronzeshirt2.html', cartlength=cartlength)
    else:
        return render_template('bronzeshirt2.html')

@app.route('/men/harleyshirt', methods=['GET', 'POST'])
def harleyshirt():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Harley Davidson Tee', description='Classic Logo Print', price=350, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('harleyshirt.html', cartlength=cartlength)
    else:
        return render_template('harleyshirt.html')

@app.route('/men/kiss', methods=['GET', 'POST'])
def kiss():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Kiss Band Tee', description='Summer 83 print', price=300, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('kiss.html', cartlength=cartlength)
    else:
        return render_template('kiss.html')

@app.route('/men/popsmoke', methods=['GET', 'POST'])
def popsmoke():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Pop Smoke Tee', description='Long Live The Woo print', price=345, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('popsmoke.html', cartlength=cartlength)
    else:
        return render_template('popsmoke.html')

@app.route('/men/retroplanet1', methods=['GET', 'POST'])
def retroplanet1():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Retro Planet Tee', description='Callahan Autoparts Print', price=360, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('retroplanet1.html', cartlength=cartlength)
    else:
        return render_template('retroplanet1.html')

@app.route('/men/retroplanet2', methods=['GET', 'POST'])
def retroplanet2():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Retro Planet Tee', description='Masters of the Universe Print', price=360, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('retroplanet2.html', cartlength=cartlength)
    else:
        return render_template('retroplanet2.html')

@app.route('/men/retroplanet3', methods=['GET', 'POST'])
def retroplanet3():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Retro Planet Tee', description='Columbus City Print', price=360, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('retroplanet3.html', cartlength=cartlength)
    else:
        return render_template('retroplanet3.html')

@app.route('/men/shelby', methods=['GET', 'POST'])
def shelby():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Shelby Racing Tee', description='Cobra Print', price=140, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('shelby.html', cartlength=cartlength)
    else:
        return render_template('shelby.html')

@app.route('/men/kc', methods=['GET', 'POST'])
def kc():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='KC Tee', description='Kansas City Print', price=160, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('kc.html', cartlength=cartlength)
    else:
        return render_template('kc.html')

@app.route('/men/kobe', methods=['GET', 'POST'])
def kobe():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Kobe Bryant Tee', description='Legend Print', price=400, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('kobe.html', cartlength=cartlength)
    else:
        return render_template('kobe.html')

@app.route('/men/nirvana', methods=['GET', 'POST'])
def nirvana():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Nirvana Band Tee', description='In Utero Print', price=400, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('nirvana.html', cartlength=cartlength)
    else:
        return render_template('nirvana.html')

@app.route('/men/photosynthesis', methods=['GET', 'POST'])
def photosynthesis():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Photosynthesis Tee', description='Photosynthesis is Fun Print', price=140, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('photosynthesis.html', cartlength=cartlength)
    else:
        return render_template('photosynthesis.html')

@app.route('/men/peace', methods=['GET', 'POST'])
def peace():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='3DaysOfPeace Tee', description='2010 Fest Print', price=140, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('3daysofpeace.html', cartlength=cartlength)
    else:
        return render_template('3daysofpeace.html')

@app.route('/men/wheaties', methods=['GET', 'POST'])
def wheaties():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Wheaties Football Tee', description='79 Nostalgia Print', price=140, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('wheaties.html', cartlength=cartlength)
    else:
        return render_template('wheaties.html')
        
@app.route('/men/sugar', methods=['GET', 'POST'])
def sugar():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='Sugar Daddy Tee', description='03 Vintage', price=140, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('sugar.html', cartlength=cartlength)
    else:
        return render_template('sugar.html')

@app.route('/men/flannel', methods=['GET', 'POST'])
def flannel():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='DG Flannel Tee', description='Brown DG Cotton', price=200, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('flannel.html', cartlength=cartlength)
    else:
        return render_template('flannel.html')

@app.route('/men/stones', methods=['GET', 'POST'])
def stones():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='The Stones Band Tee', description='92 Tour Print', price=340, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('stones.html', cartlength=cartlength)
    else:
        return render_template('stones.html')

@app.route('/men/who', methods=['GET', 'POST'])
def who():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        if request.method == 'POST':
            cart = Cart(name='The Who Band Tee', description='My Generation Print', price=340, user=current_user)
            db.session.add(cart)
            db.session.commit()
            flash('Item successfully added to Cart!', 'success')
            return redirect(url_for('tees'))
        return render_template('who.html', cartlenght=cartlength)
    else:
        return render_template('who.html')

@app.route('/tees')
def tees():
    if current_user.is_authenticated:
        cartlength = len(current_user.products)
        return render_template('tees.html', cartlength=cartlength)
    else:
        return render_template('tees.html', title='Tees')

@app.route('/women')
def women():
    return render_template('women.html')


@app.route('/cart')
@login_required
def cart():
    cartlength = len(current_user.products)
    items = current_user.products
    prices = []
    def addTotal():
        for i in items:
            prices.append(i.price)
        return prices    
    addTotal()
    total = sum(prices)
    return render_template('cart.html', items=items, cartlength=cartlength, total=total)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, cellphone=form.cellphone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account Has Been Successfully Created', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Incorrect email or password', 'danger')
    return render_template('login.html',form=form ,title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/deleteitem/<cart_id>', methods=['POST'])
def deleteitem(cart_id):
    trash = Cart.query.filter_by(id=cart_id).first()
    db.session.delete(trash)
    db.session.commit()
    flash('Item deleted!', 'success')
    return redirect(url_for('tees'))

@app.route('/account')
@login_required
def account():
    user_orders = current_user.checks
    return render_template('account.html', title='Account', user_orders=user_orders)     

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    items = current_user.products
    orders = []
    prices = []
    def addTotal():
        for i in items:
            prices.append(i.price)
        return prices
    
    def addOrders():
        orders.append(items)
        return orders

    addTotal()
    addOrders()
    
    total = sum(prices)

    c_out = Orders(items=str(orders), order_total=total, user=current_user)
    for x in items:
        trash_item = Cart.query.filter_by(user_id=current_user.id).first()
        db.session.delete(trash_item)
    db.session.add(c_out)
    
    db.session.commit()
    flash('Thank you for the purchase! Your order has been recieved!')
    return redirect(url_for('account'))
          
