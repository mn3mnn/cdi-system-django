from django.urls import path
from welly import welly_views
app_name='welly'
urlpatterns = [
    path('',welly_views.index,name="index"),
    path('index/',welly_views.index,name="index"),
    path('patient',welly_views.patient,name="patient"),
    path('patient-details',welly_views.patient_details,name="patient-details"),
    path('doctor',welly_views.doctor,name="doctor"),
    path('doctor-details',welly_views.doctor_details,name="doctor-details"),
    path('reviews',welly_views.reviews,name="reviews"),


    path('app-profile/',welly_views.app_profile,name="app-profile"),
    path('post-details/',welly_views.post_details,name="post-details"),
    path('email-compose/',welly_views.email_compose,name="email-compose"),
    path('email-inbox/',welly_views.email_inbox,name="email-inbox"),
    path('email-read/',welly_views.email_read,name="email-read"),
    path('app-calendar/',welly_views.app_calendar,name="app-calendar"),
    path('ecom-product-grid/',welly_views.ecom_product_grid,name="ecom-product-grid"),
    path('ecom-product-list/',welly_views.ecom_product_list,name="ecom-product-list"),
    path('ecom-product-detail/',welly_views.ecom_product_detail,name="ecom-product-detail"),
    path('ecom-product-order/',welly_views.ecom_product_order,name="ecom-product-order"),
    path('ecom-checkout/',welly_views.ecom_checkout,name="ecom-checkout"),
    path('ecom-invoice/',welly_views.ecom_invoice,name="ecom-invoice"),
    path('ecom-customers/',welly_views.ecom_customers,name="ecom-customers"),
    path('chart-flot/',welly_views.chart_flot,name="chart-flot"),
    path('chart-morris/',welly_views.chart_morris,name="chart-morris"),
    path('chart-chartjs/',welly_views.chart_chartjs,name="chart-chartjs"),
    path('chart-chartist/',welly_views.chart_chartist,name="chart-chartist"),
    path('chart-sparkline/',welly_views.chart_sparkline,name="chart-sparkline"),
    path('chart-peity/',welly_views.chart_peity,name="chart-peity"),

    path('ui-accordion/',welly_views.ui_accordion,name="ui-accordion"),
    path('ui-alert/',welly_views.ui_alert,name="ui-alert"),
    path('ui-badge/',welly_views.ui_badge,name="ui-badge"),
    path('ui-button/',welly_views.ui_button,name="ui-button"),
    path('ui-modal/',welly_views.ui_modal,name="ui-modal"),
    path('ui-button-group/',welly_views.ui_button_group,name="ui-button-group"),
    path('ui-list-group/',welly_views.ui_list_group,name="ui-list-group"),
    path('ui-media-object/',welly_views.ui_media_object,name="ui-media-object"),
    path('ui-card/',welly_views.ui_card,name="ui-card"),
    path('ui-carousel/',welly_views.ui_carousel,name="ui-carousel"),
    path('ui-dropdown/',welly_views.ui_dropdown,name="ui-dropdown"),
    path('ui-popover/',welly_views.ui_popover,name="ui-popover"),
    path('ui-progressbar/',welly_views.ui_progressbar,name="ui-progressbar"),
    path('ui-tab/',welly_views.ui_tab,name="ui-tab"),
    path('ui-typography/',welly_views.ui_typography,name="ui-typography"),
    path('ui-pagination/',welly_views.ui_pagination,name="ui-pagination"),
    path('ui-grid/',welly_views.ui_grid,name="ui-grid"),
    

    path('uc-select2/',welly_views.uc_select2,name="uc-select2"),
    path('uc-nestable/',welly_views.uc_nestable,name="uc-nestable"),
    path('uc-noui-slider/',welly_views.uc_noui_slider,name="uc-noui-slider"),
    path('uc-sweetalert/',welly_views.uc_sweetalert,name="uc-sweetalert"),
    path('uc-toastr/',welly_views.uc_toastr,name="uc-toastr"),
    path('map-jqvmap/',welly_views.map_jqvmap,name="map-jqvmap"),
    path('uc-lightgallery/',welly_views.uc_lightgallery,name="uc-lightgallery"),

    path('widget-basic/',welly_views.widget_basic,name="widget-basic"),

    path('form-element/',welly_views.form_element,name="form-element"),
    path('form-wizard/',welly_views.form_wizard,name="form-wizard"),
    path('form-editor/',welly_views.form_editor,name="form-editor"),
    path('form-pickers/',welly_views.form_pickers,name="form-pickers"),
    path('form-validation/',welly_views.form_validation,name="form-validation"),

    path('table-bootstrap-basic/',welly_views.table_bootstrap_basic,name="table-bootstrap-basic"),
    path('table-datatable-basic/',welly_views.table_datatable_basic,name="table-datatable-basic"),


    path('page-login/',welly_views.page_login,name="page-login"),
    path('page-register/',welly_views.page_register,name="page-register"),
    path('page-forgot-password/',welly_views.page_forgot_password,name="page-forgot-password"),
    path('page-lock-screen/',welly_views.page_lock_screen,name="page-lock-screen"),
    path('page-empty/',welly_views.page_empty,name="page-empty"),
    path('page-error-400/',welly_views.page_error_400,name="page-error-400"),
    path('page-error-403/',welly_views.page_error_403,name="page-error-403"),
    path('page-error-404/',welly_views.page_error_404,name="page-error-404"),
    path('page-error-500/',welly_views.page_error_500,name="page-error-500"),
    path('page-error-503/',welly_views.page_error_503,name="page-error-503"),

]