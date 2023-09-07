from flask import request, jsonify
from flask_api import FlaskAPI
app = FlaskAPI(__name__)


@app.route('/skills', methods=['POST'])
def get_skills():
    try:
        data = request.json  # Parse JSON data from the request
        skills = data.get('skills')  # Get the value of the 'skills' key

        if skills and skills is not None:
            try:
                from gensim.models import Word2Vec

                loaded_model = Word2Vec.load("../word2vec2.model")  # Loading Word2Vec model
                similar_skills = loaded_model.wv.most_similar(skills, topn=8)  # Getting similar skills for given skill
                return jsonify({'skills': similar_skills}), 200 
            
            except Exception as e:

                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'Skills key not found in the JSON data'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
