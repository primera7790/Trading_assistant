from trading_assistant.celery_file import app
from program.tech_zone.modules.trading_assist_bot import init_bot


@app.task
def auto_mode_task():
    init_bot()


@app.task
def stop_auto_mode_task(process_id):
    app.control.revoke(process_id, terminate=True)





# def auto_mode_task(request):
#     work_volume_message = auto_mode()
#     # time.sleep(10)
#     # work_volume_message = work_volume_calculation
#     messages.info(request, work_volume_message)
#     HttpResponseRedirect(request.META.get('HTTP_REFERER'))
