from flask import Blueprint, render_template, request
from app.model import contacts_collection  # Import the collection from models.py

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch the form data
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('msg')

        # Prepare the document for MongoDB insertion
        contact_data = {
            "name": name,
            "email": email,
            "message": msg
        }

        # Insert the document into the 'contacts' collection
        result = contacts_collection.insert_one(contact_data)

        # Print to console for debugging/logging purposes
        print(f"Inserted document ID: {result.inserted_id}")

        # Success message for user
        success_message = "Thank you for contacting us! Your details have been saved."

        # Pass success message to template
        return render_template('index.html', success_message=success_message)

    # For GET requests, just show the form.
    return render_template('index.html')




# Other Pages
@main.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@main.route('/courses', methods=['GET','POST'])
def services():
    return render_template('courses.html')
@main.route('/trainers', methods=['GET','POST'])
def projects():
    return render_template('trainers.html')

@main.route('/events', methods=['GET','POST'])
def events():
    return render_template('events.html')

@main.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')





