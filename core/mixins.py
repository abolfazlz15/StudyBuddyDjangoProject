# ---this code has bug---

# from django.http import Http404, HttpResponse

# class AddTopicMixins():
#     def dispach(self, request, *args, **kwargs):
#         if request.user.username == 'abolfazl':
#             print('sfsdf')
#         else:
#             print('aaaa')
#         return super().dispach(request, *args, **kwargs)