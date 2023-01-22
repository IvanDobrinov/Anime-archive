def get_base_context(request):
    context = {}

    context['authenticated'] = request.user.is_authenticated

    return context