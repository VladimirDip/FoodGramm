from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView

from .logic import get_request_tags, save_recipe, edit_recipe
from .models import Recipe, Tag
from .forms import RecipeForm


class IndexListView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'
    paginate_by = 2

    def get_queryset(self):
        self.recipes = Recipe.objects.filter(tags__title__in=get_request_tags(
            request=self.request)).select_related(
            'author').prefetch_related(
            'tags').order_by('-pk').distinct('pk')
        return self.recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        # print(context)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'singlePageNotAuth.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


# class RecipeCreateView(CreateView):
#     template_name = 'formRecipe.html'
#     model = Recipe
#     form_class = RecipeForm
#     success_url = 'index'
#
#     def form_valid(self, form):
#         print(self.object)
#         print(form.instance)
#         save = save_recipe(self.request, form.instance)
#         print(save)
#         return super().form_valid(form)

def recipe_new(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        print(f'this is form {form.data}')
        print(f'this is form_valid {form.is_valid()}')

        if form.is_valid():
            recipe = save_recipe(request, form)

            return redirect(
                'recipe_view_slug', slug=recipe.slug
            )
        else:
            print(form.errors.as_data())
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'formRecipe.html', context)





