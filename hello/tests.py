from django.test import TestCase, Client
from django.utils import timezone
from .models import LogMessage, Board, Task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class TestLogMessageModel(TestCase):

    def setUp(self):
        self.log_message = LogMessage.objects.create(
            message='Test Message',
            log_date=timezone.now()
        )

    def test_log_message_creation(self):
        self.assertTrue(isinstance(self.log_message, LogMessage))
        self.assertEqual(self.log_message.message, 'Test Message')

    def test_log_message_str(self):
        expected_object_name = f"'{self.log_message.message}' logged on {timezone.localtime(self.log_message.log_date).strftime('%A, %d %B, %Y at %X')}"
        self.assertEqual(str(self.log_message), expected_object_name)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_not_found_url(self):
        response = self.client.get('/a-url-that-does-not-exist')

        self.assertEquals(response.status_code, 404)


class BoardModelTest(TestCase):
    def test_board_creation(self):
        board = Board.objects.create(name="Test Board")
        self.assertEqual(str(board), "Test Board")


class BoardAPIPermissionsTest(APITestCase):
    def setUp(self):
        # ایجاد گروه و کاربر
        self.admin_group = Group.objects.create(name='board_admin')
        self.user_admin = User.objects.create_user(username='admin', password='pass')
        self.user_admin.groups.add(self.admin_group)
        self.user_normal = User.objects.create_user(username='normal', password='pass')
        self.board = Board.objects.create(name='Test Board', created_by=self.user_admin)

    def test_admin_can_list_boards(self):
        self.client.login(username='admin', password='pass')
        response = self.client.get('/boards/api/boards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_normal_user_cannot_list_boards(self):
        self.client.login(username='normal', password='pass')
        response = self.client.get('/boards/api/boards/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_board(self):
        self.client.login(username='admin', password='pass')
        data = {'name': 'New Board', 'created_by': self.user_admin.id}
        response = self.client.post('/boards/api/boards/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_normal_user_cannot_create_board(self):
        self.client.login(username='normal', password='pass')
        data = {'name': 'Another Board', 'created_by': self.user_normal.id}
        response = self.client.post('/boards/api/boards/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
