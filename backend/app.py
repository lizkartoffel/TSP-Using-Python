from flask import Flask, request, jsonify
from database import init_db, get_cities
from ga_solver import solve_tsp


app = Flask(__name__, static_folder='../frontend', static_url_path='/')


@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

@app.route('/api/cities', methods=['GET'])
def cities():
    return jsonify(get_cities())

@app.route('/api/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        cities = data.get('cities', [])
        if not cities:
            return jsonify({'error': 'No cities provided'}), 400
        best_route, best_distance = solve_tsp(cities)

        return jsonify({'route': best_route, 'distance': best_distance})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)