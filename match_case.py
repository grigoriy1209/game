def process_command(command):
    match command:
        case 'start':
            print('prog_start')
        case 'stop':
            print('prog_stop')
        case _:
            print('unknown command')


command = 'pause '

if command == 'start':
    print('prog_start')
elif command == 'stop':
    print('prog_stop')
elif command == 'pause':
    print('prog_pause')
else:
    print('unknown command')

user = {"role": "wwwww", "status": "active"}

if user['role'] == 'admin' and user['status'] == 'active':
    print('user activate')
elif user['role'] == 'editor' and user['status'] == 'active':
    print('editor activate')
elif user['role'] == 'viewer' and user['status'] == 'inactive':
    print('viewer inactivate')
else:
    print('unknown role status')

user = {"role": "admin", "status": "active"}

match user:
    case {'role': 'admin', 'status': 'active'}:
        print('user activate')
    case {'role': 'editor', 'status': 'active'}:
        print('editor activate')
    case {'role': 'viewer', 'status': 'inactive'}:
        print('viewer inactivate')
    case _:
        print('unknown user status')

