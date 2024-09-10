from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm, UserUpdateForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data("username")
            password = form.cleaned_data("password1")
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'account/register.html', {"form": form})

    else:
        form = NewUserForm()
        return render(request, 'account/register.html', {"form": form})
    

def user_login(request):
    if request.user.is_authenticated and 'next' in request.GET:
        messages.add_message(request, messages.WARNING, 'Erişiminiz bulunmamaktadır!') 
        return redirect('index')

    if request.method == 'POST':
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username = username, password = password)


            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Giriş Başarılı!')
                nextUrl = request.GET.get('next', None)
                if nextUrl is None:
                    return redirect('blog')
                else:
                    return redirect(nextUrl)
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            return render(request, 'account/login.html', {'form': form})
        
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('blog')


def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parola başarıyla güncellendi')
            return redirect('index')
        else:
            return render(request, 'account/change_password.html', {'form': form})


    form = UserPasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {"form": form})


def account(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'joined_date': user.date_joined,
        'first_name': user.first_name,
        'last_name': user.last_name
        # Diğer göstermek istediğiniz kullanıcı bilgileri buraya ekleyin
    }
    return render(request, 'account/account.html', context)



def update_info(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bilgileriniz başarıyla güncellendi.')
            return redirect('account')

        else:
            messages.error(request, 'Bir hata oluştu. Lütfen bilgilerinizi kontrol edin.')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'account/update_info.html', {'form': form})


