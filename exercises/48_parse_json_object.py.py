import json


def parse_json_object(text:str)->dict|None:

    try:
        data = json.loads(text)
    except json.decoder.JSONDecodeError:
        return None

    if isinstance(data, dict):
        return data

    return None

if __name__ == "__main__":
    assert parse_json_object('{"name": "Виталий", "age": 25}') == {"name": "Виталий", "age": 25}
    assert parse_json_object(' {} ') == {}
    assert parse_json_object('{"enabled": true, "tags": ["python"], "value": null}') == {"enabled": True, "tags": ["python"], "value": None}
    assert parse_json_object('[1, 2]') is None
    assert parse_json_object('42') is None
    assert parse_json_object('"hello"') is None
    assert parse_json_object('true') is None
    assert parse_json_object('null') is None
    assert parse_json_object('{bad json}') is None
    assert parse_json_object('') is None

    assert parse_json_object('{"name": "Виталий", "age": 32, "type": "engineer"}') == {"name": "Виталий", "age": 32, "type": "engineer"}

#Работает :)
