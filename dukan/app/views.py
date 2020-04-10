"""
Definition of views.
"""

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.utils import timezone
from django.views.generic import ListView
from .models import register
import sqlite3, os, json
from PIL import Image
from twilio.rest import Client

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request, customer_name=''):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'name' : customer_name
        }
    )
def get_all_users( json_str = False ):
    conn = sqlite3.connect('shops.db')
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    db = conn.cursor()

    rows = db.execute('''
    SELECT * from register
    ''').fetchall()

    conn.commit()
    conn.close()

    #if json_str:
    #    return json.dumps( [dict(ix) for ix in rows], indent=2) #CREATE JSON

    return [dict(ix) for ix in rows]

def about(request,customer_name='vsvai'):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    conn = sqlite3.connect('shops.db')
    cur = conn.cursor()
    cur.execute("select * from register")
    a = cur.fetchall()
    conn.commit()
    data = get_all_users(json_str = True)
    return render(
        request,
        'app/about.html',
        {
            'title': 'Shops',
            'all_shops' : data,
            'year': datetime.now().year,
            'customer_name': customer_name,
            'name' : customer_name
        }
    )

def logincust(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        user_name =request.POST['user_name']
        phone_no =request.POST['phone_no']
        if "login" in request.POST: 
            conn = sqlite3.connect('shops.db')
            cur = conn.cursor()
            cur.execute("SELECT user_name, phone_no FROM customer")
            a=cur.fetchall()
            conn.commit()
            for i in a:
                print(i)
                if i[0] == user_name:
                    if i[1] == int(phone_no):
                        print('login')
                        return redirect("about", user_name)
            else:
                conn = sqlite3.connect('shops.db')
                cur = conn.cursor()
                cur.execute("INSERT INTO customer VALUES(?,?)",(user_name,phone_no))
                conn.commit()
                print('not login')
                return redirect("about", user_name)
       
    else:
        return render(request,'app/logincust.html',{'title':'Customer Login', 'message':'login your account.','year':datetime.now().year})

   

def register(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST': #user want to signup
        conn = sqlite3.connect('shops.db')
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        shop_name =request.POST['shop_name']
        contact =request.POST['contact']
        store_type =request.POST['store_type']
        shop_no =request.POST['shop_no']
        city =request.POST['city']
        state =request.POST['state']
        locality =request.POST['locality']
        pincode =request.POST['pincode']
        date=timezone.datetime.now()
        #register.user = 'vsvai'
        cur = conn.cursor()
        cur.execute(f"INSERT INTO register VALUES (?,?,?,?,?,?,?,?,?,?,?)",(first_name, last_name, shop_name, contact, store_type, shop_no, city, state, locality, pincode, date))
        conn.commit()    
        #register1.save()
        return redirect('loginShop')
    else:
        return render(
            request,
            'app/register.html',
            {
                'title':'Register Customer',
                'message':'Create your account.',
                'year':datetime.now().year,
            }
        )

def loginShop(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        user_name =request.POST['user_name']
        password =request.POST['password']
        if 'login' in request.POST:
            conn = sqlite3.connect('shops.db')
            cur = conn.cursor()
            cur.execute("SELECT first_name, shop_name FROM register")
            a=cur.fetchall()
            conn.commit()
            for i in a:
                if i[0] == user_name:
                    if i[1] == password:
                        print('login')
                        return redirect("update", user_name)
                    else:
                        print('password incorrect')
                else:
                    print('wrong username')
    return render(
        request,
        'app/loginShop.html',
        {
            'title':'Login Shop',
            'message':'try again.',
            'year':datetime.now().year,
        }
    )

def detail(request, customer_name = ''):
    assert isinstance(request, HttpRequest)
    conn = sqlite3.connect('shops.db')
    cur = conn.cursor()
    cur.execute("select * from register")
    a = cur.fetchall()
    print(a)
    cur.execute(f"select * from bookings where shop_name='{shop_name}' and cust_name='{customer_name}'")
    b= cur.fetchall()
    print(b)
    conn.commit()
       
    return render(
        request,
        'app/contact.html',
        {
            'title':'Detail page',
            'message':'detail of this page given below',
            'year':datetime.now().year,
            'name' : customer_name,
            'booking' : b,
        }
    )

def update(request, shop_name = ''):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        conn = sqlite3.connect('shops.db')
        cur = conn.cursor()
        cur.execute(f"select * from register where first_name='{shop_name}'")
        a = cur.fetchall()[0]
        print(a)
        cur.execute(f"select * from bookings where shop_name='{shop_name}'")
        b= cur.fetchall()
        print(b)
        im = Image.open("vsvai.jpg").show()
        conn.commit()
        return render(
        request,
        'app/update.html',
        {
            'title':'Update page',
            'message':'u can edit detail of this page given below',
            'year':datetime.now().year,
            'name' : shop_name,
            'first_name' : a[0],
            'last_name' : a[1],

            'shop_name' : a[2],
            'contact' : a[3],
            'shop_no' : a[5],
            'city' : a[6],
            'state' : a[7],
            'locality' : a[8],
            'pincode' : a[9],
            'booking' : b,
            'image' : im


        }
    )

    if request.method=='POST':
        conn = sqlite3.connect('shops.db')
        if "submit" in request.POST:
            first_name =request.POST['first_name']
            last_name =request.POST['last_name']
            #shop_name =request.POST['shop_name']
            contact =request.POST['contact']      
            #store_type =request.POST['store_type']
            shop_no =request.POST['shop_no']
            city =request.POST['city']
            state =request.POST['state']
            locality =request.POST['locality']
            pincode =request.POST['pincode']
            date=timezone.datetime.now()
            #register.user = 'vsvai'
        cur = conn.cursor()

        cur.execute(f"UPDATE register SET last_name= ?, contact = ?, shop_no = ?, city = ?, state = ?, locality = ?, pincode = ? WHERE first_name = '{first_name}'",(last_name, contact, shop_no, city, state, locality, pincode))
        conn.commit()
        return redirect('about')
    
def photo(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/photo.html')
def book(request, customer_name):
    assert isinstance(request, HttpRequest)
    conn = sqlite3.connect('shops.db')
    cur = conn.cursor()
    cur.execute(f'SELECT phone_no FROM customer WHERE user_name="{ customer_name }"')
    data = cur.fetchall()
    print(data)
    customer_contact = data[0][0]
    shop_name = request.GET['shop_name']
    cur.execute(f'SELECT contact FROM register WHERE first_name="{ shop_name }"')
    shop_data=cur.fetchall()
    print(shop_data)
    shop_contact = shop_data[0][0]
    conn.commit()
    print(shop_contact)
    if request.method=='GET':
        conn.commit()
        return render(
            request,
            'app/book.html',
            {
                'title' : 'Another Detail page',
                'message' : 'Details of this page is hereby solemnly given below:',
                'year' : datetime.now().year,
                'customer_name' : customer_name,
                'customer_contact' : customer_contact,
                'shop_contact' : shop_contact,
                'shop_name' : shop_name,
                'name' : customer_name
            }
        )
    else:
        conn = sqlite3.connect('shops.db')
        cur = conn.cursor()
        text =request.POST['text']
        image = request.FILES['image']
        date=request.POST['date']
        hour=request.POST['time']
        minute=request.POST['minute']
        period=request.POST['period']
        cur = conn.cursor()
        im1 = Image.open(image)
        print(customer_contact,shop_contact)
        #a=user_name
        #-------------------------------
        account_sid = "AC813125d82e4ffc9caab2ef32d48a92e6"
        auth_token = "716fd100f4cc2e528a65928bb89cfa8f"
        client = Client(account_sid, auth_token)
        sms = client.messages.create(from_="+1 806 587 0221", body=f"YOUR ID::{customer_name},{customer_contact},SHOP DETAILS:: {shop_name},{shop_contact},YOUR ORDER:{text},TIME::{date}, {hour}, {minute} ,{period}", to="+919811208502",)
        print(sms.sid)
        #-------------------------------
        im1.save(customer_name + ".jpg")
        cur.execute( f"INSERT INTO bookings VALUES (?,?,?,?,?,?,?,?,?,?)",(customer_name,customer_contact,shop_name,shop_contact,text,customer_name, date, hour, minute ,period))
        conn.commit()
        return redirect('about', customer_name)
    