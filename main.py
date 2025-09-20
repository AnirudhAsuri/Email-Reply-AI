import os
import httpx
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
# Note: Set your GROQ_API_KEY in Replit Secrets
def get_groq_client():
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please add it to Replit Secrets.")
    
    # Create a custom HTTP client to avoid proxy conflicts in Replit environment
    custom_client = httpx.Client(
        timeout=60.0,
        # Explicitly disable any proxy configurations
        verify=True
    )
    
    return Groq(
        api_key=api_key,
        http_client=custom_client
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data first (outside try block to ensure variables are defined)
        original_email = request.form.get('original_email', '').strip()
        key_points = request.form.get('key_points', '').strip()
        tone = request.form.get('tone', 'Formal')
        
        try:
            
            # Validate input
            if not original_email:
                return render_template('index.html', 
                                     original_email=original_email,
                                     key_points=key_points,
                                     tone=tone,
                                     error="Please provide the original email.")
            if not key_points:
                return render_template('index.html', 
                                     original_email=original_email,
                                     key_points=key_points,
                                     tone=tone,
                                     error="Please provide key points for your reply.")
            
            # Construct the master prompt using the exact template from requirements
            master_prompt = f"""
As an expert professional communications assistant, your task is to draft a perfect email reply.

**Analyze the original email below:**
---
{original_email}
---

**Use the following key points to construct the reply:**
---
{key_points}
---

**Instructions:**
1. Write a complete email reply.
2. Incorporate all the provided key points naturally into the message.
3. Adopt a strictly **{tone}** tone.
4. Ensure the final output is only the email text, starting with the greeting (e.g., "Hello [Name],") and ending with the sign-off (e.g., "Best regards,"). Do not include any extra commentary.
"""
            
            # Initialize Groq client and generate reply
            client = get_groq_client()
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": master_prompt
                    }
                ],
                model="gemma2-9b-it",
                temperature=0.7,
                max_tokens=1024
            )
            
            generated_reply = chat_completion.choices[0].message.content
            
            return render_template('index.html', 
                                 original_email=original_email,
                                 key_points=key_points,
                                 tone=tone,
                                 generated_reply=generated_reply)
            
        except ValueError as e:
            # Log the actual error for debugging (in production, use proper logging)
            print(f"Configuration error: {str(e)}")
            return render_template('index.html', 
                                 original_email=original_email,
                                 key_points=key_points,
                                 tone=tone,
                                 error="The service is currently unavailable. Please try again later.")
        except Exception as e:
            # Log the actual error for debugging (in production, use proper logging)
            print(f"Error generating reply: {str(e)}")
            return render_template('index.html', 
                                 original_email=original_email,
                                 key_points=key_points,
                                 tone=tone,
                                 error="An unexpected error occurred while generating the reply. Please try again.")
    
    return render_template('index.html')

if __name__ == '__main__':
    # Use debug=False for production deployment
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)