import json
import requests

def parse_command(command_string, config_dict):
    response_string = "I don't understand your command."
    command_string_list = command_string.split()
    try:
        response_string = command_dict[command_string_list[0]](command_string_list[1:], config_dict)
    except KeyError:
        pass
    return response_string

def altitude(string_list, config_dict):
    response_string = "Altitude service error"
    google_map_api_key = config_dict['google_api']['map']
    map_request = 'https://maps.googleapis.com/maps/api/elevation/json?locations=%f, %f&key=%s'
    if len(string_list) != 2:
        response_string = "You need 2 numbers"
    try:
        lat = float(string_list[0].replace(',', ''))
        lng = float(string_list[1].replace(',', ''))
    except:
        response_string = "I am not able to understand your input: %s" % (" ".join(string_list))
        return response_string
    google_response = requests.get(map_request % (lat, lng, google_map_api_key))
    if google_response.status_code == 200:
        google_response_json_dict = json.loads(google_response.text)
        if google_response_json_dict['status'] != 'OK':
            return response_string
        response_string = google_response_json_dict['results'][0]['elevation']
    else:
        pass
    return response_string

command_dict = dict()
command_dict['/altitude'] = altitude
