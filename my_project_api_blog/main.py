from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

response_api = "https://api.npoint.io/b008dbee3926074bb337"
data_blog = requests.get(response_api)
all_posts = data_blog.json()


@app.route('/')
def home():
    post = [Post(**data) for data in all_posts]
    return render_template("index.html", posts=post)


@app.route("/blog/<int:blog_id>")
def get_blog(blog_id):
    for post in all_posts:
        if post["id"] == blog_id:
            selected_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    return render_template("post.html", posts=selected_post)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
