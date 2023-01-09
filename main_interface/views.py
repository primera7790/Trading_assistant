from program import main

from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

# from main_interface.models import UserData
from .tasks import auto_mode_task, stop_auto_mode_task
# from program.tech_zone.modules.work_with_data import work_volume_calculation
from main_interface.forms import BalanceForm
from program.tech_zone.modules.database_admin import table_update, table_select
from program.tech_zone.modules.work_with_data import check_new_balance, work_volume_calculation


# count = 0
process_id = 0


def index(request):
    return render(request, 'main_interface/index.html')


def init_base(request):
    work_volume_message = work_volume_calculation()
    messages.info(request, work_volume_message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def init_current(request):
    work_volume_message = main.main()
    messages.info(request, work_volume_message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def init_auto_mode(request):
    global process_id
    start_process = auto_mode_task.delay()
    process_id = start_process.id
    # work_volume_calculation()
    process_start_message = 'Авторежим активирован. Telegram bot активен.'
    messages.info(request, process_start_message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def init_disable_auto_mode(request):
    stop_auto_mode_task(process_id)
    process_stop_message = 'Авторежим деактивирован. Telegram bot более не активен.'
    messages.info(request, process_stop_message)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def change_settings(request):
    submit_button = request.POST.get('submit')

    value = ''
    form = BalanceForm(request.POST or None)

    context = {
        'form': form,
        'value': value,
        'submit_button': submit_button,
    }

    if form.is_valid():
        value = form.cleaned_data.get('value')
        check_response = check_new_balance(value)

        if check_response == 'Баланс успешно обновлен!':
            table_update('balance', round(float(value), 3))
            messages.info(request, check_response)
            return HttpResponseRedirect(reverse('index'))

        elif check_response and check_response != 'Баланс успешно обновлен!':
            messages.info(request, check_response)
            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'main_interface/settings.html', context)


def show_balance(request):
    balance = table_select('balance')
    messages.info(request, f'Ваш баланс: {balance}$')
    return render(request, 'main_interface/balance.html')
