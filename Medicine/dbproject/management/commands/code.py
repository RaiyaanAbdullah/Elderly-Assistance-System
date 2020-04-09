from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        print(time)
'''def increase_count():
	obj=medicine.objects.get(id=3)
	obj.consumption_counter+=1
	obj.save()'''