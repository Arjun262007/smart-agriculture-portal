# Path: smart-agriculture-portal/app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Initial agricultural fields dataset
FIELDS = [
    {"field_id": "F001", "crop": "Wheat", "moisture": 28.5, "water_consumption": 120, "temp": 26.0, "status": "Needs Irrigation", "health": "Good"},
    {"field_id": "F002", "crop": "Corn", "moisture": 45.0, "water_consumption": 95, "temp": 28.2, "status": "Optimal", "health": "Excellent"},
    {"field_id": "F003", "crop": "Rice", "moisture": 22.1, "water_consumption": 210, "temp": 30.5, "status": "Needs Irrigation", "health": "Fair"},
    {"field_id": "F004", "crop": "Soybean", "moisture": 50.2, "water_consumption": 80, "temp": 25.4, "status": "Optimal", "health": "Good"},
    {"field_id": "F005", "crop": "Cotton", "moisture": 29.0, "water_consumption": 150, "temp": 29.1, "status": "Needs Irrigation", "health": "At Risk"}
]

@app.route('/')
def dashboard():
    filter_crop = request.args.get('crop', 'All')
    
    # Enhancement: Field-based filtering
    filtered_fields = [f for f in FIELDS if filter_crop == 'All' or f['crop'] == filter_crop]
    
    # Enhancement Analytics
    total_water = sum(f['water_consumption'] for f in FIELDS)
    lowest_moisture_field = min(FIELDS, key=lambda x: x['moisture'])
    
    # Prioritized irrigation recommendation list (moisture < 30%)
    recommendations = [f for f in FIELDS if f['moisture'] < 30.0]
    
    return render_template(
        'index.html', 
        fields=filtered_fields, 
        total_water=total_water,
        lowest_field=lowest_moisture_field,
        recommendations=recommendations,
        filter_crop=filter_crop
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
