import requests
import pytest

class TestPosts:
    def test_get_post_by_id(self, base_url):
        post_id = 1
        url = f'{base_url}/posts/{post_id}'
        response = requests.get(url)

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        assert response.status_code == 200
        data = response.json()

        required_fields = ['userId', 'id', 'title', 'body']
        for field in required_fields:
            assert field in data

        assert data['id'] == post_id
        assert data['title'] == data['title']

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
        data = response.json()

        assert "id" in data

        assert data['title'] == new_post['title']
        assert data['body'] == new_post['body']
        assert data['userId'] == new_post['userId']

    def test_get_comments_by_id(self, base_url):
        post_id = 1
        url = f'{base_url}/posts/{post_id}/comments'
        response = requests.get(url)

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Response JSON: {response.json()}")

        assert response.status_code == 200
        comments = response.json()

        assert isinstance(comments, list)
        assert len(comments) > 0

        required_fields = ['postId', 'id', 'name', 'email', 'body']

        for comment in comments:
            for field in required_fields:
                assert field in comment

            assert comment['name'] != ''
            assert comment['email'] != ''
            assert comment['body'] != ''
