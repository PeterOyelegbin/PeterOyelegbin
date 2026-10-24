from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from reviews.models import Review


class ReviewSubmissionTests(TestCase):
    @patch("projects.views.notify_admin_of_review_submission")
    def test_valid_review_submission_is_saved_for_approval(self, notify_admin):
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "review",
                "full_name": "Jordan Example",
                "email": "jordan@example.com",
                "ratings": "4",
                "comment": "Excellent work.",
            },
        )

        self.assertRedirects(response, reverse("home"))
        review = Review.objects.get(email="jordan@example.com")
        self.assertEqual(review.ratings, 4)
        self.assertFalse(review.verify)
        notify_admin.assert_called_once_with()

    def test_invalid_review_submission_keeps_form_errors(self):
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "review",
                "full_name": "Jordan Example",
                "email": "jordan@example.com",
                "ratings": "9",
                "comment": "Excellent work.",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Select a valid choice")
        self.assertFalse(Review.objects.filter(email="jordan@example.com").exists())

    def test_unverified_reviews_are_not_public(self):
        Review.objects.create(
            full_name="Pending Reviewer",
            email="pending@example.com",
            ratings=5,
            comment="This review is awaiting approval.",
        )

        response = self.client.get(reverse("home"))

        self.assertNotContains(response, "This review is awaiting approval.")


class ContactRequestTests(TestCase):
    @patch("projects.views.notify_admin_of_contact_request")
    def test_valid_contact_request_notifies_admin(self, notify_admin):
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "contact",
                "name": "Taylor Example",
                "email": "taylor@example.com",
                "message": "I need help with a Django API.",
            },
        )

        self.assertRedirects(response, reverse("home"))
        notify_admin.assert_called_once_with(
            name="Taylor Example",
            email="taylor@example.com",
            message="I need help with a Django API.",
        )

    @patch("projects.views.notify_admin_of_contact_request")
    def test_invalid_contact_request_shows_errors_without_notifying(self, notify_admin):
        response = self.client.post(
            reverse("home"),
            {
                "form_type": "contact",
                "name": "Taylor Example",
                "email": "not-an-email",
                "message": "I need help with a Django API.",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address")
        notify_admin.assert_not_called()
