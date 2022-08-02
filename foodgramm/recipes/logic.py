

def get_request_tags(request):
    return request.GET.getlist('tag', ('breakfast', 'lunch', 'dinner'))