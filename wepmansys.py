from flask import Flask, request, jsonify

app = Flask(__name__)

weapons_data = {
    "weapons": [
        {"id": 1, "name": "AK-47", "type": "Assault Rifle", "manufacturer": "Kalashnikov Concern", "model": "AK-47", "caliber": "7.62mm", "ammunition": "7.62×39mm", "accessories": ["Scope", "Silencer"], "country": "Russia", "year": 1947, "status": "Active", "owner": "Military"},
        {"id": 2, "name": "M16", "type": "Assault Rifle", "manufacturer": "Colt's Manufacturing Company", "model": "M16", "caliber": "5.56mm", "ammunition": "5.56×45mm NATO", "accessories": ["Scope", "Grenade Launcher"], "country": "USA", "year": 1964, "status": "Active", "owner": "Military"},
        # Add more weapons as needed
    ]
}

# CRUD APIs for Weapons
@app.route("/weapons", methods=['GET'])
def get_all_weapons():
    return jsonify(weapons_data['weapons'])

@app.route("/weapons/<int:weapon_id>", methods=['GET'])
def get_weapon_by_id(weapon_id):
    weapon = next((w for w in weapons_data['weapons'] if w['id'] == weapon_id), None)
    if weapon:
        return jsonify(weapon)
    return jsonify({"error": "Weapon not found"}), 404

@app.route("/weapons", methods=['POST'])
def add_weapon():
    new_weapon = request.json
    new_weapon['id'] = len(weapons_data['weapons']) + 1
    weapons_data['weapons'].append(new_weapon)
    return jsonify({"msg": "Weapon added", "weapon": new_weapon}), 201

@app.route("/weapons/<int:weapon_id>", methods=['PUT'])
def update_weapon(weapon_id):
    weapon = next((w for w in weapons_data['weapons'] if w['id'] == weapon_id), None)
    if weapon:
        weapon.update(request.json)
        return jsonify({"msg": "Weapon updated", "weapon": weapon})
    return jsonify({"error": "Weapon not found"}), 404

@app.route("/weapons/<int:weapon_id>", methods=['DELETE'])
def delete_weapon(weapon_id):
    weapon = next((w for w in weapons_data['weapons'] if w['id'] == weapon_id), None)
    if weapon:
        weapons_data['weapons'].remove(weapon)
        return jsonify({"msg": "Weapon deleted"})
    return jsonify({"error": "Weapon not found"}), 404

# Weapon Type APIs
@app.route("/weapons/types", methods=['GET'])
def get_weapon_types():
    types = list(set(w['type'] for w in weapons_data['weapons']))
    return jsonify(types)

@app.route("/weapons/type/<string:type>", methods=['GET'])
def get_weapons_by_type(type):
    weapons = [w for w in weapons_data['weapons'] if w['type'] == type]
    return jsonify(weapons)

@app.route("/weapons/type", methods=['POST'])
def add_weapon_type():
    new_type = request.json['type']
    for weapon in weapons_data['weapons']:
        if weapon['type'] == new_type:
            return jsonify({"error": "Type already exists"}), 400
    weapons_data['weapons'].append({"type": new_type})
    return jsonify({"msg": "Weapon type added", "type": new_type}), 201

@app.route("/weapons/type/<string:type>", methods=['PUT'])
def update_weapon_type(type):
    for weapon in weapons_data['weapons']:
        if weapon['type'] == type:
            weapon['type'] = request.json['type']
            return jsonify({"msg": "Weapon type updated", "type": weapon['type']})
    return jsonify({"error": "Type not found"}), 404

@app.route("/weapons/type/<string:type>", methods=['DELETE'])
def delete_weapon_type(type):
    for weapon in weapons_data['weapons']:
        if weapon['type'] == type:
            weapons_data['weapons'].remove(weapon)
            return jsonify({"msg": "Weapon type deleted"})
    return jsonify({"error": "Type not found"}), 404

# Weapon Manufacturer APIs
@app.route("/weapons/manufacturers", methods=['GET'])
def get_weapon_manufacturers():
    manufacturers = list(set(w['manufacturer'] for w in weapons_data['weapons']))
    return jsonify(manufacturers)

@app.route("/weapons/manufacturer/<string:manufacturer>", methods=['GET'])
def get_weapons_by_manufacturer(manufacturer):
    weapons = [w for w in weapons_data['weapons'] if w['manufacturer'] == manufacturer]
    return jsonify(weapons)

@app.route("/weapons/manufacturer", methods=['POST'])
def add_weapon_manufacturer():
    new_manufacturer = request.json['manufacturer']
    for weapon in weapons_data['weapons']:
        if weapon['manufacturer'] == new_manufacturer:
            return jsonify({"error": "Manufacturer already exists"}), 400
    weapons_data['weapons'].append({"manufacturer": new_manufacturer})
    return jsonify({"msg": "Weapon manufacturer added", "manufacturer": new_manufacturer}), 201

