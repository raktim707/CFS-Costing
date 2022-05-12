from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import MaterialConfigurationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import RFQEntry, MaterialConfiguration, Material, PrimaryProcess, SecondaryProcess, MaterialCost, ProcessCost, StandardPart
from .forms import MaterialForm
from .utils import getDimension, getMatDim
from django.views.generic.edit import UpdateView
from django.core import serializers
from django.template.loader import render_to_string


@login_required(redirect_field_name='login')
def home(request):
    return render(request, 'inventory/home.html')


@login_required(redirect_field_name='login')
def add_entry(request):
    rfq_entry = RFQEntry.objects.all()
    primary_process = PrimaryProcess.objects.all()
    secondary_process = SecondaryProcess.objects.all()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
    else:
        form = MaterialForm()
    return render(request, 'inventory/add_entry.html', {'form': form, 'primary_process': primary_process, 'secondary_process': secondary_process, 'rfq_entry': rfq_entry})


def rfq_detail(request, pk):
    rfq_entry = get_object_or_404(RFQEntry, pk=pk)
    materials = rfq_entry.materialcost_set.all()
    process = rfq_entry.processcost_set.all()
    return render(request, "inventory/rfq_entry_detail.html", {'rfq_entry': rfq_entry, 'materials': materials, 'process': process})


class EditRFQView(UpdateView):
    model = RFQEntry
    template_name = 'inventory/edit_rfq.html'
    fields = ['rfq_no', 'dwg_no', 'customer', 'type', 'date']

    def get_success_url(self, **kwargs):
        return reverse_lazy('rfq_detail', args=(self.object.pk,))


def editMaterialView(request, pk):
    materialcost = get_object_or_404(MaterialCost, pk=pk)
    if request.method == 'GET':
        material = materialcost.material
        material_configuration = get_object_or_404(
            MaterialConfiguration, name=material)
        active_fields = getMatDim(material_configuration, materialcost)
        print(active_fields)
        return render(request, 'inventory/edit_material.html', {'active_fields': active_fields, 'material_cost': materialcost})

    if request.method == 'POST':
        materialCost = request.POST.dict()
        print(materialCost)
        materialCost.pop('csrfmiddlewaretoken')
        MaterialCost.objects.filter(
            pk=pk).update(**materialCost)
        materialcost.editor.add(request.user)
        return redirect('add_entry')


@login_required(redirect_field_name='login')
def import_from_excel(request):
    return render(request, 'inventory/import.html')


def adminMaterialConfigure(request):
    if request.method == 'POST':
        form = MaterialConfigurationForm(request.POST)
        return redirect('/')
    else:
        form = MaterialConfigurationForm()
    return render(request, 'inventory/materialConfigure.html', {'form': form})


def primaryProcess(request):
    return render(request, 'inventory/primaryProcess.html')


def secondaryProcess(request):
    return render(request, 'inventory/secondaryProcess.html')


def addPrimaryProcess(request):
    return render(request, 'inventory/addPrimaryProcess.html')


def manageUser(request):
    users = User.objects.all()
    return render(request, 'inventory/manageUsers.html')


def addNewUser(request):
    return render(request, "inventory/addUser.html")


def rfqGeneralData(request):
    user = request.user
    my_data = request.POST.dict()
    rfq_no = my_data['rfq_no']
    dwg_no = my_data['dwg_no']
    customer = my_data['customer']
    type = my_data['type']
    date = my_data['date']
    if not RFQEntry.objects.filter(rfq_no=rfq_no):
        instance = RFQEntry.objects.create(rfq_no=rfq_no, dwg_no=dwg_no,
                                           customer=customer, type=type, date=date)
        instance.editor.add(user)
        return JsonResponse(my_data)
    else:
        return JsonResponse({'error': 'Error'})


def materialDimensions(request):
    if request.method == 'GET':
        my_data = request.GET.dict()
        name = my_data['name']
        material = MaterialConfiguration.objects.get(name=name)
        active_fields = getDimension(material)
        return JsonResponse({"my_data": active_fields})


def materialCost(request):
    if request.method == 'POST':
        material_data = request.POST.dict()
        material_name = material_data.pop('name')
        material = Material.objects.get(id=material_name)
        rfq_no = material_data['rfq_no']
        rfq_entry = RFQEntry.objects.get(rfq_no=rfq_no)
        if material_data['csrfmiddlewaretoken']:
            material_data.pop('csrfmiddlewaretoken')

        if material and rfq_entry:
            material_data['material'] = material
            material_data['rfq_no'] = rfq_entry
            material_cost = MaterialCost(**material_data)
            material_cost.save()
            material_cost.editor.add(request.user)
            material_cost.save()
            material_data['rfq_no'] = rfq_no
            material_data['material'] = material_name
            return JsonResponse(material_data)


def processCost(request):
    if request.method == 'POST':
        process_data = request.POST.dict()
        if process_data['csrfmiddlewaretoken']:
            process_data.pop('csrfmiddlewaretoken')
        rfq_no = process_data['rfq_no']
        #rfq_no = get_object_or_404(RFQEntry, rfq_no=rfq_no)
        primary_process = process_data['PrimaryProcess']
        primary_process = get_object_or_404(
            PrimaryProcess, name=primary_process)
        secondary_process = process_data['SecondaryProcess']
        secondary_process = get_object_or_404(
            SecondaryProcess, name=secondary_process)
        quantity = process_data['Quantity']
        primary_cost = process_data['PrimaryCost']
        secondary_cost = process_data['SecondaryCost']
        total_cost = int(primary_cost) * int(quantity) + \
            int(secondary_cost) * int(quantity)
        process_data['total_cost'] = total_cost
        print('Process data is: ', process_data)
        '''new_process_cost = ProcessCost(rfq_no=rfq_no, quantity=quantity, primary_process=primary_process,
                                       secondary_process=secondary_process, primary_cost=primary_cost, secondary_cost=secondary_cost)
        new_process_cost.save()
        new_process_cost.editor.add(request.user)
        new_process_cost.save()'''
        return JsonResponse(process_data)


def searchStandardPart(request):
    if request.method == 'GET':
        query = request.GET.dict()
        dwg_no = ''
        manufacturer = ''
        model = ''
        if query['DWG']:
            dwg_no = int(query['DWG'])
            parts = StandardPart.objects.filter(dwg_no=dwg_no)
        if query['Manufacturer']:
            manufacturer = query['Manufacturer']
            if dwg_no != '':
                if len(parts) != 0:
                    parts = parts.filter(Manufacturer=manufacturer)
            else:
                parts = StandardPart.objects.filter(Manufacturer=manufacturer)
        if query['Model']:
            model = query['Model']
            if parts:
                parts.filter(model_no=model)
            else:
                parts = StandardPart.objects.filter(model_no=model)
        if parts:
            html = render_to_string(
                template_name='inventory/partial_results.html', context={'parts': parts})
            data_dict = {'html_from_view': html}
            return JsonResponse(data=data_dict, safe=False)


def welcome(request):
    return render(request, 'inventory/landing.html')
