from django.shortcuts import render, redirect

# Demo user data (replace with database or Django User model for production)
USER_DATA = {
    'usha': {
        'name': 'Usha ',
        'employee_id': 'EMP1001',
        'department': 'Development',
        'role': 'Backend Developer',
        'email': 'usha.r@nexnora.com',
        'phone': '+91-9876543210',
    },
    'kavyav': {
        'name': 'Kavya V',
        'employee_id': 'EMP12345',
        'department': 'Development',
        'role': 'Frontend Developer',
        'email': 'kavya.v@nexnora.com',
        'phone': '+91-9876543210',
    },
    # Add more users as needed
}

def login(request):
    return render(request, 'login.html')

def userd(request):
    return render(request, 'userd.html')

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # For demo, password is '1234' for all users
        if username in USER_DATA and password == '1234':
            request.session['user'] = username
            return redirect('user_page')
        else:
            error = 'Invalid username or password'
    return render(request, 'login.html', {'error': error})

def user_page(request):
    user = request.session.get('user')
    if not user or user not in USER_DATA:
        return redirect('login')
    profile = USER_DATA[user]
    return render(request, 'user_page.html', {'username': user, 'profile': profile})

def logout_view(request):
    request.session.flush()
    return redirect('login')