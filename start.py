from terminatorWeather.models import Location
from terminatorWeather.models import Past
from terminatorWeather.models import Abnormal
from terminatorWeather.scripts import createMonth
from django.contrib.auth import get_user_model

loc = Location()
loc.collectModelLocation()

past = Past()
Past().read_past_weather_file()

abnormal = Abnormal()
Abnormal().find_abnormal_weather()

createMonth()

User = get_user_model()
User.objects.create_superuser("Antoni.Drakon@mail.ru", "KiKBooto")
