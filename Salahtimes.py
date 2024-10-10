from sun import get_suntime
import datetime

def salahtimes(lat,lng,address):

    sunrise, sunset = get_suntime(lat,lng)
    print(sunrise)
    print(sunset)

    now = datetime.datetime.now()
    date = now.date()
    hour = now.hour
    minute = now.minute
    time = f"{hour}:{minute}"

    sunrise_dt = datetime.datetime.strptime(sunrise,"%H:%M")
    sunset_dt = datetime.datetime.strptime(sunset,"%H:%M")
    day_duration = sunset_dt - sunrise_dt

    # Calculate the duration of the night
    night_duration = datetime.timedelta(days=1) - day_duration

    # Calculate Fajr time
    fajr_angle = 18  # Angle of the sun below the horizon for Fajr
    fajr_duration = night_duration * fajr_angle / 180
    fajr_time = sunrise_dt - fajr_duration

    # Calculate Dhuhr time
    dhuhr_time = sunrise_dt + day_duration / 2

    # Calculate Asr time
    asr_angle = 12  # Angle of the sun below the horizon for Asr
    asr_duration = night_duration * asr_angle / 180
    asr_time = sunset_dt - asr_duration

    # Calculate Maghrib time
    maghrib_time = sunset_dt

    # Calculate Isha time
    isha_angle = 18  # Angle of the sun below the horizon for Isha
    isha_duration = night_duration * isha_angle / 180
    isha_time = sunset_dt + isha_duration

    salah_times = f"Date - {date}\nTime - {time}\nAddress - {address}\n\nSunrise - {sunrise} am\nSunset - {sunset} pm\n\nFajr - {fajr_time.strftime("%H:%M")} am\nZuhr - {dhuhr_time.strftime("%I:%M")} pm\nAsr - {asr_time.strftime("%I:%M")} pm\nMaghrib - {maghrib_time.strftime("%I:%M")} pm\nIsha - {isha_time.strftime("%I:%M")} pm"

    return salah_times