@app.route("/weapons/manufacturer/<string:manufacturer>", methods=['PUT'])
def update_weapon_manufacturer(manufacturer):
    for weapon in weapons_data['weapons']:
        if weapon['manufacturer'] == manufacturer:
            weapon['manufacturer'] = request.json['manufacturer']
            return jsonify({"msg": "Weapon manufacturer updated", "manufacturer": weapon['manufacturer']})
    return jsonify({"error": "Manufacturer not found"}), 404

@app.route("/weapons/manufacturer/<string:manufacturer>", methods=['DELETE'])
def delete_weapon_manufacturer(manufacturer):
    for weapon in weapons_data['weapons']:
        if weapon['manufacturer'] == manufacturer:
            weapons_data['weapons'].remove(weapon)
            return jsonify({"msg": "Weapon manufacturer deleted"})
    return jsonify({"error": "Manufacturer not found"}), 404

# Weapon Model APIs
@app.route("/weapons/models", methods=['GET'])
def get_weapon_models():
    models = list(set(w['model'] for w in weapons_data['weapons']))
    return jsonify(models)

@app.route("/weapons/model/<string:model>", methods=['GET'])
def get_weapons_by_model(model):
    weapons = [w for w in weapons_data['weapons'] if w['model'] == model]
    return jsonify(weapons)

@app.route("/weapons/model", methods=['POST'])
def add_weapon_model():
    new_model = request.json['model']
    for weapon in weapons_data['weapons']:
        if weapon['model'] == new_model:
            return jsonify({"error": "Model already exists"}), 400
    weapons_data['weapons'].append({"model": new_model})
    return jsonify({"msg": "Weapon model added", "model": new_model}), 201

@app.route("/weapons/model/<string:model>", methods=['PUT'])
def update_weapon_model(model):
    for weapon in weapons_data['weapons']:
        if weapon['model'] == model:
            weapon['model'] = request.json['model']
            return jsonify({"msg": "Weapon model updated", "model": weapon['model']})
    return jsonify({"error": "Model not found"}), 404

@app.route("/weapons/model/<string:model>", methods=['DELETE'])
def delete_weapon_model(model):
    for weapon in weapons_data['weapons']:
        if weapon['model'] == model:
            weapons_data['weapons'].remove(weapon)
            return jsonify({"msg": "Weapon model deleted"})
    return jsonify({"error": "Model not found"}), 404

# Additional Filtering APIs
@app.route("/weapons/calibers", methods=['GET'])
def get_weapon_calibers():
    calibers = list(set(w['caliber'] for w in weapons_data['weapons']))
    return jsonify(calibers)

@app.route("/weapons/caliber/<string:caliber>", methods=['GET'])
def get_weapons_by_caliber(caliber):
    weapons = [w for w in weapons_data['weapons'] if w['caliber'] == caliber]
    return jsonify(weapons)

@app.route("/weapons/ammunition", methods=['GET'])
def get_weapon_ammunition():
    ammunition = list(set(w['ammunition'] for w in weapons_data['weapons']))
    return jsonify(ammunition)

@app.route("/weapons/ammunition/<string:ammunition>", methods=['GET'])
def get_weapons_by_ammunition(ammunition):
    weapons = [w for w in weapons_data['weapons'] if w['ammunition'] == ammunition]
    return jsonify(weapons)

@app.route("/weapons/accessories", methods=['GET'])
def get_weapon_accessories():
    accessories = list(set(acc for w in weapons_data['weapons'] for acc in w['accessories']))
    return jsonify(accessories)

@app.route("/weapons/accessory/<string:accessory>", methods=['GET'])
def get_weapons_by_accessory(accessory):
    weapons = [w for w in weapons_data['weapons'] if accessory in w['accessories']]
    return jsonify(weapons)

@app.route("/weapons/countries", methods=['GET'])
def get_weapon_countries():
    countries = list(set(w['country'] for w in weapons_data['weapons']))
    return jsonify(countries)

@app.route("/weapons/country/<string:country>", methods=['GET'])
def get_weapons_by_country(country):
    weapons = [w for w in weapons_data['weapons'] if w['country'] == country]
    return jsonify(weapons)

@app.route("/weapons/statuses", methods=['GET'])
def get_weapon_statuses():
    statuses = list(set(w['status'] for w in weapons_data['weapons']))
    return jsonify(statuses)

@app.route("/weapons/status/<string:status>", methods=['GET'])
def get_weapons_by_status(status):
    weapons = [w for w in weapons_data['weapons'] if w['status'] == status]
    return jsonify(weapons)

if __name__ == '__main__':
    app.run(debug=True) 