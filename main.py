'''
Reto Python Día 5
'''
usuarios = {}

options = {
    1: '1. Registrar usuario.',
    2: '2. Consultar usuario.',
    3: '3. Actualizar datos de usuario.',
    4: '4. Eliminar usuario.',
    5: '5. Listar usuarios.',
    6: '6. Salir.' }


def menu():
    for value in options.values():
        print(value)  


def new_user():
    
    contador_id = 1    
    initial_regs = int(input('Ingresa la cantidad de usuarios a registrar: '))

    for _ in range(initial_regs):
        name      = input(f'Ingresa el nombre del usuario #{contador_id}: ')
        while len(name) < 5 or len(name) > 50:
            print('¡Error! El nombre debe tener entre 5 a 50 caracteres')
            name  = input(f'Ingresa el nombre del usuario #{contador_id}: ')        

        last_name     = input(f'Ingresa los apellidos del usuario #{contador_id} ')
        while len(last_name) < 5 or len(last_name) > 50:
            print('¡Error! El apellido debe tener entre 5 a 50 caracteres')
            last_name = input(f'Ingresa los apellidos del usuario #{contador_id}: ')        
            
        phone     = input(f'Ingresa el telefono del usuario #{contador_id} ')
        while len(phone) <= 9:
            print('¡Error! El numero debe tener minimo 10 digitos')
            phone = input(f'Ingresa el telefono del usuario #{contador_id} ')        
            
        email     = input(f'Ingresa el correo electronico del usuario #{contador_id} ')
        while len(email) < 5 or len(email) > 50:
            print('¡Error! El correo debe tener entre 5 a 50 caracteres')
            email = input(f'Ingresa el correo electronico del usuario #{contador_id} ')
              
        usuarios[contador_id] = {"Nombre": name, "Apellidos": last_name, "Telefono": phone, "Email": email}            
        
        contador_id += 1    

        print('')
            
        if contador_id != initial_regs:
            print('\nUsuarios Registrados:')
            print('')
            for id_usuario, datos_usuario in usuarios.items():                    
                print(f'ID: {id_usuario}, Nombre: {datos_usuario['Nombre']} {datos_usuario['Apellidos']}, Telefono: {datos_usuario['Telefono']}, Email: {datos_usuario['Email']}')
                print('')
                
                
def show_user():
    id_usuario = int(input('Ingresa el ID del usuario que deseas consultar: '))
    if id_usuario in usuarios:
        print('Información del usuario:')
        print('')
        for key, value in usuarios[id_usuario].items():
            print(f'{key.capitalize()}: {value}')
    else:
        print('El usuario no está registrado.')
        print('')
        input('Presiona Enter para continuar.')
        

def edit_user():
    id_usuario = int(input('Ingresa el ID del usuario que deseas modificar: '))
    if id_usuario in usuarios:
        for campo in ['Nombre', 'Apellidos', 'Telefono', 'Email']:
            valor = input(f'Ingresa el nuevo {campo} del usuario #{id_usuario}: ')
            while not (5 <= len(valor) <= 50):
                valor = input(f'El {campo} es incorrecto, intentalo de nuevo: ')
            usuarios[id_usuario][campo] = valor
            print('')
            print(f'Datos del usuario #{id_usuario} actualizados correctamente.')
    else:
        print('El usuario no está registrado.')
        print('')
        input('Presiona Enter para continuar.')
        

def delete_user():
    id_usuario = int(input('Ingresa el ID del usuario que deseas eliminar: '))
    if id_usuario in usuarios:
        confirmacion = input(f'¿Estás seguro que quieres eliminar al usuario {id_usuario}? (s/n): ').lower()
        if confirmacion == 's':
            del usuarios[id_usuario]
            print(f'Usuario con ID {id_usuario} eliminado exitosamente.')
        else:
            print('Eliminacion cancelada.')
    else:
        print('El usuario no esta registrado.')


def list_users():
    if usuarios:
        print('Lista de Usuarios:')
        print('')
        for id_usuario, datos_usuario in usuarios.items():
            print(f'ID: {id_usuario}, Nombre: {datos_usuario["Nombre"]} {datos_usuario["Apellidos"]}, Telefono: {datos_usuario["Telefono"]}, Email: {datos_usuario["Email"]}')
    else:
        print('No hay usuarios registrados.')
                         
    
while True:
    print('Sistema de Registro de Usuarios')
    print('')    
    menu()    
    print('')
    option = int(input('Selecciona una opción: '))
    if option == 1:
        new_user()
    elif option == 2:
        show_user()
    elif option == 3:
        edit_user()
    elif option == 4:
        delete_user()
    elif option == 5:
        list_users()  
    elif option == 6:
        print('')
        print('-- Saliendo del Sistema --')
        exit()        
    else:
        print('Opción Invalida')

"""
TODO:
- Abstraer más las funciones
- Crear más validaciones
- Agregar algo más gráfico
"""