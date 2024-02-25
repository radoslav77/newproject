from calendar import month
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.http import JsonResponse
import csv
import json
import datetime 
from datetime import timedelta 
import datetime as dt
from django.utils.dateparse import parse_date
from django.templatetags.static import static



from .forms import *


# global variebles
time = datetime.datetime.now()
TODAY = time.strftime('%Y'+'-'+'%m'+'-'+'%d')
today = time.strftime('%d'+'/'+'%m'+'/'+'%Y')
ENTRY = Amenities_CSV.objects.all()
YearMounts = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
              '07': 'July', '08': 'Auguest', '09': 'September', '10': 'Octomber', '11': 'November', '12': 'December'}
#DATA_LONG_STAY = LongStay.objects.all()

FRUIT = ['Large fruit', 'Midium fruit','Small fruit','Presidential']
DRINK = ['White wine','Red wine','Champagne', 'Negroni', 'Water']
TURN_DOWN = { 'Monday':'Ginger Florentine',
                'Tuesday':'Vanilla Macaroons', 
                'Wednesday':'Pistachio Finnacier',
                'Thursday':'Lemon drizzle',
                'Friday':'Mini cooies',
                'Saturday':'Vanilla Madeleines',
                'Sunday' :'MIxed seeds and nuts Flapjack',
}
DESSERT = ['Chocolate truffle', 'Macaroons 4pcs', 'Macaroons 8pcs', 'Baklava', 'Maamul', 'Arab amenity']
CODE_AMENITY = {
	'VIP1': ('birthday cake', '' , ''),
	'VIP2': ('Chocolate box', '', ''),
	'VIP3': ('Small fruit bowl', 'florentine', ''),
	'VIP4': ('Medium fruit bowl', '4 macaroons', 'Red Wine'),
	'VIP5': ('Large fruit bowl', '6 macaroons', 'Premium Red Wine'),
	'VIP6': ('Presidential fruit bowl', '8 macaroons', 'Custom Amenities' ),
	'VIP4ME': ('Medium fruit bowl','dates', 'baklava'),
	'VIP3ME': ('Small fruit bowl', 'dates', ''),
	'VIP5ME': ('Large fruit bowl', 'Arabic Inspired Amenity', '')

}


# Create your views here.


# input of csdv file + spacial amenities
def index(request):
    if request.user.is_authenticated:
        user = request.user.username
      
        #print(time.strftime('%A'))
        #delete all entry of csv file model
        if request.method == 'POST':
        # name = request.POST['day']
            day_name = time.strftime('%A')
            amound = request.POST['amount']
            for k, v in TURN_DOWN.items():
                if day_name == k:
                    
                    data = Replenishment(amenity_replen=v,amount_day=amound,date_of_input=today)
                    data.save()
                    print(v)

        return render(request, 'calc/index.html', {
            'form': InputData(),
            'form1' : CSVFileForm(),
            'user':user
        })
    
    else:
        return render(request, 'calc/index.html', {
            'msg': 'You need to login!!!',
            
        })



def upload_csv(request):
    user = request.user.username
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file = CSVFile.objects.all()  
            print(file)  
 
            for entyr in file: 
                #print(entyr)
                #neeed to work on file path
                file1 = open(('media/'f'{entyr.file}'))
                
                #print(file1)      
                with open ('media/'f'{entyr.file}', 'r') as fi:
                    csvreader = csv.reader(fi)
                    for row in csvreader:
                        for cell in csvreader:
                            #print(row[0], row[1])
                            #print(cell[1], cell[2], cell[4], cell[13],cell[12])
                
                            data = Amenities_CSV(date= cell[1], 
                                    day_of_week=cell[2], amenity_code=cell[4],iventory=cell[13],
                                    reserved=cell[12])
                            print(data)
                            data.save()
                            
                            #file.delete()
                            #break from the loop if not integer 
                            data = CSVFile.objects.all()
                            print(data)

            data_input = Amenities_CSV.objects.all()
            for d in data_input:
                if '/' not in d.date:
                    d.delete()

            # Add additional processing logic if needed
            return render(request, 'calc/index.html', {
        'form': InputData(),
        'form1' : CSVFileForm(),
        'user':user
    })
            #return redirect('index')  # Redirect to a success page
    else:
        form = CSVFileForm()

    return render(request, 'calc/upload_csv.html', {'form': form})


