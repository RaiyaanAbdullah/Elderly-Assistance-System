
from medicines.models import medicine
def increase_count(Id):
    obj=medicine.objects.get(id=Id)
    obj.consumption_counter+=1
    obj.save()
    print("Incremented")

increase_count(3)


    