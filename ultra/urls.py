"""ultra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexfunction),
    path('team/', teamfunction),
    path('contact/', contactfunction),
    path('index/',indexfunction),
    path('cregistrationform/',cregistration_form),
    path('dregistrationform/',dregistration_form),
    path('loginc/',loginc),
    path('logindev/',logindev),
    path('form_submit/',contact_form),
    path('project/',project),
    #path('done/',donefunction),
    #path('admin_user/',admin_user),
    #path('admin_registration/',admin_registration),
    #path('update_form/',update_form),
    #path('admin_reg_del/<email>/',admin_reg_del),
    #path('admin_usr_details/<email>/',admin_usr_detail),
    #path('demofunction/',demofunction),
    #path('dashboard/',dashboard),
    #path('fileupload/',app_save),
    #path('fileform/',fileform),
    #path('admin_project/',admin_project),
    #path('admin_bid/',admin_bid),
    #path('admin_query/',admin_query),
    # 2admin panel
    #path('admin_index/',admin_index),
    #path('admin_index2/',admin_index2),
    #path('admin_index3/',admin_index3),
    #path('admin_alert/',admin_alert),
    #path('admin_badge/',admin_badge),
    #path('admin_card/',admin_card),
    #path('admin_chart/',admin_chart),
    #path('admin_font/',admin_font),
    #path('admin_form/',admin_form),
    #path('admin_grid/',admin_grid),
    #path('admin_inbox/',admin_inbox),
    #path('admin_index4/',admin_index4),
    #path('admin_map/',admin_map),
    #path('admin_modal/',admin_modal),
    #path('admin_progress-bar/',admin_probar),
    #path('admin_register/',admin_register),
    #path('admin_switch/',admin_switch),
    #path('admin_tab/',admin_tab),
    #path('admin_table/',admin_table),
    #path('admin_typo/',admin_typo),
    
    #main_admin
    path('admin_indexm/',admin_indexm),
    path('admin_cf/',admin_cf),
    path('admin_regclient/',admin_regclient),
    path('admin_clientupdate/<email>/',admin_clientupdate),
    path('admin_clientupdatein/',admin_clientupdatein),
    path('admin_clientdel/<email>/',admin_clientdel),
    path('admin_developer/',admin_developer),
    path('admin_developerupdate/<email>/',admin_developerupdate),
    path('admin_developerupdatein/',admin_developerupdatein),
    path('admin_developerdel/<email>/',admin_developerdel),
    path('admin_login/',admin_login),
    path('admin_loginauth/',admin_loginauth),
    path('admin_logout/',admin_logout),
    #path('export_users_csv/',export_users_csv),
    #path('export_dev_csv/',export_dev_csv),
    path('importcsv/',importcsvc),
    path('importcsvd/',importcsvd),
    path('reg_project/',reg_project),#render admin project table
    path('projectin/',projectin),#Project Insert by client
    path('export_project/<id>/',export_project),#Download Project File
    path('admin_bid/<id>/',bidding),#rendering admin bid page
    path('admin_bconfirm/<id>/',bid_confirm),#rendering admin bid page
    path('projdel/<id>/',projdel),#admin project delete
   #dev pass forgot
    path('resetdone/',resetdone),#send reset link on email
    path('resetconfirm/',resetconfirm),
    path('resetcomplete/',resetcomplete),
    path('resetpassword/<id>/',resetpassword),#reset pass page render
    path('upresetpass/<id>/',upresetpass),#reset pass insert
    path('send_email/',smail),#send email forgot
    path('dev_fp/',dev_fp),#dev forgot pass
    #client fp
    path('logout/',logout),
    path('resetpasswordc/<id>/',resetpasswordc),#reset pass page render
    path('upresetpassc/<id>/',upresetpassc),#reset pass insert
    path('send_emailc/',smailc),#send email forgot
    path('cli_fp/',cli_fp),#dev forgot pass
    #Developer panel
    path('dev_dashboard/',dev_dashboard),#Developer Dashboard
    path('dev_project/',dev_project),#Developer assign projects
    path('dev_confirm/',dev_confirm),#Developer confirm projects
    path('dev_inbox/',dev_inbox),#Developer inbox
    path('dev_form/',dev_form),#Developer inbox
    path('dev_profileupdate/',dev_profileupdate),#admin profile update
    path('devindex/',devindex),#admin profile update
    path('bidpopup/<id>/',bidpopup),#Developer bid popup
    path('descpopup/<id>/',descpopup),#Developer bid popup
    path('descpopupcli/<id>/',descpopupcli),#Developer client detail popup
    path('descpopupd/<id>/',descpopupd),#Developer projdesc popup
    path('cpassd/<id>/',cpassd),#client cpass render
    path('cpassdev/<id>/',cpassdev),#client cpass change
    path('popupupload/<id>/',popupupload),
    path('upprojfile/<id>/',upprojfile),
    #client panel
    path('cliindex/',cliindex),#client browseproject
    path('downloadf/<id>/',downloadf),
    path('cli_dashboard/',cli_dashboard),#Client Dashboard
    path('cli_form/',cli_form),#Client profile form
    path('cli_profileupdate/',cli_profileupdate),#Client profile update
    path('cdescpopup/<id>/',cdescpopup),#Client desc popup
    path('cpassc/<id>/',cpassc),#client cpass render
    path('cpasscli/<id>/',cpasscli),#client cpass change
]
