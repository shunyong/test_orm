from django.shortcuts import render,redirect,HttpResponse
from .models import employee,department,group,employeeinfo
# Create your views here.
def list_dep_old(request):
    dep_list = department.objects.all()
    return render(request,'test_orm/list_dep_old.html',{'dep_list':dep_list})

def add_dep_old(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '部门名称不能为空！'})

    try:# 用create()函数新建一条记录，这条记录会自动保存，不用调用save()函数
        p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
        return redirect('/test_orm_old/list_dep_old')
    except Exception as e:
        return render(request, 'test_orm/add_dep_old.html',{'error_info':'输入部门名称重复或信息有错误！'})
    finally:
        pass
    return render(request, 'test_orm/add_dep_old.html')

def del_dep_old(request,dep_id):
    dep_object = department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old/')

def edit_dep_old(request,dep_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = department.objects.get(id=id)
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object=department.objects.get(id=dep_id)
        return render(request,'test_orm/edit_dep_old.html',{'department':dep_object})