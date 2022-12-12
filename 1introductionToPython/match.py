http_status = int(input('Enter the http status code: '))

match http_status:
    case 200 | 201 :
        print('Connection Ok')
    case 400 :
        print('Bad Request')
    case 500 | 501 :
        print('Server Error')
    case _ :
        print('Unknown')