from django.shortcuts import render
from datetime import date

# dummy data
all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image": "photo3.jpg",
        "author" : "Eithan Mendez",
        "date": date(2024, 5, 5),
        "title": "Mountain trip",
        "excert": "Today, we got an special trip to relax and rest",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reprehenderit nostrum facere rem suscipit ipsum repudiandae 
            sint est similique ratione explicabo hic, amet veritatis, labore excepturi harum possimus! Accusamus, quam qui?
        """
    },
    {
        "slug" : "django-journey",
        "image": "photo4.jpg",
        "author" : "Eithan Mendez",
        "date": date(2024, 5, 11),
        "title": "Project configuration journey",
        "excert": "There's allways something special when you finish up configuring the barebones of the project that feels really nice",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reprehenderit nostrum facere rem suscipit ipsum repudiandae 
            sint est similique ratione explicabo hic, amet veritatis, labore excepturi harum possimus! Accusamus, quam qui?
        """
    },
    {
        "slug" : "improving-myself",
        "image": "photo5.jpg",
        "author" : "Eithan Mendez",
        "date": date(2024, 5, 12),
        "title": "A hard path ahead",
        "excert": "There's allways something special when you finish up configuring the barebones of the project that feels really nice",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reprehenderit nostrum facere rem suscipit ipsum repudiandae 
            sint est similique ratione explicabo hic, amet veritatis, labore excepturi harum possimus! Accusamus, quam qui?
        """
    }
] 

def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-3:] # starts at the end of the list, moves 3 items from the end of the list
    return render(request, "blog/index.html", { "posts": latest_posts })

def posts(request):
    return render(request, "blog/all-posts.html", { "all_posts": all_posts })

def single_posts(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug) # go through all the posts and look for the slug key if match
    return render(request, "blog/post-detail.html", { "identified_post" : identified_post })
