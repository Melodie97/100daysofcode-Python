travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, no_of_visits, city):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = no_of_visits
    new_country["cities"] = city
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
