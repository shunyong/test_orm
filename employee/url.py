from employee.views import *
from django.urls import path,include
urlpatterns = [
    # path('list_employee_old/',list_employee_old),
    # path('add_employee_old/',add_employee_old),
    # path('edit_employee_old/<int:emp_id>/',edit_employee_old),
    # path('del_employee_old/<int:emp_id>/',delete_employee_old),# 操作部门数据表（department）相关URL配置项
    path('add_dep_old/',add_dep_old),
    path('del_dep_old/<int:dep_id>/',del_dep_old),
    path('edit_dep_old/<int:dep_id>/',edit_dep_old),# 操作团体数据表（group）相关URL配置项
    # path('add_group_old/',add_group_old),
    # path('list_group_old/',list_group_old),
    # path('del_group_old/<int:group_id>/',del_group_old),
    # path('edit_group_old/<int:group_id>/',edit_group_old),# 操作员工补充信息数据表（employeeinfo）相关URL配置项
    # path('add_emnployeeinfo_old/', add_employeeinfo_old),
    # path('list_employeeinfo_old/', list_employeeinfo_old),
    # path('del_employeeinfo_old/<int:info_id>/', del_employeeinfo_old),
    # path('edit_employeeinfo_old/<int:info_id>/', edit_employeeinfo_old),
path('list_dep_old/',list_dep_old)
]