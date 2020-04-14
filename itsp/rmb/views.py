from django.shortcuts import render
from  .  models import Status
from  .  import tsv1

for i in range(1,10):
    print(i)
    new_entry_col = Status(tsv1.output_sheet(i,1),tsv1.output_sheet(i,2),tsv1.output_sheet(i,3),tsv1.output_sheet(i,4))
    new_entry_col.save()

for i in range(10,20):
    print(i)
    new_entry_col = Status(tsv1.output_sheet(i,1),tsv1.output_sheet(i,2),tsv1.output_sheet(i,3),tsv1.output_sheet(i,4))
    new_entry_col.save()

def homepage(request):

    status_lines = Status.objects.all()
    return render(request,'main.html',{ 'status_lines': status_lines })
