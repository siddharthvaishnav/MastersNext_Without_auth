from django.core.management.base import BaseCommand
import requests
from home.models import College
from pprint import pprint


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
        api_key = "rS1wJ6t9kIgnxl7ZZsJUphAXfocaJYbVbpF6vCte"
        parameters = {
            'school.state': 'CA',
            'latest.programs.cip_4_digit.credential.level': 5,
            'fields': 'school.name,school.city,school.state,latest.admissions.admission_rate.overall,latest.cost.attendance.academic_year,latest.admissions.sat_scores.average.overall,school.school_url,latest.programs.cip_4_digit.title,latest.cost.net_price.public.by_income_level.0-30000,latest.cost.net_price.public.by_income_level.30001-48000,latest.cost.net_price.public.by_income_level.48001-75000,latest.cost.net_price.public.by_income_level.75001-110000,latest.cost.net_price.public.by_income_level.110001-plus,latest.student.size,earnings.10_yrs_after_entry.median',

            'api_key': 'rS1wJ6t9kIgnxl7ZZsJUphAXfocaJYbVbpF6vCte',
            'per_page': 20
        }
       # site = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.highest=4&latest.programs.cip_4_digit=1401,2401&fields=school.name,latest.programs.cip_4_digit,latest.admissions.admission_rate.overall,latest.cost.attendance.academic_year,school.city,school.state,latest.earnings.10_yrs_after_entry.median&per_page=1000&api_key=rS1wJ6t9kIgnxl7ZZsJUphAXfocaJYbVbpF6vCte'

        response = requests.get(url, params=parameters)
        data = response.json()

        for item in data['results']:
            rate = item["latest.admissions.admission_rate.overall"]
            if rate != None:
                rate = rate*100
                rate = round(rate, 2)

            college = College.objects.create(
                name=item["school.name"],
                course=item["latest.programs.cip_4_digit"],
                student_size=item["latest.student.size"],
                acceptance_rate=rate,
                cost_0_to_30k=item["latest.cost.net_price.public.by_income_level.0-30000"],
                cost_30_to_48k=item["latest.cost.net_price.public.by_income_level.30001-48000"],
                cost_48_to_75k=item["latest.cost.net_price.public.by_income_level.48001-75000"],
                cost_75_to_110k=item["latest.cost.net_price.public.by_income_level.75001-110000"],
                cost_110k_plus=item["latest.cost.net_price.public.by_income_level.110001-plus"],
                # salary=item["latest.earnings.10_yrs_after_entry.median"],
                location=item["school.city"] + ", " + item["school.state"],
                tuition=item["latest.cost.attendance.academic_year"],
                satscore=item["latest.admissions.sat_scores.average.overall"],
                link=item["school.school_url"],
                # duration=item["latest.programs.cip_4_digit"],
            )

            college.save()

        # pprint(data)
        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded college data'))
