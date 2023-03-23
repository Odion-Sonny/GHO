# from flask import Flask, request, jsonify
# import duckdb

# app = Flask(__name__)
# db = duckdb.connect('my_db.duckdb')

# @app.route('/segmentation', methods=['POST'])
# def segmentation():
#     payload = request.json
    
#     # Get the table name and criteria from the payload
#     table_name = payload.get('table_name')
#     criteria = payload.get('criteria')
    
#     # Build the SQL query based on the criteria
#     query = f"SELECT * FROM {table_name} WHERE "
#     for field, value in criteria.items():
#         if isinstance(value, dict):
#             for key, val in value.items():
#                 query += f"{field}.{key} = '{val}' AND "
#             # Remove the last "AND" from the query
#             query = query[:-5]
#         else:
#             query += f"{field} = '{value}' AND "
#     # Remove the last "AND" from the query
#     query = query[:-5]
    
#     # Execute the query and return the results as JSON
#     results = db.execute(query).fetchall()
#     keys = [column[0] for column in db.execute(f"PRAGMA table_info({table_name})").fetchall()]
#     response = []
#     for row in results:
#         response.append(dict(zip(keys, row)))
#     return jsonify(response)

from flask import Flask, request, jsonify
import duckdb
import logging

app = Flask(__name__)
db = duckdb.connect('my_db.duckdb')

@app.route('/segmentation', methods=['POST'])
def segmentation():
    payload = request.json
    
    # Get the table name and criteria from the payload
    table_name = payload.get('table_name')
    criteria = payload.get('criteria')
    
    # Build the SQL query based on the criteria
    query = f"SELECT DISTINCT users.user_id FROM users INNER JOIN user_events ON users.user_id = user_events.user_id"
    if criteria:
        query += " WHERE "
        for field, value in criteria.items():
            if isinstance(value, dict):
                for key, val in value.items():
                    query += f"{key}.{field} = '{val}' AND "
                # Remove the last "AND" from the query
                query = query[:-5]
            else:
                query += f"{table_name}.{field} = '{value}' AND "
        # Remove the last "AND" from the query
        query = query[:-5]
    # Execute the query and return the results as JSON
    try:
        results = db.execute(query).fetchall()
        response = [row[0] for row in results]
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error executing query {query}: {e}")
        return jsonify({'error': 'Failed to execute query'}), 500
    
if __name__ == '__main__':
    app.run()
