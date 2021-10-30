from django.http import JsonResponse

calendar = {
    "January": 31,
    "February": 29,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

def get_day(month: int, day: int) -> JsonResponse:
    month_name = list(calendar.keys())[month-1]
    # month_index = list(calendar.keys()).index(month) + 1
    body = {
        "name": f'{month_name} {day}',
        "month": month_name,
        "monthNumber": month,
        "day": day,
        "description": f"Day {day} of {month_name}",
        "external_url": f"https://days.calendar.org/{month}/{day}",
        "attributes": [
           {
             "trait_type": "Month",
             "value": month_name,
           },
           {
             "trait_type": "Day",
             "value": day,
           },
        ]
      }
    return body
   
invalid_body =  {"result": "Invalid day"}

def day_json_view(request, month, day):
    valid_month = month < 13 and month > 0
    num_days = list(calendar.values())[month-1]
    valid_day = day <= num_days and day > 0
    if valid_month and valid_day:
        body = get_day(month, day)
        return JsonResponse(body)
    return JsonResponse(invalid_body, status=400)