from django.shortcuts import render

# Create your views here.
# from .models import Message


# @require_http_methods(["GET", "POST"])
# def form_template_view(request):
#     """Create data records via form submission."""
#     if request.method == 'POST':
#         form = GuestBookForm(request.POST)
#         if form.is_valid():
#             Message.objects.create(name=form.cleaned_data.get('name'),
#                                    message=form.cleaned_data.get('msg'))
#             messages.success(request, 'Success!')
#             return HttpResponseRedirect('form')
#     else:
#         form = GuestBookForm()
#     context = {'title': 'Form View',
#                'form': form,
#                'path': request.path,
#                'entries': Message.objects.all()}
#     return render(request, 'function_views/form.html', context)