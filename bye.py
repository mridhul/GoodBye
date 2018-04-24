from cisco import friends
import MridhulJosePax as mpax
import json

with open("{}/database/cisco.json".format(root_dir()), "r") as f:
    memories = json.load(f)

'''
Hello *,

As most of you know, today is my last day at Cisco. I would like to thank you for all your support and for all the fun filled moments.

Last 3 years@cisco was really a fantastic journey, a great learning experience and a wonderful opportunity to work with some best technologists and great humans. Thank you all once again and
please keep in touch.

'''

@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "ContactMe": {
            "Linkedin": "https://www.linkedin.com/in/mridhulpax/",
            "FaceBook": "https://www.facebook.com/mjpax",
            "Email"   : "mridhuljospax@gmail.com"
        }
    })



if __name__ == "__main__":
    mpax.run(port=5003, debug=True)


