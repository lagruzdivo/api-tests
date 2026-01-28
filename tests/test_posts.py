import requests
import pytest
from models import Post, Comment

class TestPosts:
    def test_get_post_by_id(self, base_url):
        post_id = 1
        url = f'{base_url}/posts/{post_id}'
        response = requests.get(url)

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        assert response.status_code == 200
        post_data = response.json()
        validated_post = Post(**post_data)

        assert validated_post.id == post_id

    def test_create_post(self, base_url):
        url = f'{base_url}/posts'
        new_post = {
            'userId': 1,
            'title': 'Test Post',
            'body': 'Test body'
        }
        response = requests.post(url, json=new_post)

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        assert response.status_code == 201
        post_data = response.json()
        validated_post = Post(**post_data)

        assert validated_post.userId == new_post['userId']
        assert validated_post.title == new_post['title']
        assert validated_post.body == new_post['body']

    def test_get_comments_by_id(self, base_url):
        post_id = 1
        url = f'{base_url}/posts/{post_id}/comments'
        response = requests.get(url)

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        assert response.status_code == 200
        comments_data = response.json()

        assert isinstance(comments_data, list)
        assert len(comments_data) > 0

        for comment_data in comments_data:
            comment = Comment(**comment_data)

            assert comment.name != ''
            assert comment.email != ''
            assert comment.body != ''
            assert comment.postId == post_id
