url = 'localhost'
db = 'prueba'
username = 'demo'
password = 'demo'


from odoo_rpc_client import Client

# assume that odoo server is listening localhost on standard 8069 port and
# have database 'my_db'.
#client = Client('192.168.20.113', 'postgres', 'admin', 'admin', '8071')
client = Client(url, db, username, password)

hr_employee = client['hr.employee']
empleado = hr_employee.search_records([('work_email', '=', 'carlosxtacuri@gmail.com')])
if empleado:
    print(empleado[0])
    id_calendario = empleado[0].resource_calendar_id.id
    resource_calendar = client['resource.calendar']
    horario = resource_calendar.search_records([('id','=', empleado[0].resource_calendar_id.id)])


    # Resource calnedar attendance
    resource_calendar_attendance = client['resource.calendar.attendance']
    dias = resource_calendar_attendance.search_records([('calendar_id', '=', id_calendario)])

    dias_list = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    dia_laboral = {'morning': 'Mañana', 'afternoon': 'Tarde'}

    for i in dias:
        dia = dias_list[int(i.dayofweek)]
        print('Dia: ', dia)
        day_period = i.day_period
        print('M/T: ', dia_laboral.get(day_period))
        print('Inicio: ', i.hour_from, ' - Fin: ', i.hour_to)


    # attendance_ids


