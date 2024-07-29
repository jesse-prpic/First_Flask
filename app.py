from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contactus():
    return "My contact details are ----- "

courses = [
    {
        "code": 101,
        "Name": "Diploma of IT",
        "duration": "1.5 years",
    },
    {
        "code": 102,
        "Name": "Diploma of Web Dev",
        "duration": "1.5 years",
    },
    {
        "code": 103,
        "Name": "Diploma of Data Science",
        "duration": "2 years",
    },
    {
        "code": 104,
        "Name": "Bachelor of IT",
        "duration": "1.5 years",
    },
    {
        "code": 105,
        "Name": "Bachelor of Web Dev",
        "duration": "2.5 years",
    },
    {
        "code": 106,
        "Name": "Bachelor of Data Science",
        "duration": "4 years",
    }
]

@app.route("/courses")
def list_courses():
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)]
    return courses

@app.route("/courses/101")
def get_course_101():
    return courses[0]

@app.route("/courses/200")
def error_route():
    return{"error": "Course does not exist"}, 404

# POST request
# Add a new course
@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json()
    courses.append(body)
    return courses

# DELETE Request
@app.route("/courses/107", methods=["DELETE"])
def delete_course_107():
    del courses[-1]
    return {"message": "Duplicate course 107 successfully deleted"}

# PUT Request
# Updating an entire course
@app.route("/courses/107", methods=["PUT"])
def put_course_107():
    body = request.get_json()
    courses[-1] = body
    return courses[-1]

# PATCH Request
# Patching a part of a course
@app.route("/courses/101", methods=["PATCH"])
def path_101():
    body = request.get_json()

    courses[0]["duration"] = body.get("duration") or courses[0]["duration"]
    courses[0]["Name"] = body.get("Name") or courses[0]["Name"]

    return courses[0]

if __name__ == "__main__":
    app.run(debug=True)