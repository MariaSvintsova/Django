from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import DishForm
from main.models import Dish, Customer


class DishListView(ListView):
    model = Dish
    # template_name = 'main/dish_list.html'
    # object_list = Dish.objects.all()
    # context_object_name = f'{object_list}'
    # extra_context = {'title': 'SkyStore'}


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone} ({email}): {message}')
    return render(request, 'main/contacts.html')


class DishDetailView(DetailView):
    model = Dish
    # template_name = 'main/dish_detail.html'
    # context_object_name = 'dish'



class DishCreateView(CreateView):
    model = Dish
    fields = ('name', 'description', 'category', 'photo', 'price', 'birthday')
    success_url = reverse_lazy('main:home')




class DishUpdateView(UpdateView):
    model = Dish
    fields = ('name', 'description', 'category', 'photo', 'price', 'birthday')
    success_url = reverse_lazy('main:home')

    def get_success_url(self, *args, **kwargs):
        return reverse('main:students_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        CustomerFormset = inlineformset_factory(Dish, Customer, form=DishForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = CustomerFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = CustomerFormset(instance=self.object)
        return context_data



def toggle_activity(request, pk):
    dish_item = get_object_or_404(Dish, pk=pk)
    if dish_item.is_active:
        dish_item.is_active = False
    else:
        dish_item.is_active = True

    dish_item.save()
    return redirect(reverse('main:home'))