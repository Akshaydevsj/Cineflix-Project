from django.shortcuts import render,redirect

from django.views import View

from . models import SubscriptionPlans

from django.utils.decorators import method_decorator

from .forms import SubscriptionPlanForm

from authentication.permissions import permitted_user_roles

# Create your views here.

class SubscriptionView(View):

    template = 'subscriptions/subscription-list.html'

    def get(self, request, *args, **kwargs):

        plans = SubscriptionPlans.objects.filter(active_status=True)

        data = {'plans': plans}

        return render(request, self.template,context=data)
                      

@method_decorator(permitted_user_roles(['Admin']), name='dispatch')
class SubscriptionPlanCreateView(View):

    form_class = SubscriptionPlanForm

    template = 'subscriptions/subscription-plan-create.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        data = {

            'page': 'Create Subscription Plan',

            'form': form,

        }

        return render(request, self.template, context=data)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()

            return redirect('subscription-list')  

        print(form.errors)

        data = {

            'page': 'Create Subscription Plan',

            'form': form,

        }

        return render(request, self.template, context=data)
    


@method_decorator(permitted_user_roles(['Admin']), name='dispatch')
class SubscriptionPlanEditView(View):

    form_class = SubscriptionPlanForm

    template = 'subscriptions/subscription-plan-edit.html'

    def get(self, request, uuid, *args, **kwargs):

        plan = SubscriptionPlans.objects.get(uuid=uuid)

        form = self.form_class(instance=plan)

        data = {'form': form, 'page': plan.name}

        return render(request, self.template, context=data)

    def post(self, request, uuid, *args, **kwargs):

        plan = SubscriptionPlans.objects.get(uuid=uuid)

        form = self.form_class(request.POST, instance=plan)

        if form.is_valid():

            form.save()

            return redirect('subscription-list')

        data = {'form': form, 'page': plan.name}

        return render(request, self.template, context=data)



@method_decorator(permitted_user_roles(['Admin']), name='dispatch')
class SubscriptionPlanDeleteView(View):

    def get(self, request, uuid, *args, **kwargs):

        plan = SubscriptionPlans.objects.get(uuid=uuid)

        plan.active_status = False  

        plan.save()

        return redirect('subscription-list')