def update_daily(request):

    DATE_OF_SUBMITION = Amenities_CSV.objects.filter(date_of_input=TODAY)
    entry = Amenities_CSV.objects.all()
    replenish = Replenishment.objects.filter(date_of_input=TODAY)
    special_data =[]
    reple = []
    # spaecial input amaenities need to conbaind them
    special_entry = Spacial_Amenities.objects.all()
    for s in special_entry:
        s_date = s.arrival_date.strftime('%d'+'/''%m'+'/'+'%Y')
        if s_date == today:
            special_data.append(s)
    #replenish.delete()
    for en in replenish:
        reple.append(en)   
        #print(s.arrival_date,'-',s_date)
    #print(special_data)
    
    # back to the original operation
    t = datetime.datetime.now() + timedelta(days=1)
    day_tomorrow = t.strftime('%d'+'/'+'%m'+'/'+'%Y')
    Data_for_today =[]
    Count = 0
    data_with_amenity = []
	
    for ent in entry:
       # print(ent.date,' --', today)
        if ent.date == today:
            for key, item in CODE_AMENITY.items():
                if ent.amenity_code == key:
                    Count = Count + 1
            #print(ent)
                    input_date = str(ent.date_of_input)
                    Data_for_today.append({
                    'arrival_date': ent.date,
                    'day_name': ent.day_of_week,
                    'amenity_code': ent.amenity_code,
                    'fruit_amenity': item[0],
                    'dessert_amenity': item[1],
                    'dessert_amenity1': item[2],
                    'iventory': ent.iventory,
                    'reserved': ent.reserved,
                    'input_date': input_date,
                    'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')
                    })

    data_view = []
    data12 = CSVFile.objects.all()
    for d in data12:
        data_view.append({'file': d.file,
                          'id': d.big_id})



    #print(Data_for_today,'-',data_with_amenity)
    #print(entry, '____---',DATE_OF_SUBMITION)
    return render(request, 'calc/today.html',{'data':Data_for_today,
                                              'code': CODE_AMENITY,
                                              'special':special_data,
                                              'today': today,
                                              'replenish': reple,
                                              'media': data_view})


def code_API(request):
    
    JSON_data = []

    for it in ENTRY:
        for key, item in CODE_AMENITY.items():
            if it.amenity_code == key:
               
                input_date = str(it.date_of_input),
                JSON_data.append({
                    'big_id': it.big_id,
                    'arrival_date': it.date,
                    'day_name': it.day_of_week,
                    'amenity_code': it.amenity_code,
                    'fruit_amenity': item[0],
                    'dessert_amenity': item[1],
                    'dessert_amenity1': item[2],
                    'iventory': it.iventory,
                    'reserved': it.reserved,
                    'input_date': input_date,
                    'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')
                    })

                #print(123)
                # if that is the key take this input an dgo update the filds with Fruit and dessert
                #print(key, '-', item)
                #print(type(item))
                #print(key)
    #print(JSON_data)
    return HttpResponse(json.dumps(JSON_data), content_type="application/json")


def tomorrow_amenities(request):
    
    
    entry = Amenities_CSV.objects.all()
    t = datetime.datetime.now() + timedelta(days=1)
    day_tomorrow = t.strftime('%d'+'/'+'%m'+'/'+'%Y')
    Data_for_tomorrow = []
    
    for ent in entry:
        if ent.date == day_tomorrow:
            for key, item in CODE_AMENITY.items():
                if ent.amenity_code == key:
                    #Count = Count + 1
            #print(ent)
                    input_date = str(ent.date_of_input)
                    Data_for_tomorrow.append({
                    'arrival_date': ent.date,
                    'day_name': ent.day_of_week,
                    'amenity_code': ent.amenity_code,
                    'fruit_amenity': item[0],
                    'dessert_amenity': item[1],
                    'dessert_amenity1': item[2],
                    'iventory': ent.iventory,
                    'reserved': ent.reserved,
                    'input_date': input_date,
                    'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')
                    })

    
    return render(request, 'calc/tomorrow.html',{'data':Data_for_tomorrow,
                                              'date': day_tomorrow})

def day_after(request):
    entry = Amenities_CSV.objects.all()
    t = datetime.datetime.now() + timedelta(days=2)
    day_after = t.strftime('%d'+'/'+'%m'+'/'+'%Y')
    Data_for_tomorrow = []
    
    for ent in entry:
        if ent.date == day_after:
            for key, item in CODE_AMENITY.items():
                if ent.amenity_code == key:
                    #Count = Count + 1
            #print(ent)
                    input_date = str(ent.date_of_input)
                    Data_for_tomorrow.append({
                    'arrival_date': ent.date,
                    'day_name': ent.day_of_week,
                    'amenity_code': ent.amenity_code,
                    'fruit_amenity': item[0],
                    'dessert_amenity': item[1],
                    'dessert_amenity1': item[2],
                    'iventory': ent.iventory,
                    'reserved': ent.reserved,
                    'input_date': input_date,
                    'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')
                    })


    return render(request, 'calc/tomorrow.html',{'data':Data_for_tomorrow,
                                              'date': day_after,
                                              'date1': 'Day after arrivals:'})


def special(request):
    
    if request.method == 'POST':
        form = SpecialAmenity(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'calc/special.html',{
        'form': SpecialAmenity(),
    })
    
    

    return render(request, 'calc/special.html',{
        'form': SpecialAmenity(),
    })


