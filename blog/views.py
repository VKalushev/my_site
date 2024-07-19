from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Vasil",
        "date": date(2024, 7, 21),
        "title": "Mountain Hiking",
        "excerpt" : "There is nothing like the views you get when hiking in the mountains! And I wasn't even prepared whilst I was enjoying the view!",
        "content" : """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eaque nam vel laborum! Odio harum numquam reiciendis 
        voluptatem distinctio pariatur molestias dolorum modi, impedit maiores accusamus nam ipsum fuga possimus magni.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eaque nam vel laborum! Odio harum numquam reiciendis 
        voluptatem distinctio pariatur molestias dolorum modi, impedit maiores accusamus nam ipsum fuga possimus magni.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eaque nam vel laborum! Odio harum numquam reiciendis 
        voluptatem distinctio pariatur molestias dolorum modi, impedit maiores accusamus nam ipsum fuga possimus magni.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Vasil",
        "date": date(2024, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Vasil",
        "date": date(2024, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post['date'])
    latests_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "all_posts": latests_posts[::-1]
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_details(request,slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post" : post 
    })