from django.conf.urls import url

from tickets import views as t_view
from search.views import TicketLiveSearchAutoCompleteView



urlpatterns = [
    url(
        r'^$',
        t_view.home,
        name='home'
    ),
    url(
        r'^tickets/add/$',
        t_view.add_ticket,
        name='add_ticket'
    ),
    url(
        r'^tickets/files/$',
        t_view.add_files,
        name='add_files'
    ),
    url(
        r'^tickets/read_mail/$',
        t_view.read_mail,
        name='read_mail'
    ),
    url(
        r'^tickets/monkey-test/ajax/$',
        t_view.monkey_test_ajax,
        name = 'monkey_test_ajax'
    ),
    url(
        r'^tickets/edit/(?P<id>[a-z0-9\-_]+)/$',
        t_view.edit_ticket,
        name='edit_ticket'
    ),
    url(
        r'^tickets/download/(?P<file_id>[0-9]+)/$',
        t_view.download_attachment,
        name='download_attachment'
    ),
    url(
        r'^history/(?P<title>[A-Za-z0-9\-_]+)-(?P<id>[0-9]+)/$',
        t_view.history_ticket,
        name='history_ticket'
    ),
    url(
        r'^tickets/delete/(?P<id>[a-z0-9\-]+)/$',
        t_view.delete_ticket,
        name='delete_ticket'
    ),
    url(
        r'^tickets/activate/(?P<id>[0-9]+)/$',
        t_view.activate_ticket,
        name='activate_ticket'
    ),
    url(
        r'^tickets/close/(?P<id>[a-z0-9\-]+)/$',
        t_view.close_ticket,
        name='close_ticket'
    ),
    url(
        r'^tickets/alerts/(?P<id>[a-z0-9\-]+)/$',
        t_view.ticket_add_alert,
        name='ticket_add_alert'
    ),
    url(
        r'^tickets/blacklist/(?P<id>[a-z0-9\-]+)/$',
        t_view.blacklist_ticket,
        name='ticket_blacklist'
    ),
    url(
        r'^tickets/edit/inline/(?P<id>[a-z0-9\-_]+)$',
        t_view.edit_ticket_inline,
        name='edit_ticket_inline'
    ),
    url(
        r'^ws/alerts/(?P<id>[a-z0-9\-_]+)$',
        t_view.ticket_add_alert_inline,
        name='ticket_add_alert_inline'
    ),
    url(
        r'^ws/inline/get/(?P<id>[a-z0-9\-_]+)$',
        t_view.get_answer_inline,
        name='get_answer_inline'
    ),
    url(
        r'^ws/inline/edit$',
        t_view.edit_answer_inline,
        name='edit_answer_inline'
    ),
    url(
        r'^ws/inline/ticket_title/$',
        t_view.get_related_tickets,
        name='get_related_tickets'
    ),
    url(
        r'^ws/inline/gluu_default_values/$',
        t_view.gluu_default_values,
        name='gluu_default_values'
    ),
    url(
        r'^tickets/(?P<title>[a-zA-Z0-9\-_ ]+)$',
        t_view.populate_related_tickets,
        name='populate_related_tickets'
    ),
    url(
        r'^ws/inline/ticket_attachments/$',
        t_view.populate_ticket_data,
        name='populate_ticket_data'
    ),

    url(
        r'^ws/inline/delete/(?P<id>[a-z0-9\-_]+)$',
        t_view.delete_answer_inline,
        name='delete_answer_inline'
    ),
    url(
        r'^ws/inline/company/(?P<company_id>[a-z0-9\-_]+)/$',
        t_view.retrieve_company_members_inline,
        name='retrieve_company_inline'
    ),
    url(
        r'^ws/inline_assign/$',
        t_view.ticket_assign_inline,
        name='ticket_assign_inline'
    ),
    url(
        r'^ws/file/delete/(?P<id>[a-z0-9\-_]+)$',
        t_view.delete_files_inline,
        name='delete_files_inline'
    ),
    url(
        r'^ws/autocomplete-search/$',
        TicketLiveSearchAutoCompleteView.as_view(),
        name='autocomplete_search'
    ),
    url(
        r'^ws/inline/support-plan/(?P<user_id>[a-z0-9\-_]+)/$',
        t_view.retrieve_support_plan,
        name='retrieve_support_plan'
    ),
    url(
        r'^(?P<category>[A-Za-z\-_]+)/$',
        t_view.tickets_lists,
        name='tickets_lists'
    ),
    url(
        r'^(?P<category>[A-Za-z\-_]+)/(?P<id>[0-9]+)/(?P<title>[A-Za-z0-9\-_]+)/$',
        t_view.view_ticket,
        name='view_ticket'
    ),
    url(
        r'^(?P<id>[0-9]+)/$',
        t_view.view_ticket,
        name='view_ticket_shorthand'
    ),
    # This is kept for backwards-compatability
    url(
        r'^(?P<category>[A-Za-z\-_]+)/(?P<title>[A-Za-z0-9\-_]+)-(?P<id>[0-9]+)/$',
        t_view.view_ticket,
        name='view_ticket_old'
    ),
]