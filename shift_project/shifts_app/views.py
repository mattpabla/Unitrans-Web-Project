from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .shift import Shift
from .run import Run
from .shift_group import ShiftGroup
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from shifts_app.forms import ShiftForm
from django.core.urlresolvers import reverse


def check_admin(user):
   return user.is_superuser


def selection_page(request):
    return render(request,'shifts_app/selection_page.html')

@user_passes_test(check_admin)
@login_required(login_url='/shifts_app/login/')
def sup_main(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/sup_main.html', context)


@login_required(login_url='/shifts_app/login/')
def employee_main(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    
    context = {
        'all_shifts': all_shifts,
        'all_runs':all_runs,
    }
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request,'shifts_app/employee_main.html', context)

@login_required(login_url='/shifts_app/login/')
def monday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/monday.html', context)

@login_required(login_url='/shifts_app/login/')
def tuesday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/tuesday.html', context)

@login_required(login_url='/shifts_app/login/')
def wednesday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/wednesday.html', context)

@login_required(login_url='/shifts_app/login/')
def thursday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/thursday.html', context)

@login_required(login_url='/shifts_app/login/')
def friday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/friday.html', context)

@login_required(login_url='/shifts_app/login/')
def saturday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/saturday.html', context)

@login_required(login_url='/shifts_app/login/')
def sunday(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/sunday.html', context)


#def index(request,group_id):
    #group = get_object_or_404(ShiftGroup, pk=group_id)
    #return render(request,'shifts_app/index.html', {'group': group})

@login_required(login_url='/shifts_app/login/')
def detail(request,shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    return render(request,'shifts_app/detail.html', {'shift': shift})

@login_required(login_url='/shifts_app/login/')
def shift_cover(request):
    
    all_shifts = Shift.objects.all()
    try:
        selected_shift = all_shifts.get(pk=request.POST["shift"])
    except (KeyError, Shift.DoesNotExist):
        return render(request,'shifts_app/shift_cover.html', 
        {
            'all_shifts' : all_shifts,
            'error_message':"no valid Shift selected",
        })
    else:
        selected_shift.shift_cover = True
        selected_shift.covered = True

        selected_shift.save()
        return render(request,'shifts_app/shift_cover.html', {'all_shifts' : all_shifts})


class ShiftDelete(DeleteView):
    model = Shift
    success_url = reverse_lazy('shifts_app:sup_main')


@login_required(login_url='/shifts_app/login/')
def chat_room(request):
    all_shifts = Shift.objects.all()
    all_runs = Run.objects.all()
    context = {'all_shifts': all_shifts,'all_runs':all_runs}
    return render(request,'shifts_app/chat_room.html', context)



@user_passes_test(check_admin)
def add_shifts(request):
    if request.method =='POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('shifts_app:sup_main'))
        else :
            return render(request, 'shifts_app/add_shifts.html', {'form': form})
    else:
        form = ShiftForm()

        args = {'form': form}
        return render(request, 'shifts_app/add_shifts.html', args)







