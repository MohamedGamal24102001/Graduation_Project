# views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Email
from .forms import EmailForm
from intelligent.views import classify
from .utils import classify_email
import django_filters



# Define a regular expression pattern to match against academic email domains
ACADEMIC_PATTERN = r"^[a-zA-Z0-9._%+-]+@(?:edu|ac\.uk)$"

# Define a dictionary mapping three-letter month abbreviations to their corresponding numeric values
MONTH_DICT = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def find_dates_and_days_in_string(string):
    # Import the necessary libraries
    import re
    import datetime

    # Define a pattern to match against dates in the string
    date_pattern = r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b"

    # Find all instances of the date pattern in the string
    date_matches = re.findall(date_pattern, string)

    # Loop through each date match and convert it to a datetime object
    dates_and_days = []
    for date_match in date_matches:
        date_parts = date_match.split(' ')
        day = int(date_parts[0])
        month = MONTH_DICT[date_parts[1]]
        year = datetime.date.today().year
        date = datetime.date(year, month, day)
        day_of_week = date.strftime('%A')
        dates_and_days.append((date, day_of_week))

    # Return the list of dates and days
    return dates_and_days











class AcademicListView(ListView):
    model = Email
    template_name = 'academic.html'

    def get_queryset(self):
        """
        Return only the emails with academic=True.
        """
        return Email.objects.filter(academic=True)
    #filterset_class = EmailFilter

class HomeView(ListView):
    model = Email
    template_name = 'home.html'
    ordering = ['-email_date']






class AddEmailView(CreateView):
    model = Email
    form_class = EmailForm
    template_name = 'send_message.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Set the academic field based on the email content.
        """
        email = form.save(commit=False)
        label = classify_email(email)
        if label == 'Event':
            email.academic = True
        else:
            email.academic = False
        email.save()

        # Debug output
        print("New email created:")
        print("Subject:", email.subject)
        print("Body:", email.body)
        print("Classification:", label)

        return super().form_valid(form)
class MessageDetailView(DetailView):
    model = Email
    template_name = 'message_details.html'


def welcome_page(request):
    x = "hi amr we have meeting 10 may 2023 at 10:30am "
    print (classify(x) + x)
    return render(request, 'welcome_page.html', {})
    