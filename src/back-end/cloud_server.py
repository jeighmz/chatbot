from flask import Flask, request, jsonify
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai import APIClient, Credentials
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS
import os

# Load environment variables
load_dotenv()

# Flask app initialization
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Credentials and model setup
api_key = os.getenv("IBM_CLOUD_API_KEY")
url = os.getenv("URL")
project_id = os.getenv("PROJECT_ID")
generate_params = {
    GenParams.MAX_NEW_TOKENS: 100
}
model = Model(
    model_id='meta-llama/llama-3-405b-instruct',
    params=generate_params,
    credentials=Credentials(api_key=api_key, url=url),
    project_id=project_id
)

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # Extract prompt from request
        data = request.json
        prompt = data.get('prompt')
        
        # Check if prompt is provided
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Generate response using the model
        generated_response = model.generate(prompt=prompt)
        generated_text = generated_response['results'][0]['generated_text']
        
        # Return the generated text as JSON
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        # Log the exception
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)