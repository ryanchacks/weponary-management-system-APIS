# Weapon Management System API

This is a Flask-based API for managing a weapon inventory system. The API provides endpoints for CRUD operations on weapons, as well as additional filtering and categorization functionalities.

## Endpoints

### CRUD APIs for Weapons (5)
- **GET /weapons** – Get all weapons
- **GET /weapons/<int:weapon_id>** – Get a weapon by ID
- **POST /weapons** – Add a new weapon
- **PUT /weapons/<int:weapon_id>** – Update a w# Weapon Management System API

This is a Flask-based API for managing a weapon inventory system. The API provides endpoints for CRUD operations on weapons, as well as additional filtering and categorization functionalities.

## Endpoints

### CRUD APIs for Weapons (5)
- **GET /weapons** – Get all weapons
- **GET /weapons/<int:weapon_id>** – Get a weapon by ID
- **POST /weapons** – Add a new weapon
- **PUT /weapons/<int:weapon_id>** – Update a weapon by ID
- **DELETE /weapons/<int:weapon_id>** – Delete a weapon by ID

### Weapon Type APIs (4)
- **GET /weapons/types** – Get all weapon types
- **GET /weapons/type/<string:type>** – Get weapons by type
- **POST /weapons/type** – Add a weapon type
- **PUT /weapons/type/<string:type>** – Update a weapon type
- **DELETE /weapons/type/<string:type>** – Delete a weapon type

### Weapon Manufacturer APIs (4)
- **GET /weapons/manufacturers** – Get all manufacturers
- **GET /weapons/manufacturer/<string:manufacturer>** – Get weapons by manufacturer
- **POST /weapons/manufacturer** – Add a manufacturer
- **PUT /weapons/manufacturer/<string:manufacturer>** – Update a manufacturer
- **DELETE /weapons/manufacturer/<string:manufacturer>** – Delete a manufacturer

### Weapon Model APIs (4)
- **GET /weapons/models** – Get all weapon models
- **GET /weapons/model/<string:model>** – Get weapons by model
- **POST /weapons/model** – Add a weapon model
- **PUT /weapons/model/<string:model>** – Update a weapon model
- **DELETE /weapons/model/<string:model>** – Delete a weapon model

### Additional Filtering APIs (10)
- **GET /weapons/calibers** – Get all calibers
- **GET /weapons/caliber/<string:caliber>** – Get weapons by caliber
- **GET /weapons/ammunition** – Get all ammunition types
- **GET /weapons/ammunition/<string:ammunition>** – Get weapons by ammunition
- **GET /weapons/accessories** – Get all accessories
- **GET /weapons/accessory/<string:accessory>** – Get weapons by accessory
- **GET /weapons/countries** – Get all weapon countries
- **GET /weapons/country/<string:country>** – Get weapons by country
- **GET /weapons/statuses** – Get all weapon statuses
- **GET /weapons/status/<string:status>** – Get weapons by status

## Running the Application

1. Ensure you have Python and Flask installed.
2. Save the code in a file named `wepmansys.py`.
3. Run the application using the command:
   ```sh
   python wepmansys.py
   ```
4. The API will be available at `http://127.0.0.1:5000`.
