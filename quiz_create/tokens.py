from lib2to3.pgen2.tokenize import generate_tokens
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, quiz, timestamp) -> str:
        return (text_type(quiz.pk)+text_type(timestamp))

generate_token = TokenGenerator()