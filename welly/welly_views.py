from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='welly:page-login')
def index(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'welly/index.html',context)

@login_required(login_url='welly:page-login')
def statistics(request):
    context={
        "page_title":"Statistics"
    }
    return render(request,'welly/statistics.html',context)

@login_required(login_url='welly:page-login')
def work_list(request):
    context={
        "page_title":"Work List"
    }
    return render(request,'welly/work-list.html',context)

def patient(request):
    context={
        "page_title":"Patient"
    }
    return render(request,'welly/patient.html',context)


def patient_details(request):
    context={
        "page_title":"Patient Detail"
    }
    return render(request,'welly/patient-details.html',context)


def doctor(request):
    context={
        "page_title":"Doctor"
    }
    return render(request,'welly/doctor.html',context)


def doctor_details(request):
    context={
        "page_title":"Doctor Details"
    }
    return render(request,'welly/doctor-details.html',context)


def reviews(request):
    context={
        "page_title":"Reviews"
    }
    return render(request,'welly/reviews.html',context)



def app_profile(request):
    context={
        "page_title":"App Profile"
    }
    return render(request,'welly/apps/app-profile.html',context)


def post_details(request):
    context={
        "page_title":"Post Details"
    }
    return render(request,'welly/apps/post-details.html',context)


def email_compose(request):
    context={
        "page_title":"Compose"
    }
    return render(request,'welly/apps/email/email-compose.html',context)


def email_inbox(request):
    context={
        "page_title":"Inbox"
    }
    return render(request,'welly/apps/email/email-inbox.html',context)


def email_read(request):
    context={
        "page_title":"Read"
    }
    return render(request,'welly/apps/email/email-read.html',context)


def app_calendar(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'welly/apps/app-calendar.html',context)


def ecom_product_grid(request):
    context={
        "page_title":"Product Grid"
    }
    return render(request,'welly/apps/shop/ecom-product-grid.html',context)


def ecom_product_list(request):
    context={
        "page_title":"Product List"
    }
    return render(request,'welly/apps/shop/ecom-product-list.html',context)


def ecom_product_detail(request):
    context={
        "page_title":"Product Detail"
    }
    return render(request,'welly/apps/shop/ecom-product-detail.html',context)


def ecom_product_order(request):
    context={
        "page_title":"Product Order"
    }
    return render(request,'welly/apps/shop/ecom-product-order.html',context)


def ecom_checkout(request):
    context={
        "page_title":"Checkout"
    }
    return render(request,'welly/apps/shop/ecom-checkout.html',context)


def ecom_invoice(request):
    context={
        "page_title":"Invoice"
    }
    return render(request,'welly/apps/shop/ecom-invoice.html',context)


def ecom_customers(request):
    context={
        "page_title":"Customers"
    }
    return render(request,'welly/apps/shop/ecom-customers.html',context)


def flat_icons(request):
    context={
        "page_title":"Flat Icons"
    }
    return render(request,'welly/flat-icons.html',context)


def svg_icons(request):
    context={
        "page_title":"Svg Icons"
    }
    return render(request,'welly/svg-icons.html',context)


def feather_icons(request):
    context={
        "page_title":"Feather Icons"
    }
    return render(request,'welly/feather-icons.html',context)


def content(request):
    context={
        "page_title":"Content"
    }
    return render(request,'welly/cms/content.html',context)


def add_content(request):
    context={
        "page_title":"Add Content"
    }
    return render(request,'welly/cms/add-content.html',context)


def menu(request):
    context={
        "page_title":"Menu"
    }
    return render(request,'welly/cms/menu.html',context)


def email_template(request):
    context={
        "page_title":"Email Template"
    }
    return render(request,'welly/cms/email-template.html',context)


def add_email(request):
    context={
        "page_title":"Add Email"
    }
    return render(request,'welly/cms/add-email.html',context)


def blog(request):
    context={
        "page_title":"Blog"
    }
    return render(request,'welly/cms/blog.html',context)


def add_blog(request):
    context={
        "page_title":"Add Blog"
    }
    return render(request,'welly/cms/add-blog.html',context)


def blog_category(request):
    context={
        "page_title":"Blog Category"
    }
    return render(request,'welly/cms/blog-category.html',context)


def chart_flot(request):
    context={
        "page_title":"Chart Flot"
    }
    return render(request,'welly/charts/chart-flot.html',context)


def chart_morris(request):
    context={
        "page_title":"Chart Morris"
    }
    return render(request,'welly/charts/chart-morris.html',context)


def chart_chartjs(request):
    context={
        "page_title":"Chart Chartjs"
    }
    return render(request,'welly/charts/chart-chartjs.html',context)


def chart_chartist(request):
    context={
        "page_title":"Chart Chartist"
    }
    return render(request,'welly/charts/chart-chartist.html',context)


def chart_sparkline(request):
    context={
        "page_title":"Chart Sparkline"
    }
    return render(request,'welly/charts/chart-sparkline.html',context)


def chart_peity(request):
    context={
        "page_title":"Chart Peity"
    }
    return render(request,'welly/charts/chart-peity.html',context)



