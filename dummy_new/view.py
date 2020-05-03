from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv


@api_view(['POST'])
def create_csv(request):
    dict_data = request.data.get('data')
    header = request.data.get('header')

    csv_file = "new.csv"
    csv_columns = header
    try:
        with open(csv_file, 'w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=csv_columns)
            writer.writeheader()
            writer.writerow(dict_data)
    except IOError:
        return Response({"success":False,"message":"Something Went Wrong"})
    return Response({"success":True,"message":"Successfully"})

@api_view(['GET'])
def get_data_from_csv(request):
    file_name =  request.GET.get('file_name')
    arr = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                arr.append(row)
    except IOError:
        return Response({"success":False,"message":"File Not Found"})

    return Response({"success":True,"message":"Successfully","result":arr})





