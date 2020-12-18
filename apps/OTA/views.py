from django.shortcuts import render
from apps.OTA.models import Message

# Create your views here.


def message_form(request):

    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()
    elif request.method == "GET":
        var_dict = {}
        all_message = Message.objects.filter()
        if all_message:
            message = all_message[0]
            var_dict = {
                "message": message
            }
            print(message.message)
        return render(request, "message_form.html", var_dict)

    return render(request, "message_form.html")