def update(request):

    if request.method == 'POST':
        
        date = request.POST['date']
        day = request.POST['day_of_week']
        code = request.POST['amenity_code']
       #inventory = request.POST['inventory']
        reserved = request.POST['reserved']
        
        data = Amenities_CSV(date=date,day_of_week=day,
                             amenity_code=code,iventory=100,
                             reserved=reserved,date_of_input=today)
        data.save()
        
    else:
        return render(request, 'calc/daily-addson.html',{
            'form':UpDateDaily()

        })

    return render(request, 'calc/daily-addson.html',{
        'form': UpDateDaily()
    })
   


def month(request, month):
    new_data = []
    cont = 0
    cont1 = 0
    ENTRY
    special_ameninty = Spacial_Amenities.objects.all()
    for s in special_ameninty:
        date_str = str(s.arrival_date)
        s_dobj = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
        s_month = s_dobj.strftime('%B')
        if month == s_month:
            new_data.append({'arrival_date': s.arrival_date,
                            'day_name': s.day_of_week,
                            'amenity_code': s.amenity_code,
                            'fruit_amenity': s.amenity_type,
                            'dessert_amenity': '',
                            'dessert_amenity1': '',
                            'iventory': 'iventory',
                            'reserved': s.amenity_amount,
                            'input_date': date_str,
                            'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')})
            cont = cont + 1


    for d in ENTRY:
        date_obj = dt.datetime.strptime(d.date, '%d/%m/%Y')
        ent_month = date_obj.strftime('%B')
        if month == ent_month:
            for key, item in CODE_AMENITY.items():
                if d.amenity_code == key:
                    input_date = str(d.date_of_input)
                    new_data.append({'arrival_date': d.date,
                            'day_name': d.day_of_week,
                            'amenity_code': d.amenity_code,
                            'fruit_amenity': item[0],
                            'dessert_amenity': item[1],
                            'dessert_amenity1': item[2],
                            'iventory': d.iventory,
                            'reserved': d.reserved,
                            'input_date': input_date,
                            'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')})
                    cont = cont + 1
    #print(cont)
    for i  in new_data:
        for j, m in i.items():            
            if j == 'reserved':
                if int(m) == 0 or m == '0':
                    new_data.remove(i)
                    cont1 = cont1 + 1
    
       
    

    return render(request, 'calc/arch-month.html', {
        'data': new_data,
        'month': month
    })

def media_file(request):

    data_view = []
    data = CSVFile.objects.all()
    for d in data:
        data_view.append({'file': d.file,
                    'id': d.big_id})
            
    return render(request, 'calc/media.html',{
            'data':data
    })

def delete_media(request,id):
    if request.user.is_superuser:
        print(request.user.username)
        print(id)
        file = CSVFile.objects.get(big_id=id)
        
        file.file.delete()
        file.delete()

        data_media = CSVFile.objects.all()
        print(data_media)
        return redirect('calc:index')

def total(request, month):
    new_data = []
    cont = 0
    cont1 = 0
    ENTRY
    special_ameninty = Spacial_Amenities.objects.all()
    for s in special_ameninty:
        date_str = str(s.arrival_date)
        s_dobj = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
        s_month = s_dobj.strftime('%B')
        if month == s_month:
            new_data.append({'arrival_date': s.arrival_date,
                            'day_name': s.day_of_week,
                            'amenity_code': s.amenity_code,
                            'fruit_amenity': s.amenity_type,
                            'dessert_amenity': '',
                            'dessert_amenity1': '',
                            'iventory': 'iventory',
                            'reserved': s.amenity_amount,
                            'input_date': date_str,
                            'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')})
            cont = cont + 1


    for d in ENTRY:
        date_obj = dt.datetime.strptime(d.date, '%d/%m/%Y')
        ent_month = date_obj.strftime('%B')
        if month == ent_month:
            for key, item in CODE_AMENITY.items():
                if d.amenity_code == key:
                    input_date = str(d.date_of_input)
                    new_data.append({'arrival_date': d.date,
                            'day_name': d.day_of_week,
                            'amenity_code': d.amenity_code,
                            'fruit_amenity': item[0],
                            'dessert_amenity': item[1],
                            'dessert_amenity1': item[2],
                            'iventory': d.iventory,
                            'reserved': d.reserved,
                            'input_date': input_date,
                            'today_date': time.strftime('%d'+'/'+'%m'+'/'+'%Y')})
                    cont = cont + 1
    #print(cont)
    for i  in new_data:
        for j, m in i.items():            
            if j == 'reserved':
                if int(m) == 0 or m == '0':
                    new_data.remove(i)
                    cont1 = cont1 + 1
    total_data = []

    for entry in new_data:
        for k, it in entry.items():
            
            if it == 'Small fruit bowl':
                total_data.append({
                    'small fruit': '',
                    'mid fruit':''
                })
                #print(entry.reserved)


    return render(request, 'calc/total.html',{
        'month': month
    })


def longstay(request):
    pass



def cost(request):
    pass

def daily_cost(request):
    pass



