import requests

my_url="https://api.openweathermap.org/data/2.5/onecall"

parameters={
    "lat":26.339750,
    "lon":-81.677680,
    "appid":"e197dd2e82bed6562289f769275dd1c5"
}

response=requests.get(url=my_url, params=parameters)
data=response.json()
data_slice=data["hourly"][:12]

will_rain=False

for hour_Data in data_slice:
    condition_code=hour_Data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain=True

if will_rain:


    my_email = "kk4074919@gmail.com"
    my_password = "kamal1234@"

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kamalpreet24242@gmail.com",
            msg="barish hone wali hai "
        )