def ui_accordion(request):
    context={
        "page_title":"Accordion"
    }
    return render(request,'welly/bootstrap/ui-accordion.html',context)


def ui_alert(request):
    context={
        "page_title":"Alert"
    }
    return render(request,'welly/bootstrap/ui-alert.html',context)


def ui_badge(request):
    context={
        "page_title":"Badge"
    }
    return render(request,'welly/bootstrap/ui-badge.html',context)


def ui_button(request):
    context={
        "page_title":"Button"
    }
    return render(request,'welly/bootstrap/ui-button.html',context)


def ui_modal(request):
    context={
        "page_title":"Modal"
    }
    return render(request,'welly/bootstrap/ui-modal.html',context)


def ui_button_group(request):
    context={
        "page_title":"Button Group"
    }
    return render(request,'welly/bootstrap/ui-button-group.html',context)


def ui_list_group(request):
    context={
        "page_title":"List Group"
    }
    return render(request,'welly/bootstrap/ui-list-group.html',context)


def ui_media_object(request):
    context={
        "page_title":"Media Object"
    }
    return render(request,'welly/bootstrap/ui-media-object.html',context)


def ui_card(request):
    context={
        "page_title":"Card"
    }
    return render(request,'welly/bootstrap/ui-card.html',context)


def ui_carousel(request):
    context={
        "page_title":"Carousel"
    }
    return render(request,'welly/bootstrap/ui-carousel.html',context)


def ui_dropdown(request):
    context={
        "page_title":"Dropdown"
    }
    return render(request,'welly/bootstrap/ui-dropdown.html',context)


def ui_popover(request):
    context={
        "page_title":"Popover"
    }
    return render(request,'welly/bootstrap/ui-popover.html',context)


def ui_progressbar(request):
    context={
        "page_title":"Progressbar"
    }
    return render(request,'welly/bootstrap/ui-progressbar.html',context)


def ui_tab(request):
    context={
        "page_title":"Tab"
    }
    return render(request,'welly/bootstrap/ui-tab.html',context)


def ui_typography(request):
    context={
        "page_title":"Typography"
    }
    return render(request,'welly/bootstrap/ui-typography.html',context)


def ui_pagination(request):
    context={
        "page_title":"Pagination"
    }
    return render(request,'welly/bootstrap/ui-pagination.html',context)


def ui_grid(request):
    context={
        "page_title":"Grid"
    }
    return render(request,'welly/bootstrap/ui-grid.html',context)




def uc_select2(request):
    context={
        "page_title":"Select"
    }
    return render(request,'welly/plugins/uc-select2.html',context)


def uc_nestable(request):
    context={
        "page_title":"Nestable"
    }
    return render(request,'welly/plugins/uc-nestable.html',context)


def uc_noui_slider(request):
    context={
        "page_title":"UI Slider"
    }
    return render(request,'welly/plugins/uc-noui-slider.html',context)


def uc_sweetalert(request):
    context={
        "page_title":"Sweet Alert"
    }
    return render(request,'welly/plugins/uc-sweetalert.html',context)


def uc_toastr(request):
    context={
        "page_title":"Toastr"
    }
    return render(request,'welly/plugins/uc-toastr.html',context)


def map_jqvmap(request):
    context={
        "page_title":"Jqvmap"
    }
    return render(request,'welly/plugins/map-jqvmap.html',context)


def uc_lightgallery(request):
    context={
        "page_title":"LightGallery"
    }
    return render(request,'welly/plugins/uc-lightgallery.html',context)


def widget_basic(request):
    context={
        "page_title":"Widget"
    }
    return render(request,'welly/widget-basic.html',context)


def form_element(request):
    context={
        "page_title":"Form Element"
    }
    return render(request,'welly/forms/form-element.html',context)


def form_wizard(request):
    context={
        "page_title":"Form Wizard"
    }
    return render(request,'welly/forms/form-wizard.html',context)


def form_editor(request):
    context={
        "page_title":"CkEditor"
    }
    return render(request,'welly/forms/form-editor.html',context)


def form_pickers(request):
    context={
        "page_title":"Pickers"
    }
    return render(request,'welly/forms/form-pickers.html',context)


def form_validation(request):
    context={
        "page_title":"Form Validation"
    }
    return render(request,'welly/forms/form-validation.html',context)


def table_bootstrap_basic(request):
    context={
        "page_title":"Table Bootstrap"
    }
    return render(request,'welly/table/table-bootstrap-basic.html',context)


def table_datatable_basic(request):
    context={
        "page_title":"Table Datatable"
    }
    return render(request,'welly/table/table-datatable-basic.html',context)






def page_register(request):
    return render(request,'welly/pages/page-register.html')

def page_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('login successful')
            return redirect('welly:index')

    return render(request,'welly/pages/page-login.html')

def page_logout(request):
    logout(request)
    return redirect('welly:page-login')

def page_forgot_password(request):
    return render(request,'welly/pages/page-forgot-password.html')

def page_lock_screen(request):
    return render(request,'welly/pages/page-lock-screen.html')

def page_empty(request):
    context={
        "page_title":"Empty Page"
    }
    return render(request,'welly/pages/page-empty.html',context)

def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')
