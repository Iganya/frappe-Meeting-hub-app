// frappe.views.calendar["Meeting"] = {
//     field_map: {
//         "start": "start",
//         "end": "end",
//         "id": "name",
//         "title": "title",
//         "status": "status",
//     },
//     options: {
//         header:{
//             left: 'prev,next today',
//             center: 'title',
//             right: 'month'
//         }
//     },
//     get_events_method: "meeting.api.get_meetings"
// }
frappe.views.calendar['Meeting'] = {
    field_map: {
        start: 'start',
        end: 'end',
        id: 'name',
        allDay: 'all_day',
        title: 'title',
        status: 'status',
        color: 'color'
    },
    style_map: {
        Public: 'success',
        Private: 'info'
    },
    order_by: 'end',
    get_events_method: 'meeting.api.get_meetings'
}